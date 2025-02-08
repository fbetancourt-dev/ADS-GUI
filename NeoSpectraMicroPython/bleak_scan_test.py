import sys
import asyncio
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QLabel,
    QMessageBox,
)
from PyQt6.QtCore import QThread, pyqtSignal
from bleak import BleakScanner, BleakClient

# UART Service and Characteristic UUIDs
UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"


class BLEScannerThread(QThread):
    device_found = pyqtSignal(str, str)
    log_message = pyqtSignal(str)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def scan():
            def detection_callback(device, advertisement_data):
                self.log_message.emit(
                    f"Detected device: {device.name or 'Unknown'} - {device.address}"
                )
                if device.name and "NeoSpectra" in device.name:
                    self.device_found.emit(device.name, device.address)

            scanner = BleakScanner(detection_callback=detection_callback)
            await scanner.start()
            await asyncio.sleep(10)
            await scanner.stop()

        loop.run_until_complete(scan())
        loop.close()


class BLEConnectThread(QThread):
    log_message = pyqtSignal(str)
    connected = pyqtSignal(bool)

    def __init__(self, address):
        super().__init__()
        self.address = address
        self.client = None

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        async def connect():
            try:
                self.client = BleakClient(self.address)
                await self.client.connect()
                if self.client.is_connected:
                    self.log_message.emit(f"Connected to {self.address}")
                    self.connected.emit(True)
                else:
                    self.log_message.emit(f"Failed to connect to {self.address}")
                    self.connected.emit(False)
            except Exception as e:
                self.log_message.emit(f"Failed to connect: {e}")
                self.connected.emit(False)

        self.loop.run_until_complete(connect())

    def disconnect(self):
        if self.client and self.client.is_connected:

            async def async_disconnect():
                try:
                    await self.client.disconnect()
                    self.log_message.emit("Disconnected successfully")
                except Exception as e:
                    self.log_message.emit(f"Failed to disconnect: {e}")

            self.loop.run_until_complete(async_disconnect())
            self.loop.stop()
            self.loop.close()


class BLEScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BLE UART Scanner")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Click 'Scan' to find BLE UART devices")
        layout.addWidget(self.label)

        self.scan_button = QPushButton("Scan")
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_device)
        layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton("Disconnect")
        self.disconnect_button.clicked.connect(self.disconnect_device)
        layout.addWidget(self.disconnect_button)

        self.device_list = QListWidget()
        layout.addWidget(self.device_list)

        self.log_list = QListWidget()
        layout.addWidget(self.log_list)

        self.setLayout(layout)

        self.scanner_thread = BLEScannerThread()
        self.scanner_thread.device_found.connect(self.add_device)
        self.scanner_thread.log_message.connect(self.log_message)

        self.connect_thread = None

    def start_scan(self):
        self.device_list.clear()
        self.log_list.clear()
        self.label.setText("Scanning for devices...")
        self.scanner_thread.start()

    def add_device(self, name, address):
        if not any(
            address in self.device_list.item(i).text()
            for i in range(self.device_list.count())
        ):
            self.device_list.addItem(f"{name} ({address})")
        self.label.setText("Scan complete. Devices found:")

    def log_message(self, message):
        self.log_list.addItem(message)
        self.log_list.scrollToBottom()  # Auto-scroll to the latest item

    def connect_device(self):
        selected = self.device_list.currentItem()
        if selected:
            address = selected.text().split("(")[-1].strip(")")
            self.connect_thread = BLEConnectThread(address)
            self.connect_thread.log_message.connect(self.log_message)
            self.connect_thread.start()
        else:
            QMessageBox.warning(
                self, "No Device Selected", "Please select a device to connect."
            )

    def disconnect_device(self):
        if (
            self.connect_thread
            and self.connect_thread.client
            and self.connect_thread.client.is_connected
        ):
            self.connect_thread.disconnect()
        else:
            QMessageBox.warning(
                self,
                "No Device Connected",
                "There is no active connection to disconnect.",
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BLEScannerApp()
    window.show()
    sys.exit(app.exec())
