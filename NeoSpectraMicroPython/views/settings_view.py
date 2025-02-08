from PyQt6 import QtCore, QtWidgets, QtGui


class SettingsView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SettingsView, self).__init__(parent)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Settings")
        self.resize(780, 780)

        # Main Layout
        mainLayout = QtWidgets.QVBoxLayout(self)

        # Title
        self.settingsTitle = QtWidgets.QLabel("Settings", self)
        self.settingsTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.settingsTitle.setStyleSheet("font-size: 24px; font-weight: bold; margin: 10px;")
        mainLayout.addWidget(self.settingsTitle)

        # Grid Layout for Settings
        gridLayout = QtWidgets.QGridLayout()

        # Source Settings
        sourceSettingsGroup = QtWidgets.QGroupBox("SOURCE SETTINGS")
        sourceLayout = QtWidgets.QGridLayout()

        sourceParams = [
            ("T1", ""),
            ("T2_MAX", ""),
            ("T2_C1", ""),
            ("T2_C2", ""),
            ("Delta T", ""),
            ("Lamp Select", "Select the active lamp."),
            ("Lamps Count", "Number of lamps available."),
            ("Resolution", "Defines the wavelength resolution.")
        ]

        for i, (param, description) in enumerate(sourceParams):
            label = QtWidgets.QLabel(param)
            if param in ["Resolution"]:
                comboBox = QtWidgets.QComboBox()
                comboBox.addItems(["16 nm @ 1500 nm", "32 nm @ 1500 nm"])
                sourceLayout.addWidget(label, i, 0)
                sourceLayout.addWidget(comboBox, i, 1)
            else:
                spinBox = QtWidgets.QSpinBox()
                spinBox.setRange(0, 100)
                sourceLayout.addWidget(label, i, 0)
                sourceLayout.addWidget(spinBox, i, 1)
            if description:
                descLabel = QtWidgets.QLabel(description)
                descLabel.setStyleSheet("font-size: 10px; color: gray;")
                sourceLayout.addWidget(descLabel, i, 2)

        sourceSettingsGroup.setLayout(sourceLayout)
        gridLayout.addWidget(sourceSettingsGroup, 0, 0)

        # Measurement Parameters
        measurementParamsGroup = QtWidgets.QGroupBox("MEASUREMENT PARAMETERS")
        measurementLayout = QtWidgets.QGridLayout()

        measurementParams = [
            ("Run Mode", "Select continuous or single run mode."),
            ("Optical Gain Settings", "Adjust gain settings for optimal measurement.")
        ]

        for i, (param, description) in enumerate(measurementParams):
            label = QtWidgets.QLabel(param)
            comboBox = QtWidgets.QComboBox()
            if param == "Run Mode":
                comboBox.addItems(["Continuous", "Single"])
            else:
                comboBox.addItems(["Default", "High Gain", "Low Gain"])
            measurementLayout.addWidget(label, i, 0)
            measurementLayout.addWidget(comboBox, i, 1)

            descLabel = QtWidgets.QLabel(description)
            descLabel.setStyleSheet("font-size: 10px; color: gray;")
            measurementLayout.addWidget(descLabel, i, 2)

        measurementParamsGroup.setLayout(measurementLayout)
        gridLayout.addWidget(measurementParamsGroup, 1, 0)

        # Display Data
        displayDataGroup = QtWidgets.QGroupBox("DISPLAY DATA")
        displayLayout = QtWidgets.QGridLayout()

        displayParams = [
            ("Enable Linear Interpolation", "Ensures consistent wavelength vectors."),
            ("Number of Data Points", "Defines the number of data points to display."),
            ("Enable FFT Settings", "Enables settings for Fourier Transform processing."),
            ("Apodization Function", "Selects the function for spectral smoothing."),
            ("Number of FFT Points", "Determines the resolution of the FFT.")
        ]

        for i, (param, description) in enumerate(displayParams):
            label = QtWidgets.QLabel(param)
            if param in ["Apodization Function"]:
                comboBox = QtWidgets.QComboBox()
                comboBox.addItems(["Boxcar", "Hanning", "Hamming", "Blackman", "Gaussian"])
            elif param in ["Number of FFT Points"]:
                comboBox = QtWidgets.QComboBox()
                comboBox.addItems(["4 K", "8 K", "16 K"])
            else:
                comboBox = QtWidgets.QComboBox()
                comboBox.addItems(["Enabled", "Disabled"])
            displayLayout.addWidget(label, i, 0)
            displayLayout.addWidget(comboBox, i, 1)

            descLabel = QtWidgets.QLabel(description)
            descLabel.setStyleSheet("font-size: 10px; color: gray;")
            displayLayout.addWidget(descLabel, i, 2)

        displayDataGroup.setLayout(displayLayout)
        gridLayout.addWidget(displayDataGroup, 0, 1)

        mainLayout.addLayout(gridLayout)

        # Restore Defaults Button
        self.restoreButton = QtWidgets.QPushButton("Restore Defaults", self)
        self.restoreButton.setStyleSheet("background-color: orange; padding: 10px;")
        mainLayout.addWidget(self.restoreButton)

        # Navigation Buttons
        navLayout = QtWidgets.QHBoxLayout()
        self.homeButton = QtWidgets.QPushButton("Home")
        self.spectrumButton = QtWidgets.QPushButton("Spectrum")

        homeIcon = QtGui.QIcon("./assets/home_icon.png")
        spectrumIcon = QtGui.QIcon("./assets/spectrum_icon.png")

        self.homeButton.setIcon(homeIcon)
        self.spectrumButton.setIcon(spectrumIcon)

        navLayout.addWidget(self.homeButton)
        navLayout.addWidget(self.spectrumButton)

        mainLayout.addLayout(navLayout)

        # Connect Home button to go back to HomeView
        self.homeButton.clicked.connect(self.goToHomeView)
        self.spectrumButton.clicked.connect(self.goToSpectrumView)

    def goToHomeView(self):
        from views.home_view import HomeView

        if self.parent:
            self.parent.setCentralWidget(HomeView(self.parent))

    def goToSpectrumView(self):
        from views.spectrum_view import SpectrumView

        if self.parent:
            self.parent.setCentralWidget(SpectrumView(self.parent))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SettingsView()
    window.show()
    sys.exit(app.exec())
