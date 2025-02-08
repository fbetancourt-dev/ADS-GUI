from PyQt6.QtCore import QObject, pyqtSignal
from bleak import BleakScanner, BleakClient, BleakError
import asyncio
import math
from collections import deque


class BluetoothManager(QObject):
    connection_changed = pyqtSignal(bool)  # Signal to notify about connection status
    data_received = pyqtSignal(bytes)  # Signal to notify when data is received
    data_transfer_complete = pyqtSignal()  # Signal when all data has been received

    UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
    UART_SAFE_SIZE = 20

    def __init__(self):
        super().__init__()
        self.ble_client = None
        self.is_connected = False
        self.data_received_flag = False
        self.expected_data_length = 0
        self.received_data = bytearray()
        self.command_queue = deque()
        self.processing_command = False

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

    def queue_command(self, data: bytearray):
        self.command_queue.append(data)
        if not self.processing_command:
            asyncio.create_task(self._process_queue())

    async def _process_queue(self):
        self.processing_command = True
        while self.command_queue:
            data = self.command_queue.popleft()
            await self.send_data(data)
            await self._wait_for_data_transfer()
        self.processing_command = False

    async def send_data(self, data: bytearray):
        if self.ble_client and self.ble_client.is_connected:
            try:
                print(f"sent: {data}")
                self.data_received_flag = False
                self.received_data = bytearray()
                self.expected_data_length = 0  # Reset before sending

                chunks = [
                    data[i : i + self.UART_SAFE_SIZE]
                    for i in range(0, len(data), self.UART_SAFE_SIZE)
                ]
                for chunk in chunks:
                    await self.ble_client.write_gatt_char(self.UART_RX_CHAR_UUID, chunk)
                    print(f"[DEBUG] Chunk sent: {chunk.hex()}")
            except Exception as e:
                print(f"[ERROR] Failed to send data: {e}")

    async def _wait_for_data_transfer(self):
        while not self.data_received_flag:
            await asyncio.sleep(0.1)

    def _notification_handler(self, sender, data):
        try:
            print(f"received: {data}")

            # Handle the first packet (status + data length)
            if self.expected_data_length == 0:
                status = data[0]
                self.expected_data_length = int.from_bytes(
                    data[1:3], byteorder="little"
                )
                print(
                    f"[DEBUG] Status: {status}, Expected Data Length: {self.expected_data_length}"
                )

                if status != 0:
                    print(f"[ERROR] Device returned error status: {status}")
                    return

                self.received_data.extend(data[3:])  # Add initial data (if any)
            else:
                self.received_data.extend(data)  # Append subsequent packets

            # Check if all data has been received
            if len(self.received_data) >= self.expected_data_length:
                print(f"[DEBUG] All data received ({len(self.received_data)} bytes)")
                self.data_received_flag = True
                self.data_received.emit(bytes(self.received_data))
                self.data_transfer_complete.emit()  # Signal that data transfer is complete

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
