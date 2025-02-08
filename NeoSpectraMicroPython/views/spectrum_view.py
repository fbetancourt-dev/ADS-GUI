from PyQt6 import QtCore, QtWidgets, QtGui


class SpectrumView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SpectrumView, self).__init__(parent)
        self._settings = QtCore.QSettings("settings.ini", QtCore.QSettings.Format.IniFormat)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(382, 780)

        # Apply main stylesheet
        self.setStyleSheet("""
            QWidget {
                font-family: 'Arial';
                font-size: 14px;
            }
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
            QLabel {
                color: #333;
            }
            QFrame {
                background-color: #f5f5f5;
            }
        """)

        # Main Layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(10, 10, 10, 10)
        mainLayout.setSpacing(10)

        # Save and Restore Buttons
        self.saveBGButton = QtWidgets.QPushButton("Save BG")
        self.restoreBGButton = QtWidgets.QPushButton("Restore BG")
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.saveBGButton)
        buttonLayout.addWidget(self.restoreBGButton)
        mainLayout.addLayout(buttonLayout)

        # Number of Scans and Scan Time
        self.numScansLabel = QtWidgets.QLabel("No. Of Scans:")
        self.numScansSpin = QtWidgets.QSpinBox()
        self.numScansSpin.setValue(3)
        self.scanTimeLabel = QtWidgets.QLabel("Scan Time:")
        self.scanTimeSpin = QtWidgets.QSpinBox()
        self.scanTimeSpin.setValue(10)

        scanLayout = QtWidgets.QFormLayout()
        scanLayout.addRow(self.numScansLabel, self.numScansSpin)
        scanLayout.addRow(self.scanTimeLabel, self.scanTimeSpin)
        mainLayout.addLayout(scanLayout)

        # BG and Scan Buttons
        self.bgButton = QtWidgets.QPushButton("BG")
        self.scanButton = QtWidgets.QPushButton("SCAN")
        mainLayout.addWidget(self.bgButton)
        mainLayout.addWidget(self.scanButton)

        # Number of Scanned Samples
        self.scannedSamplesLabel = QtWidgets.QLabel("Number of Scanned Samples: 0")
        mainLayout.addWidget(self.scannedSamplesLabel)

        # Save As JSON and CSV
        self.saveAsLabel = QtWidgets.QLabel("Save As:")
        self.jsonLineEdit = QtWidgets.QLineEdit("scantest28")
        self.jsonLabel = QtWidgets.QLabel(".json")
        self.csvLineEdit = QtWidgets.QLineEdit("scantest28")
        self.csvLabel = QtWidgets.QLabel(".csv")

        saveAsLayout = QtWidgets.QFormLayout()
        saveAsLayout.addRow(self.saveAsLabel, self.jsonLineEdit)
        saveAsLayout.addRow("", self.jsonLabel)
        saveAsLayout.addRow("", self.csvLineEdit)
        saveAsLayout.addRow("", self.csvLabel)
        mainLayout.addLayout(saveAsLayout)

        # Directory Selection
        self.toLabel = QtWidgets.QLabel("To:")
        self.directoryLineEdit = QtWidgets.QLineEdit("C:/Users/fbetanco/Desktop/Files")
        self.browseButton = QtWidgets.QPushButton("...")

        directoryLayout = QtWidgets.QHBoxLayout()
        directoryLayout.addWidget(self.toLabel)
        directoryLayout.addWidget(self.directoryLineEdit)
        directoryLayout.addWidget(self.browseButton)
        mainLayout.addLayout(directoryLayout)

        # Clear and Save Buttons
        self.clearButton = QtWidgets.QPushButton("Clear")
        self.saveButton = QtWidgets.QPushButton("Save")
        actionLayout = QtWidgets.QHBoxLayout()
        actionLayout.addWidget(self.clearButton)
        actionLayout.addWidget(self.saveButton)
        mainLayout.addLayout(actionLayout)

        # Navigation Buttons
        self.homeButton = QtWidgets.QPushButton("Home")
        self.settingsButton = QtWidgets.QPushButton("Settings")
        navLayout = QtWidgets.QHBoxLayout()
        navLayout.addWidget(self.homeButton)
        navLayout.addWidget(self.settingsButton)
        mainLayout.addLayout(navLayout)

        # Connect Navigation Buttons
        self.homeButton.clicked.connect(self.openHomeView)
        self.settingsButton.clicked.connect(self.openSettingsView)

    def openHomeView(self):
        from views.home_view import HomeView

        if self.parent:
            self.parent.setCentralWidget(HomeView(self.parent))

    def openSettingsView(self):
        from views.settings_view import SettingsView

        if self.parent:
            self.parent.setCentralWidget(SettingsView(self.parent))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SpectrumView()
    window.show()
    sys.exit(app.exec())
