from PyQt6 import QtCore, QtWidgets, QtGui

from device_settings_class import DeviceSettings

class SpectrumView(QtWidgets.QWidget):
    def __init__(self, ble_manager, parent=None):
        super(SpectrumView, self).__init__(parent)
        print("[DEBUG] SpectrumView instance initialized")

        self.ble_manager = ble_manager
        self.ble_manager.connection_changed.connect(self.update_connection_status)
        self.parent = parent
        self.scanned_samples = 0
        self.setupUi()

        status = "Connected" if self.ble_manager.is_connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

        self.settings = DeviceSettings()
        print(self.settings.device_data["SourceSettings/T2_C2"])

    def setupUi(self):
        print("[DEBUG] Initializing SpectrumView UI")
        self.setWindowTitle("Spectrum View")
        self.resize(382, 780)

        self.setStyleSheet(
            """
            QWidget {
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton {
                background-color: #FF6600;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF8533;
            }
            QLabel {
                color: #333;
            }
        """
        )

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(10, 10, 10, 10)
        mainLayout.setSpacing(10)

        self.titleLabel = QtWidgets.QLabel("Spectrum Analysis")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        mainLayout.addWidget(self.titleLabel)

        self.connectionStatusLabel = QtWidgets.QLabel("BLE Status: Disconnected")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.connectionStatusLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 5px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.connectionStatusLabel)

        buttonLayoutTop = QtWidgets.QHBoxLayout()
        self.saveBGButton = QtWidgets.QPushButton("Save BG")
        self.restoreBGButton = QtWidgets.QPushButton("Restore BG")
        buttonLayoutTop.addWidget(self.saveBGButton)
        buttonLayoutTop.addWidget(self.restoreBGButton)
        mainLayout.addLayout(buttonLayoutTop)

        self.numScansLabel = QtWidgets.QLabel("No. Of Scans:")
        self.numScansInput = QtWidgets.QSpinBox()
        self.numScansInput.setRange(1, 100)
        self.numScansInput.setValue(3)

        self.scanTimeLabel = QtWidgets.QLabel("Scan Time (seconds):")
        self.scanTimeInput = QtWidgets.QSpinBox()
        self.scanTimeInput.setRange(1, 60)
        self.scanTimeInput.setValue(10)

        mainLayout.addWidget(self.numScansLabel)
        mainLayout.addWidget(self.numScansInput)
        mainLayout.addWidget(self.scanTimeLabel)
        mainLayout.addWidget(self.scanTimeInput)

        self.startBGButton = QtWidgets.QPushButton("Start BG")
        self.startBGButton.clicked.connect(self.start_bg)

        self.startScanButton = QtWidgets.QPushButton("Start Scan")
        self.startScanButton.clicked.connect(self.start_scan)

        startButtonLayout = QtWidgets.QVBoxLayout()
        startButtonLayout.addWidget(self.startBGButton)
        startButtonLayout.addWidget(self.startScanButton)
        mainLayout.addLayout(startButtonLayout)

        self.samplesLabel = QtWidgets.QLabel("Number of Scanned Samples: 0")
        self.samplesLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.samplesLabel)

        self.filePathLabel = QtWidgets.QLabel("Save As:")
        self.fileNameInput = QtWidgets.QLineEdit()
        self.fileNameInput.setPlaceholderText("Filename")
        self.fileNameInput.textChanged.connect(self.update_file_extensions)

        self.jsonFileNameLabel = QtWidgets.QLabel(".json")
        self.csvFileNameLabel = QtWidgets.QLabel(".csv")

        mainLayout.addWidget(self.filePathLabel)
        mainLayout.addWidget(self.fileNameInput)
        mainLayout.addWidget(self.jsonFileNameLabel)
        mainLayout.addWidget(self.csvFileNameLabel)

        self.toLabel = QtWidgets.QLabel("To:")
        self.filePathInput = QtWidgets.QLineEdit()
        self.browseButton = QtWidgets.QPushButton("...")
        self.browseButton.clicked.connect(self.browse_files)

        fileLayout = QtWidgets.QHBoxLayout()
        fileLayout.addWidget(self.filePathInput)
        fileLayout.addWidget(self.browseButton)
        mainLayout.addWidget(self.toLabel)
        mainLayout.addLayout(fileLayout)

        self.clearButton = QtWidgets.QPushButton("Clear")
        self.clearButton.clicked.connect(self.clear_results)
        self.saveButton = QtWidgets.QPushButton("Save")
        self.saveButton.clicked.connect(self.save_results)

        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.clearButton)
        buttonLayout.addWidget(self.saveButton)
        mainLayout.addLayout(buttonLayout)

        navigationLayout = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.homeButton.clicked.connect(self.openHomeView)
        self.spectrumButton = QtWidgets.QPushButton("Spectrum")
        self.spectrumButton.clicked.connect(self.openSpectrumView)

        navigationLayout.addWidget(self.homeButton)
        navigationLayout.addWidget(self.spectrumButton)
        mainLayout.addLayout(navigationLayout)

        self.ble_manager.connection_changed.connect(self.update_connection_status)

    def update_file_extensions(self, text):
        self.jsonFileNameLabel.setText(f"{text}.json")
        self.csvFileNameLabel.setText(f"{text}.csv")

    def update_connection_status(self, connected):
        status = "Connected" if connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

    def start_bg(self):
        if self.ble_manager.ble_client and self.ble_manager.ble_client.is_connected:
            print("[DEBUG] Starting background measurement...")
            self.scanned_samples += 1
            self.update_samples_label()
        else:
            print("[DEBUG] BLE device not connected.")

    def start_scan(self):
        if self.ble_manager.ble_client and self.ble_manager.ble_client.is_connected:
            print("[DEBUG] Starting scan measurement...")
            self.scanned_samples += 1
            self.update_samples_label()
        else:
            print("[DEBUG] BLE device not connected.")

    def update_samples_label(self):
        self.samplesLabel.setText(f"Number of Scanned Samples: {self.scanned_samples}")

    def clear_results(self):
        print("[DEBUG] Clearing measurement results")
        self.scanned_samples = 0
        self.update_samples_label()

    def save_results(self):
        print("[DEBUG] Saving measurement results")

    def browse_files(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if file_path:
            self.filePathInput.setText(file_path)

    def openHomeView(self):
        print("[DEBUG] Returning to HomeView")
        from views.home_view import HomeView

        if self.parent:
            self.parent.setCentralWidget(HomeView(self.ble_manager, self.parent))

    def openSpectrumView(self):
        print("[DEBUG] Already in SpectrumView")
