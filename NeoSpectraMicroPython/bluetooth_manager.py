from PyQt6.QtCore import QObject, pyqtSignal
from bleak import BleakScanner, BleakClient, BleakError
import asyncio


class BluetoothManager(QObject):
    connection_changed = pyqtSignal(bool)  # Signal to notify about connection status

    def __init__(self):
        super().__init__()
        self.ble_client = None
        self.is_connected = False

    async def connect_device(self, address):
        try:
            self.ble_client = BleakClient(address)
            await self.ble_client.connect()
            self.is_connected = True
            self.connection_changed.emit(True)
            print(f"[DEBUG] Connected to {address}")
        except Exception as e:
            print(f"[ERROR] Failed to connect: {e}")
            self.connection_changed.emit(False)

    async def disconnect_device(self):
        if self.ble_client and self.ble_client.is_connected:
            await self.ble_client.disconnect()
            self.is_connected = False
            self.connection_changed.emit(False)
            print("[DEBUG] Disconnected")

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
