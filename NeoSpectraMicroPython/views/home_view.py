from PyQt6 import QtCore, QtWidgets, QtGui


class HomeView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        self._settings = QtCore.QSettings(
            "settings.ini", QtCore.QSettings.Format.IniFormat
        )
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(382, 780)

        # Apply main stylesheet
        self.setStyleSheet(
            """
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
        """
        )

        # Main Layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        # Home Frame
        self.frmHome = QtWidgets.QFrame(self)
        self.frmHome.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        assets_dir = self._settings.value("AppSettings/AssetsDir", "./assets/")
        self.frmHome.setStyleSheet(
            f'background-image: url("{assets_dir}background_image.png");'
            "background-position: center; background-repeat: no-repeat; background-size: cover;"
        )
        mainLayout.addWidget(self.frmHome)

        # Layout inside Home Frame
        homeLayout = QtWidgets.QVBoxLayout(self.frmHome)
        homeLayout.setContentsMargins(10, 10, 10, 10)
        homeLayout.setSpacing(15)

        # Logo
        self.logoLabel = QtWidgets.QLabel(self.frmHome)
        self.logoLabel.setStyleSheet(
            f'border-image: url("{assets_dir}mainlogo@3x.png");'
        )
        self.logoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        homeLayout.addWidget(self.logoLabel)

        # Info Label
        self.infoLabel = QtWidgets.QLabel(self.frmHome)
        self.infoLabel.setText(
            "Interface with NeoSpectra Micro\nDevelopment Kits using your PC"
        )
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 8px; border-radius: 8px;"
        )
        homeLayout.addWidget(self.infoLabel)

        # Connection Status Label
        self.connectionStatusLabel = QtWidgets.QLabel(self.frmHome)
        self.connectionStatusLabel.setText("Please Connect to a Kit")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.connectionStatusLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 5px; border-radius: 8px;"
        )
        homeLayout.addWidget(self.connectionStatusLabel)

        # Buttons Layout
        buttonLayout = QtWidgets.QHBoxLayout()
        self.pbHomeConnect = QtWidgets.QPushButton("Connect", self.frmHome)
        self.pbHomeSettings = QtWidgets.QPushButton("Settings", self.frmHome)
        buttonLayout.addWidget(self.pbHomeConnect)
        buttonLayout.addWidget(self.pbHomeSettings)
        homeLayout.addLayout(buttonLayout)

        # Navigation Buttons
        navigationLayout = QtWidgets.QHBoxLayout()
        self.tbMainHome = QtWidgets.QPushButton("Home", self)
        self.tbMainHome.setIcon(QtGui.QIcon(f"{assets_dir}home_icon.png"))
        self.tbMainSpectrum = QtWidgets.QPushButton("Spectrum", self)
        self.tbMainSpectrum.setIcon(QtGui.QIcon(f"{assets_dir}spectrum_icon.png"))

        navigationLayout.addWidget(self.tbMainHome)
        navigationLayout.addWidget(self.tbMainSpectrum)

        mainLayout.addLayout(navigationLayout)

        # Connect Settings button to open Settings View
        self.pbHomeSettings.clicked.connect(self.openSettingsView)
        self.tbMainSpectrum.clicked.connect(self.openSpectrumView)

    def openSettingsView(self):
        from views.settings_view import SettingsView

        if self.parent:
            self.parent.setCentralWidget(SettingsView(self.parent))

    def openSpectrumView(self):
        from views.spectrum_view import SpectrumView

        if self.parent:
            self.parent.setCentralWidget(SpectrumView(self.parent))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = HomeView()
    window.show()
    sys.exit(app.exec())
