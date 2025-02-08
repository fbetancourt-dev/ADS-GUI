from PyQt6 import QtCore, QtWidgets, QtGui
from bluetooth_manager import BluetoothManager


class SettingsView(QtWidgets.QWidget):
    def __init__(self, ble_manager, parent=None):
        super(SettingsView, self).__init__(parent)
        print("[DEBUG] SettingsView instance initialized")

        self.ble_manager = ble_manager
        self.ble_manager.connection_changed.connect(self.update_connection_status)
        self.parent = parent
        self.settings = QtCore.QSettings(
            "settings.ini", QtCore.QSettings.Format.IniFormat
        )

        self.setupUi()
        self.load_settings()

        status = "Connected" if self.ble_manager.is_connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

    def setupUi(self):
        print("[DEBUG] Initializing SettingsView UI")
        self.setWindowTitle("Settings")
        self.resize(780, 780)

        mainLayout = QtWidgets.QVBoxLayout(self)

        self.connectionStatusLabel = QtWidgets.QLabel("BLE Status: Disconnected")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.connectionStatusLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 5px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.connectionStatusLabel)

        self.settingsTitle = QtWidgets.QLabel("Settings", self)
        self.settingsTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.settingsTitle.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin: 10px;"
        )
        mainLayout.addWidget(self.settingsTitle)

        gridLayout = QtWidgets.QGridLayout()

        self.widgets = {}
        sourceSettingsGroup = QtWidgets.QGroupBox("SOURCE SETTINGS")
        sourceLayout = QtWidgets.QGridLayout()

        sourceParams = {
            "T1": "Temperature setting 1",
            "T2_MAX": "Maximum temperature setting",
            "T2_C1": "Control parameter 1 for T2",
            "T2_C2": "Control parameter 2 for T2",
            "DeltaT": "Temperature difference",
            "LampSelect": "Select the active lamp",
            "LampCount": "Number of lamps available",
            "Resolution": "Measurement resolution",
        }

        for i, (param, desc) in enumerate(sourceParams.items()):
            label = QtWidgets.QLabel(f"{param}: {desc}")
            if param == "LampSelect":
                widget = QtWidgets.QComboBox()
                widget.addItems(["0", "1"])
            elif param == "LampCount":
                widget = QtWidgets.QComboBox()
                widget.addItems(["0", "1", "2"])
            elif param == "Resolution":
                widget = QtWidgets.QComboBox()
                widget.addItems(["16 nm @ 1500 nm", "32 nm @ 1500 nm"])
            else:
                widget = QtWidgets.QSpinBox()
                widget.setRange(0, 100)

            self.widgets[f"SourceSettings/{param}"] = widget
            sourceLayout.addWidget(label, i, 0)
            sourceLayout.addWidget(widget, i, 1)

        sourceSettingsGroup.setLayout(sourceLayout)
        gridLayout.addWidget(sourceSettingsGroup, 0, 0)

        measurementParamsGroup = QtWidgets.QGroupBox("MEASUREMENT PARAMETERS")
        measurementLayout = QtWidgets.QGridLayout()
        measurementParams = {
            "RunMode": ["Single", "Continuous"],
            "OpticalGainSettings": ["Default", "Calculated", "External"],
        }

        for i, (param, options) in enumerate(measurementParams.items()):
            label = QtWidgets.QLabel(param)
            comboBox = QtWidgets.QComboBox()
            comboBox.addItems(options)
            self.widgets[f"MeasurementParameters/{param}"] = comboBox
            measurementLayout.addWidget(label, i, 0)
            measurementLayout.addWidget(comboBox, i, 1)

        measurementParamsGroup.setLayout(measurementLayout)
        gridLayout.addWidget(measurementParamsGroup, 1, 0)

        displayDataGroup = QtWidgets.QGroupBox("DISPLAY DATA")
        displayLayout = QtWidgets.QGridLayout()
        displayParams = {
            "EnableLinearInterpolation": ["Disabled", "Enabled"],
            "NumberOfDataPoints": [
                " ",
                "65 pts",
                "129 pts",
                "257 pts",
                "513 pts",
                "1024 pts",
                "2048 pts",
                "4096 pts"
            ],
            "EnableFFTSettings": ["Disabled", "Enabled"],
            "ApodizationFunction": ["Boxcar", "Gaussian", "Happ-Genzel", "Lorenz"],
            "NumberOfFFTPoints": [" ", "8 K", "16 K", "32 K"],
        }

        for i, (param, options) in enumerate(displayParams.items()):
            label = QtWidgets.QLabel(param)
            comboBox = QtWidgets.QComboBox()
            comboBox.addItems(options)
            self.widgets[f"DisplayData/{param}"] = comboBox
            displayLayout.addWidget(label, i, 0)
            displayLayout.addWidget(comboBox, i, 1)

        displayDataGroup.setLayout(displayLayout)
        gridLayout.addWidget(displayDataGroup, 0, 1)

        mainLayout.addLayout(gridLayout)

        self.saveButton = QtWidgets.QPushButton("Save Settings", self)
        self.saveButton.setStyleSheet(
            "background-color: #FFA500; color: white; padding: 10px; border-radius: 5px;"
        )
        self.saveButton.clicked.connect(self.save_settings)
        mainLayout.addWidget(self.saveButton)

        self.restoreButton = QtWidgets.QPushButton("Restore Defaults", self)
        self.restoreButton.setStyleSheet(
            "background-color: #FFA500; color: white; padding: 10px; border-radius: 5px;"
        )
        self.restoreButton.clicked.connect(self.restore_defaults)
        mainLayout.addWidget(self.restoreButton)

        navLayout = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.spectrumButton = QtWidgets.QPushButton("Spectrum")
        self.homeButton.setStyleSheet(
            "background-color: #FFA500; color: white; padding: 10px; border-radius: 5px;"
        )
        self.spectrumButton.setStyleSheet(
            "background-color: #FFA500; color: white; padding: 10px; border-radius: 5px;"
        )
        navLayout.addWidget(self.homeButton)
        navLayout.addWidget(self.spectrumButton)
        mainLayout.addLayout(navLayout)

        self.homeButton.clicked.connect(self.goToHomeView)
        self.spectrumButton.clicked.connect(self.goToSpectrumView)

    def load_settings(self):
        for key, widget in self.widgets.items():
            value = self.settings.value(f"DeviceSettings/{key}", 0, type=int)
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentIndex(value)
            else:
                widget.setValue(value)

    def save_settings(self):
        for key, widget in self.widgets.items():
            value = (
                widget.currentIndex()
                if isinstance(widget, QtWidgets.QComboBox)
                else widget.value()
            )
            self.settings.setValue(f"DeviceSettings/{key}", value)
        self.settings.sync()

    def restore_defaults(self):
        for key, widget in self.widgets.items():
            default_value = self.settings.value(f"Defaults/{key}", 0, type=int)
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentIndex(default_value)
            else:
                widget.setValue(default_value)

    def update_connection_status(self, connected):
        status = "Connected" if connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

    def goToHomeView(self):
        print("[DEBUG] Returning to HomeView")
        from views.home_view import HomeView

        if self.parent:
            self.parent.setCentralWidget(HomeView(self.ble_manager, self.parent))

    def goToSpectrumView(self):
        print("[DEBUG] Switching to SpectrumView")
        from views.spectrum_view import SpectrumView

        if self.parent:
            self.parent.setCentralWidget(SpectrumView(self.ble_manager, self.parent))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ble_manager = BluetoothManager()
    window = SettingsView(ble_manager)
    window.show()
    sys.exit(app.exec())
