from PyQt6.QtCore import QObject, pyqtSignal
import asyncio

from device_settings_class import DeviceSettings

class SpectrometerController(QObject):
    operation_complete = pyqtSignal(
        str, bytes
    )  # Signal to notify when an operation is complete

    def __init__(self, ble_manager):
        super().__init__()
        self.ble_manager = ble_manager

        if self.ble_manager:
            print("[DEBUG] BLE Manager linked successfully.")

            self.ble_manager.data_received.connect(self._handle_data_received)
            self.ble_manager.data_transfer_complete.connect(
                self._handle_transfer_complete
            )

            self.current_command = None

            self.settings = DeviceSettings()
        else:
            print("[ERROR] BLE Manager is None!")

    def set_optical_settings(self, gain_setting):
        command = bytearray([0x1B])  # Command ID for optical settings
        command.extend(gain_setting.to_bytes(2, "little"))
        # self._send_command("set_optical_settings", command)
        # Schedule the coroutine properly
        asyncio.create_task(self._send_command("set_optical_settings", command))

    def set_source_settings(
        self, lamp_select, lamp_count, delta_t, t1, t2_max, t2_c1, t2_c2
    ):
        '''
        command = bytearray([0x16])  # Command ID for source settings
        command.extend(lamp_select.to_bytes(1, "little"))
        command.extend(lamp_count.to_bytes(1, "little"))
        command.extend(delta_t.to_bytes(2, "little"))
        command.extend(t1.to_bytes(2, "little"))
        command.extend(t2_max.to_bytes(2, "little"))
        command.extend(t2_c1.to_bytes(2, "little"))
        command.extend(t2_c2.to_bytes(2, "little"))
        '''

        '''
        command = bytearray()
        command.append(0x16)  # Operation ID for setSourceSettings
        
        # Add the parameters according to the BLE packet structure
        command.append(lamp_select)
        command.append(lamp_count)
        
        # Reserved bytes (2 bytes)
        command.extend((0x00, 0x00))
        
        command.append(t1)
        command.append(delta_t)
        
        # Reserved bytes (2 bytes)
        command.extend((0x00, 0x00))
        
        command.append(t2_c1)
        command.append(t2_c2)
        command.append(t2_max)
        
        '''
        value1 = lamp_select * 256 + lamp_count
        value2 = delta_t * 256 + t1
        value3 = t2_max * 65536 + t2_c2 * 256 + t2_c1

        value1Bytes = value1.to_bytes(4, "little")
        value2Bytes = value2.to_bytes(4, "little")
        value3Bytes = value3.to_bytes(4, "little")

        command = bytearray()
        command.append(0x16)  # Operation ID for setSourceSettings
        command.append(value1Bytes[0])
        command.append(value1Bytes[1])
        command.append(value1Bytes[2])
        command.append(value1Bytes[3])
        command.append(value2Bytes[0])
        command.append(value2Bytes[1])
        command.append(value2Bytes[2])
        command.append(value2Bytes[3])
        command.append(value3Bytes[0])
        command.append(value3Bytes[1])
        command.append(value3Bytes[2])
        command.append(value3Bytes[3])
        asyncio.create_task(self._send_command("set_source_settings", command))

    def run_background(
        self,
        scan_time,
        interpolation_enabled,
        data_points,
        optical_settings,
        apodization,
        zero_padding,
        run_mode,
    ):
        '''
        command = bytearray([0x04])  # Command ID for background scan
        command.extend(scan_time.to_bytes(3, "little"))
        command.append(interpolation_enabled)
        command.append(data_points)
        command.append(optical_settings)
        command.append(apodization)
        command.append(zero_padding)
        command.append(run_mode)
        '''

        command = bytearray([0x04])  # Command ID for background scan
        st = int(scan_time) * 1000
        scan_time_byte = st.to_bytes(3, "little")
        command.append(scan_time_byte[0])
        command.append(scan_time_byte[1])
        command.append(scan_time_byte[2])

        # get common WL value
        if interpolation_enabled == 1:
            if data_points == 0:
                command.append(5)
            else:
                command.append(data_points)
        else:
            command.append(0)

        # get optical settings value

        # if optical_settings_option != None:
        if optical_settings == 0:
            command.append(0)
        else:
            command.append(2)

        # get apodization window value
        command.append(apodization)

        zero_padding = apodization = int(
            self.settings.device_data["DisplayData/NumberOfFFTPoints"]
        )
        resolution = int(
            self.settings.device_data["SourceSettings/Resolution"]
        )

        if resolution == 1:
            resolution = 0
        else:
            resolution = 1

        if zero_padding == 0:
            zero_padding = 1 + 128 * resolution
            command.append(zero_padding)
        else:
            zero_padding = zero_padding + 128 * resolution
            command.append(zero_padding)
        # get run mode
        run_mode = int(
            self.settings.device_data["MeasurementParameters/RunMode"]
        )
        command.append(run_mode * 5)

        asyncio.create_task(self._send_command("run_background", command))

    def run_absorbance(
        self,
        scan_time,
        interpolation_enabled,
        data_points,
        optical_settings,
        apodization,
        zero_padding,
        run_mode,
    ):
        command = bytearray([0x05])  # Command ID for absorbance scan
        command.extend(scan_time.to_bytes(3, "little"))
        command.append(interpolation_enabled)
        command.append(data_points)
        command.append(optical_settings)
        command.append(apodization)
        command.append(zero_padding)
        command.append(run_mode)
        self._send_command("run_absorbance", command)

    async def _send_command(self, command_name, command):
        if self.ble_manager.is_connected:
            print(f"[DEBUG] Sending command: {command_name}")
            self.current_command = command_name  # Track the current command
            self.ble_manager.queue_command(command)
        else:
            print("[ERROR] BLE device not connected.")

    def _handle_data_received(self, data):
        if self.current_command:
            print(f"[DEBUG] Data received in SpectrometerController: {data.hex()}")
            # Emit signal when data is received
            self.operation_complete.emit(self.current_command, data)
            self.current_command = None

    def _handle_transfer_complete(self):
        print("[DEBUG] Data transfer complete.")
