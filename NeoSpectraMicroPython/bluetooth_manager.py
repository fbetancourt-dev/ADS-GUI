from PyQt6.QtCore import QObject, pyqtSignal
from bleak import BleakScanner, BleakClient, BleakError
import asyncio


class BluetoothManager(QObject):
    connection_changed = pyqtSignal(bool)  # Signal to notify about connection status
    data_received = pyqtSignal(bytes)  # Signal to notify when data is received

    UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_SAFE_SIZE = 20

    def __init__(self):
        super().__init__()
        self.ble_client = None
        self.is_connected = False
        self.data_received_flag = False

    async def connect_device(self, address):
        try:
            self.ble_client = BleakClient(
                address,
                disconnected_callback=self._handle_disconnection,
                filters={
                    "UUIDs": [self.UART_SERVICE_UUID],
                    "DuplicateData": False,
                },
            )
            await self.ble_client.connect()
            await self.ble_client.start_notify(
                self.UART_TX_CHAR_UUID, self._notification_handler
            )
            self.is_connected = True
            self.connection_changed.emit(True)
            print(f"[DEBUG] Connected to {address}")
        except Exception as e:
            print(f"[ERROR] Failed to connect: {e}")
            self.connection_changed.emit(False)

    async def disconnect_device(self):
        if self.ble_client and self.ble_client.is_connected:
            try:
                await self.ble_client.stop_notify(self.UART_TX_CHAR_UUID)
                await self.ble_client.disconnect()
                self.is_connected = False
                self.connection_changed.emit(False)
                print("[DEBUG] Disconnected")
            except Exception as e:
                print(f"[ERROR] Failed to disconnect: {e}")

    def is_connected(self):
        return self.ble_client and self.ble_client.is_connected

    async def scan_devices(self):
        try:
            devices = await BleakScanner.discover(timeout=10.0)
            print(f"[DEBUG] Devices found: {len(devices)}")
            return devices
        except Exception as e:
            print(f"[ERROR] BLE scan failed: {e}")
            return []

    async def send_data(self, data: bytearray):
        if self.ble_client and self.ble_client.is_connected:
            try:
                print(f"sent: {data}")
                self.data_received_flag = False
                chunks = [
                    data[i : i + self.UART_SAFE_SIZE]
                    for i in range(0, len(data), self.UART_SAFE_SIZE)
                ]
                for chunk in chunks:
                    await self.ble_client.write_gatt_char(self.UART_RX_CHAR_UUID, chunk)
                    print(f"[DEBUG] Chunk sent: {chunk.hex()}")
            except Exception as e:
                print(f"[ERROR] Failed to send data: {e}")

    def _notification_handler(self, sender, data):
        try:
            print(f"received: {data}")
            self.data_received_flag = True
            self.data_received.emit(bytes(data))
            print("[DEBUG] Data emission successful")
        except Exception as e:
            print(f"[ERROR] Exception in notification handler: {e}")

    def _handle_disconnection(self, client):
        print("[DEBUG] Device disconnected")
        self.is_connected = False
        self.connection_changed.emit(False)

    async def start(self):
        try:
            await self.ble_client.connect()
            await self.ble_client.start_notify(
                self.UART_TX_CHAR_UUID, self._notification_handler
            )
            print("[DEBUG] BLE notifications started")
        except Exception as e:
            print(f"[ERROR] Failed to start BLE client: {e}")

    async def stop(self):
        try:
            await self.ble_client.disconnect()
            print("[DEBUG] BLE client stopped")
        except Exception as e:
            print(f"[ERROR] Failed to stop BLE client: {e}")
