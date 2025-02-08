from PyQt6 import QtWidgets
import qasync
import sys
from bluetooth_manager import BluetoothManager
from views.home_view import HomeView

#from device_settings_class import DeviceSettings

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setWindowTitle("NeoSpectra Micro")
        self.resize(800, 600)

        # Initialize Bluetooth Manager
        self.ble_manager = BluetoothManager()

        # Load Home View with Bluetooth Manager
        self.home_view = HomeView(self.ble_manager, self)
        self.setCentralWidget(self.home_view)

        #self.settings = DeviceSettings()
        #print(self.settings.device_data["SourceSettings/T2_C2"])


if __name__ == "__main__":
    app = qasync.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    qasync.asyncio.set_event_loop(loop)

    main_app = MainApp()
    main_app.show()

    with loop:
        loop.run_forever()
