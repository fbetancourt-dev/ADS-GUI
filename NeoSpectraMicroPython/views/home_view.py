from PyQt6 import QtCore, QtWidgets, QtGui
from bleak import BleakScanner, BleakClient, BleakError
import asyncio
import qasync
import traceback  # For better error reporting


class DeviceSelectionDialog(QtWidgets.QDialog):
    def __init__(self, devices, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select BLE Device")
        self.resize(300, 400)

        layout = QtWidgets.QVBoxLayout(self)

        self.device_list = QtWidgets.QListWidget()
        for device in devices:
            if device.name:
                self.device_list.addItem(f"{device.name} ({device.address})")

        self.connect_button = QtWidgets.QPushButton("Connect")
        self.connect_button.clicked.connect(self.handle_connect)

        layout.addWidget(QtWidgets.QLabel("Available Devices:"))
        layout.addWidget(self.device_list)
        layout.addWidget(self.connect_button)

        self.selected_device = None

    def handle_connect(self):
        selected_index = self.device_list.currentRow()
        if selected_index >= 0:
            self.selected_device = self.device_list.item(selected_index).text()
            print(f"[DEBUG] Selected device: {self.selected_device}")
            self.accept()

    def get_selected_device(self):
        return self.selected_device


class HomeView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        print("[DEBUG] HomeView instance initialized")

        self._settings = QtCore.QSettings(
            "settings.ini", QtCore.QSettings.Format.IniFormat
        )
        self.ble_client = None
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        print("[DEBUG] Initializing HomeView UI")
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(382, 780)

        self.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(10)

        assets_dir = self._settings.value("AppSettings/AssetsDir", "./assets/")

        self.logoLabel = QtWidgets.QLabel()
        self.logoLabel.setPixmap(QtGui.QPixmap(f"{assets_dir}mainlogo@3x.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.logoLabel)

        self.infoLabel = QtWidgets.QLabel(
            "Interface with NeoSpectra Micro\nDevelopment Kits using your PC"
        )
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 8px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.infoLabel)

        self.connectionStatusLabel = QtWidgets.QLabel("Please Connect to a Kit")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.connectionStatusLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 5px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.connectionStatusLabel)

        buttonLayout = QtWidgets.QHBoxLayout()
        self.pbHomeConnect = QtWidgets.QPushButton("Connect")
        self.pbHomeConnect.clicked.connect(
            self.debug_connect_button_click
        )  # Debug click detection
        self.pbHomeSettings = QtWidgets.QPushButton("Settings")
        self.pbHomeSettings.clicked.connect(self.openSettingsView)

        buttonLayout.addWidget(self.pbHomeConnect)
        buttonLayout.addWidget(self.pbHomeSettings)
        mainLayout.addLayout(buttonLayout)

        navigationLayout = QtWidgets.QHBoxLayout()
        self.tbMainHome = QtWidgets.QPushButton("Home")
        self.tbMainSpectrum = QtWidgets.QPushButton("Spectrum")

        self.tbMainHome.clicked.connect(self.openHomeView)
        self.tbMainSpectrum.clicked.connect(self.openSpectrumView)

        navigationLayout.addWidget(self.tbMainHome)
        navigationLayout.addWidget(self.tbMainSpectrum)

        mainLayout.addLayout(navigationLayout)

    def debug_connect_button_click(self):
        print("[DEBUG] Connect button clicked!")
        self.connectionStatusLabel.setText("[DEBUG] Button click detected!")
        asyncio.ensure_future(self.handle_ble_connection())  # Ensure coroutine runs

    def openSettingsView(self):
        from views.settings_view import SettingsView

        if self.parent:
            self.parent.setCentralWidget(SettingsView(self.parent))

    def openHomeView(self):
        if self.parent:
            self.parent.setCentralWidget(HomeView(self.parent))

    def openSpectrumView(self):
        from views.spectrum_view import SpectrumView

        if self.parent:
            self.parent.setCentralWidget(SpectrumView(self.parent))

    @qasync.asyncSlot()
    async def handle_ble_connection(self):
        try:
            print(
                f"[DEBUG] Entering handle_ble_connection for button: {self.pbHomeConnect}"
            )
            self.connectionStatusLabel.setText(
                "[DEBUG] Checking BLE connection status..."
            )

            if not self.ble_client or not self.ble_client.is_connected:
                print("[DEBUG] No active connection, attempting to connect")
                await self.connect_ble()
            else:
                print("[DEBUG] Active connection found, attempting to disconnect")
                await self.disconnect_ble()

            print("[DEBUG] Exiting handle_ble_connection")
        except Exception as e:
            print(f"[ERROR] Exception in handle_ble_connection: {e}")
            print(traceback.format_exc())  # Detailed traceback
            self.connectionStatusLabel.setText(f"[ERROR] {e}")

    async def connect_ble(self):
        print("[DEBUG] Entering connect_ble")
        self.connectionStatusLabel.setText("[DEBUG] Starting BLE device scan...")

        try:
            loop = asyncio.get_running_loop()
            print(f"[DEBUG] Event loop running: {loop.is_running()}")

            try:
                devices = await BleakScanner.discover(timeout=10.0)  # Increased timeout
                print(f"[DEBUG] BLE scan complete. Devices found: {len(devices)}")
            except Exception as scan_error:
                print(f"[ERROR] BLE scan failed: {scan_error}")
                print(traceback.format_exc())
                self.connectionStatusLabel.setText("BLE scan failed.")
                return

            if not devices:
                print("[DEBUG] No BLE devices found.")
                self.connectionStatusLabel.setText("No devices found.")
                return

            for device in devices:
                print(
                    f"[DEBUG] Device found: Name={device.name}, Address={device.address}"
                )

            dialog = DeviceSelectionDialog(devices, self)
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                selected_device = dialog.get_selected_device()
                if selected_device:
                    address = selected_device.split("(")[-1].strip(")")
                    print(f"[DEBUG] Connecting to {address}...")
                    self.connectionStatusLabel.setText(f"Connecting to {address}...")
                    self.ble_client = BleakClient(address)
                    await self.ble_client.connect()
                    self.pbHomeConnect.setText("Disconnect")
                    self.connectionStatusLabel.setText(
                        f"Connected to {selected_device}"
                    )
                    print("[DEBUG] Connected successfully.")
        except BleakError as e:
            print(f"[ERROR] BLE connection error: {e}")
            print(traceback.format_exc())  # Detailed traceback
            self.connectionStatusLabel.setText("Connection failed: BLE error")
        except Exception as e:
            print(f"[ERROR] General exception during BLE connection: {e}")
            print(traceback.format_exc())  # Detailed traceback
            self.connectionStatusLabel.setText(f"Connection failed: {e}")

        print("[DEBUG] Exiting connect_ble")

    async def disconnect_ble(self):
        print("[DEBUG] Attempting to disconnect BLE device...")
        self.connectionStatusLabel.setText("[DEBUG] Disconnecting BLE device...")

        try:
            if self.ble_client and self.ble_client.is_connected:
                await self.ble_client.disconnect()
                self.pbHomeConnect.setText("Connect")
                self.connectionStatusLabel.setText("Please Connect to a Kit")
                print("[DEBUG] Disconnected successfully.")
            else:
                print("[DEBUG] No device to disconnect.")
                self.connectionStatusLabel.setText("No device connected.")
        except Exception as e:
            print(f"[ERROR] Exception during BLE disconnection: {e}")
            print(traceback.format_exc())  # Detailed traceback
            self.connectionStatusLabel.setText(f"Disconnection failed: {e}")


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        loop = qasync.QEventLoop(app)
        asyncio.set_event_loop(loop)

        window = HomeView()
        window.show()

        loop.run_forever()
    except Exception as e:
        print(f"[CRITICAL ERROR] {e}")
        print(traceback.format_exc())  # Catching any unhandled errors at app level
