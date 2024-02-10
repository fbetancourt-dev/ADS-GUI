import sys

import icecream

import math
import struct

from PyQt6.QtCore import QObject, pyqtSignal

import asyncio
import qasync

from dataclasses import dataclass
from functools import cached_property

from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

UART_SAFE_SIZE = 20


@dataclass
class QBleakClient(QObject):
    device: BLEDevice
    ble_is_connected = False

    error_first = True
    errorCode = 0
    dataLength = 0

    maxCount = 104
    count = 0

    error_data = []
    alldata = []
    frames = 0

    values_array = []
    data_ready = False

    data_received = False

    # device_settings
    dev_interpolation_enabled = True

    messageChanged = pyqtSignal(bytes)

    def __post_init__(self):
        super().__init__()

    @cached_property
    def client(self) -> BleakClient:
        return BleakClient(
            self.device,
            disconnected_callback=self._handle_disconnect,
            filters={
                "UUIDs": [UART_SERVICE_UUID],
                "DuplicateData": False,
            }
        )

    async def start(self):
        await self.client.connect()
        await self.client.start_notify(UART_TX_CHAR_UUID, self._handle_read)

    async def stop(self):
        try:
            await self.client.disconnect()
        except:
            print("", end="")

    async def write(self, data):
        self.count = 0
        self.error_first = True
        self.error_data = []
        self.alldata = []
        await self.client.write_gatt_char(UART_RX_CHAR_UUID, data)
        print("sent:", data)

        self.data_received = False

    def _handle_disconnect(self) -> None:
        print("Device was disconnected, goodbye.")
        # cancelling all tasks effectively ends the program
        for task in asyncio.all_tasks():
            task.cancel()

    def _handle_read(self, _: int, data: bytearray) -> None:
        print("received:", data)
        self.data_received = True

        if self.error_first == True:
            # print("error_first")

            for elem in data:
                self.error_data.append(elem)

            # print("error len")
            # print(len(self.error_data))
            # print("error_data")
            # print(self.error_data)

            if self.error_data[0] == 0:
                # print("no errors")
                self.error_first = False

                self.dataLength = self.error_data[1] + (self.error_data[2] << 8)
                # print("dataLength")
                # print(self.dataLength)

                if (self.dataLength == 1) or (self.dataLength == 2):
                    self.maxCount = 1
                else:
                    if self.dev_interpolation_enabled == True:
                        self.dataLength = self.dataLength + 2
                        self.frames = math.ceil(self.dataLength * 8.0 / 20.0)
                    else:
                        self.frames = math.ceil(self.dataLength * 8.0 * 2.0 / 20.0)

                    # print("frames")
                    # print(self.frames)

                    self.maxCount = self.frames
                # print("maxCount")
                # print(self.maxCount)
            else:
                print("", end="")
                # print(self.error_data[0])
        else:
            # print("no_error_first")

            # print("self_count")
            # print(self.count)

            # print("self.maxCount")
            # print(self.maxCount)
            if self.count == 0 and self.maxCount != 0:
                self.alldata = []

            for elem in data:
                self.alldata.append(elem)

            """
            print("alldata len")
            print(len(self.alldata))
            print("alldata")
            print(self.alldata)
            """

            self.count = self.count + 1

            # print("self_count: ", end='')
            # print(self.count, end='')

            # print(" self.maxCount: ", end='')
            # print(self.maxCount)

            if self.count == self.maxCount:
                # print("received double data")
                # print("alldata len")
                # print(len(self.alldata))
                # print("alldata")
                # print(self.alldata)
                # print("double array")
                self.convertDataToDoubleArray()
            else:
                # print("received float data")
                self.convertDataToFloatArray()

    def convertDataToFloatArray(self) -> []:
        i = 0
        values = []

        while i < (len(self.alldata) - 4):
            start = i
            end = i + 4

            subdata = self.alldata[start:end]
            # for elem in subdata:
            #    values.append(elem)
            byte_array = bytes(subdata)
            float_value = struct.unpack("<f", byte_array)[0]
            values.append(float_value)

            i = i + 4
        # print("float values")
        # print(values)
        return values

    def convertDataToDoubleArray(self) -> []:
        self.data_ready = False
        self.values_array.clear()
        values = []

        if self.dataLength == 1:
            values.append(0.0)
        elif self.dataLength == 2:
            start = 0
            end = 2
            subdata = self.alldata[start:end]
            # for elem in subdata:
            #    values.append(elem)
            byte_array = bytes(subdata)
            uint16_value = struct.unpack("<H", byte_array)[0]
            values.append(uint16_value)
        else:
            loopCount = 0
            i = 0
            flag = False
            wvn = []

            if self.dev_interpolation_enabled == True:
                loopCount = self.dataLength * 8
                flag = True
            else:
                loopCount = self.dataLength * 2 * 8

            while i < loopCount:
                start = i
                end = i + 8
                subdata = self.alldata[start:end]

                if (flag == True) and (i >= (loopCount - 16)):
                    # for elem in subdata:
                    #    wvn.append(elem)
                    byte_array = bytes(subdata)
                    int64_value = struct.unpack("<q", byte_array)[0]
                    wvn.append(int64_value)
                    # print("append int 64")
                else:
                    # for elem in subdata:
                    #    values.append(elem)
                    byte_array = bytes(subdata)
                    double_value = struct.unpack("<d", byte_array)[0]
                    values.append(double_value)

                i = i + 8

            if self.dev_interpolation_enabled == True:
                xStep = wvn[len(wvn) - 1]
                wvn.pop(len(wvn) - 1)

                for i in range(1, len(values)):
                    x = wvn[i - 1] + xStep
                    wvn.append(x)

                for i in range(0, len(wvn)):
                    wvn[i] = (wvn[i] >> 3) * 10000
                    x = wvn[i] / (1 << 30)
                    values.append(x)

            # print("double values")
            # print(len(values))
            # print(values)

            self.values_array = values
            self.data_ready = True
        return values
