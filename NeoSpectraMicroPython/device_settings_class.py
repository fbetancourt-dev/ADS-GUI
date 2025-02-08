from PyQt6 import QtCore

class DeviceSettings:
    def __init__(self, settings_file="settings.ini"):
        self.settings = QtCore.QSettings(settings_file, QtCore.QSettings.Format.IniFormat)
        self.load_settings()

    def load_settings(self):
        self.device_data = {
            key: self.settings.value(f"DeviceSettings/{key}", 0, type=int)
            for key in [
                "SourceSettings/T1",
                "SourceSettings/T2_MAX",
                "SourceSettings/T2_C1",
                "SourceSettings/T2_C2",
                "SourceSettings/DeltaT",
                "SourceSettings/LampSelect",
                "SourceSettings/LampCount",
                "SourceSettings/Resolution",
                "MeasurementParameters/RunMode",
                "MeasurementParameters/OpticalGainSettings",
                "DisplayData/EnableLinearInterpolation",
                "DisplayData/NumberOfDataPoints",
                "DisplayData/EnableFFTSettings",
                "DisplayData/FFTSettings",
                "DisplayData/ApodizationFunction",
                "DisplayData/NumberOfFFTPoints",
            ]
        }

        self.app_data = {
            key: self.settings.value(f"AppSettings/{key}", "")
            for key in [
                "WorkingDirectory", "BLEScanTimeout", "IOButtonEnabled"
            ]
        }

        self.scan_data = {
            key: self.settings.value(f"ScanSettings/{key}", "") if key == "FileName" else self.settings.value(f"ScanSettings/{key}", 0, type=int)
            for key in [
                "FileName", "NumberOfScans", "ScanTime"
            ]
        }

    def save_settings(self):
        for key, value in self.device_data.items():
            self.settings.setValue(f"DeviceSettings/{key}", value)

        for key, value in self.app_data.items():
            self.settings.setValue(f"AppSettings/{key}", value)

        for key, value in self.scan_data.items():
            self.settings.setValue(f"ScanSettings/{key}", value)

        self.settings.sync()

    def restore_defaults(self):
        for key in self.device_data.keys():
            self.device_data[key] = self.settings.value(f"Defaults/DeviceSettings/{key}", 0, type=int)

        for key in self.app_data.keys():
            self.app_data[key] = self.settings.value(f"Defaults/AppSettings/{key}", "")

        for key in self.scan_data.keys():
            self.scan_data[key] = self.settings.value(f"Defaults/ScanSettings/{key}", "") if key == "FileName" else self.settings.value(f"Defaults/ScanSettings/{key}", 0, type=int)

        self.save_settings()


# Usage in other views
# from device_settings_class import DeviceSettings
# device_settings = DeviceSettings()
# device_settings.load_settings()
# device_settings.save_settings()
