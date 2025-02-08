from PyQt6 import QtCore, QtWidgets, QtGui
import asyncio
import qasync
import traceback  # For better error reporting
from bluetooth_manager import BluetoothManager


class DeviceSelectionDialog(QtWidgets.QDialog):
    def __init__(self, devices, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select BLE Device")
        self.resize(300, 400)

        layout = QtWidgets.QVBoxLayout(self)

        self.device_list = QtWidgets.QListWidget()
        for device in devices:
            if device.name:
                self.device_list.addItem(f"{device.name} ({device.address})")

        self.connect_button = QtWidgets.QPushButton("Connect")
        self.connect_button.clicked.connect(self.handle_connect)

        layout.addWidget(QtWidgets.QLabel("Available Devices:"))
        layout.addWidget(self.device_list)
        layout.addWidget(self.connect_button)

        self.selected_device = None

    def handle_connect(self):
        selected_index = self.device_list.currentRow()
        if selected_index >= 0:
            self.selected_device = self.device_list.item(selected_index).text()
            print(f"[DEBUG] Selected device: {self.selected_device}")
            self.accept()

    def get_selected_device(self):
        return self.selected_device


class HomeView(QtWidgets.QWidget):
    def __init__(self, ble_manager, parent=None):
        super(HomeView, self).__init__(parent)
        print("[DEBUG] HomeView instance initialized")

        self._settings = QtCore.QSettings(
            "settings.ini", QtCore.QSettings.Format.IniFormat
        )

        self.ble_manager = ble_manager
        self.ble_manager.connection_changed.connect(self.update_connection_status)
        self.parent = parent
        self.setupUi()

        status = "Connected" if self.ble_manager.is_connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

        # Change button text based on connection status
        if self.ble_manager.is_connected:
            self.pbHomeConnect.setText("Disconnect")
        else:
            self.pbHomeConnect.setText("Connect")

    def setupUi(self):
        print("[DEBUG] Initializing HomeView UI")
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(382, 780)

        self.setStyleSheet(
            """
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
        """
        )

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(10)

        assets_dir = self._settings.value("AppSettings/AssetsDir", "./assets/")

        self.logoLabel = QtWidgets.QLabel()
        self.logoLabel.setPixmap(QtGui.QPixmap(f"{assets_dir}mainlogo@3x.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.logoLabel)

        self.infoLabel = QtWidgets.QLabel(
            "Interface with NeoSpectra Micro\nDevelopment Kits using your PC"
        )
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 8px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.infoLabel)

        self.connectionStatusLabel = QtWidgets.QLabel("Please Connect to a Kit")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.connectionStatusLabel.setStyleSheet(
            "color: white; background-color: rgba(0, 0, 0, 0.6); padding: 5px; border-radius: 8px;"
        )
        mainLayout.addWidget(self.connectionStatusLabel)

        buttonLayout = QtWidgets.QHBoxLayout()
        self.pbHomeConnect = QtWidgets.QPushButton("Connect")
        self.pbHomeConnect.clicked.connect(self.handle_connect_button)
        self.pbHomeSettings = QtWidgets.QPushButton("Settings")
        self.pbHomeSettings.clicked.connect(self.openSettingsView)

        buttonLayout.addWidget(self.pbHomeConnect)
        buttonLayout.addWidget(self.pbHomeSettings)
        mainLayout.addLayout(buttonLayout)

        navigationLayout = QtWidgets.QHBoxLayout()
        self.tbMainHome = QtWidgets.QPushButton("Home")
        self.tbMainSpectrum = QtWidgets.QPushButton("Spectrum")

        self.tbMainHome.clicked.connect(self.openHomeView)
        self.tbMainSpectrum.clicked.connect(self.openSpectrumView)

        navigationLayout.addWidget(self.tbMainHome)
        navigationLayout.addWidget(self.tbMainSpectrum)

        mainLayout.addLayout(navigationLayout)

    def update_connection_status(self, connected):
        status = "Connected" if connected else "Disconnected"
        self.connectionStatusLabel.setText(f"BLE Status: {status}")
        print(f"[DEBUG] BLE Status Updated: {status}")

        # Change button text based on connection status
        if connected:
            self.pbHomeConnect.setText("Disconnect")
        else:
            self.pbHomeConnect.setText("Connect")

    def handle_connect_button(self):
        asyncio.ensure_future(self.manage_connection())

    async def manage_connection(self):
        if (
            not self.ble_manager.ble_client
            or not self.ble_manager.ble_client.is_connected
        ):
            devices = await self.ble_manager.scan_devices()
            if devices:
                dialog = DeviceSelectionDialog(devices, self)
                if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                    selected_device = dialog.get_selected_device()
                    if selected_device:
                        address = selected_device.split("(")[-1].strip(")")
                        await self.ble_manager.connect_device(address)
        else:
            await self.ble_manager.disconnect_device()

    def openSettingsView(self):
        print("[DEBUG] openSettingsView method called")
        from views.settings_view import SettingsView

        if self.parent:
            self.parent.setCentralWidget(SettingsView(self.ble_manager, self.parent))

    def openHomeView(self):
        print("[DEBUG] openHomeView method called")
        # if self.parent:
        # Instead of creating a new instance, reuse the current one
        # self.parent.setCentralWidget(self)

    def openSpectrumView(self):
        print("[DEBUG] openSpectrumView method called")
        from views.spectrum_view import SpectrumView

        if self.parent:
            self.parent.setCentralWidget(SpectrumView(self.ble_manager, self.parent))


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        loop = qasync.QEventLoop(app)
        asyncio.set_event_loop(loop)

        ble_manager = BluetoothManager()
        window = HomeView(ble_manager)
        window.show()

        loop.run_forever()
    except Exception as e:
        print(f"[CRITICAL ERROR] {e}")
        print(traceback.format_exc())
