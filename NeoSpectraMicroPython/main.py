from PyQt6 import QtCore, QtWidgets, QtGui

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(800, 600)

        # Initialize QSettings
        self._settings = QtCore.QSettings(
            "settings.ini", QtCore.QSettings.Format.IniFormat
        )

        # Load Home View
        from views.home_view import HomeView  # Lazy import

        self.home_view = HomeView(self)
        self.setCentralWidget(self.home_view)

        # Connect navigation buttons
        self.home_view.pbHomeSettings.clicked.connect(self.openSettingsView)
        self.home_view.tbMainHome.clicked.connect(self.openHomeView)
        self.home_view.tbMainSpectrum.clicked.connect(self.openSpectrumView)

    def openHomeView(self):
        from views.home_view import HomeView  # Lazy import

        self.setCentralWidget(HomeView(self))

    def openSettingsView(self):
        from views.settings_view import SettingsView  # Lazy import

        self.setCentralWidget(SettingsView(self))

    def openSpectrumView(self):
        from views.spectrum_view import SpectrumView  # Lazy import

        self.setCentralWidget(SpectrumView(self))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
