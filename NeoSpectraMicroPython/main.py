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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
