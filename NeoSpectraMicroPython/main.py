import sys
import os
import icecream

from decimal import *

import shutil
import time
from time import sleep

import datetime
import random

from pathlib import Path

from PyQt6 import QtCore, QtWidgets

from PyQt6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QBoxLayout,
    QDialog,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QWidget,
)

from PyQt6.QtGui import QIcon, QMovie, QPainter, QPixmap
from PyQt6.QtCore import QDir, QSettings, QSize, QTimer, Qt
import json

import qasync
import asyncio

from dataclasses import dataclass
from functools import cached_property

from QBleak import QBleakClient

from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice

from Ui_MainWindow import Ui_MainWindow

import os


class MainWindowApp(Ui_MainWindow):
    _device_name = None
    # _device_name = "NeoSpectraMicro_210213"
    # _device_address = "35CF177A-98E1-42B1-8D09-73947DBACEB2"

    _client = None

    _device_curr = None
    _ble_is_connected = False

    _movie = None

    list = []
    timeS = None
    timeA = None

    _start_time = None
    _end_time = None

    _bg_was_performed = False
    _scan_was_performed = False
    _scan_continuously = False

    _flag_run_scan = False
    _scan_sample_counter = 0

    def __init__(self):
        super().__init__()

        self.setEnabled(True)
        self.resize(1506, 748)

        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##########################################################################################################
        self.pbHomeSettings.clicked.connect(self.on_pbHomeSettings_clicked)
        self.pbHomeConnect.clicked.connect(self.on_pbHomeConnect_clicked)
        self.tbMainHome.clicked.connect(self.on_tbMainHome_clicked)
        self.tbMainSpectrum.clicked.connect(self.on_tbMainSpectrum_clicked)
        self.pbSettingsRestore.clicked.connect(self.on_pbSettingsRestore_clicked)
        self.tbSpectrumFindDir.clicked.connect(self.on_tbSpectrumFindDir_clicked)
        self.tbSpectrumBG.clicked.connect(self.on_tbSpectrumBG_clicked)
        self.tbSpectrumScan.clicked.connect(self.on_tbSpectrumScan_clicked)
        self.pbSpectrumClear.clicked.connect(self.on_pbSpectrumClear_clicked)
        self.pbSpectrumSave.clicked.connect(self.on_pbSpectrumSave_clicked)

        ##########################################################################################################
        self.sbSettingsT1.valueChanged.connect(self.on_settings_changed)
        self.sbSettingsT2_C1.valueChanged.connect(self.on_settings_changed)
        self.sbSettingsT2_C2.valueChanged.connect(self.on_settings_changed)
        self.sbSettingsT2_MAX.valueChanged.connect(self.on_settings_changed)
        self.sbSettingsDeltaT.valueChanged.connect(self.on_settings_changed)

        self.cbSettingsLampSelect.currentIndexChanged.connect(self.on_settings_changed)
        self.cbSettingsLampCount.currentIndexChanged.connect(self.on_settings_changed)
        self.cbSettingsResolution.currentIndexChanged.connect(self.on_settings_changed)

        self.cbSettingsRunMode.currentIndexChanged.connect(self.on_settings_changed)
        self.cbSettingsOpticalGainSettings.currentIndexChanged.connect(
            self.on_settings_changed
        )

        self.cbSettingsEnableLinearInterpolation.currentIndexChanged.connect(
            self.on_settings_changed
        )
        self.cbSettingsNumberDataPoints.currentIndexChanged.connect(
            self.on_settings_changed
        )
        self.cbSettingsEnableFFTSettings.currentIndexChanged.connect(
            self.on_settings_changed
        )

        self.cbSettingsApodizationFunction.currentIndexChanged.connect(
            self.on_settings_changed
        )
        self.cbSettingsNumberFFTPoints.currentIndexChanged.connect(
            self.on_settings_changed
        )
        ##########################################################################################################

        # self.sbSpectrumScanTime.valueChanged.connect(self.on_homesettings_changed)
        # self.txtSpectrumJsonFileName.textChanged.connect(self.on_homesettings_changed)
        # self.txtSpectrumCsvFileName.textChanged.connect(self.on_homesettings_changed)
        # self.txtSpectrumPathFileDir.textChanged.connect(self.on_homesettings_changed)

        ##########################################################################################################

        # We ask to connect to the BLE device
        self.pbHomeConnect.setText("Connect")
        self.pbHomeSettings.setEnabled(False)

        # We initiate in the home panel
        self.frmHome.move(10, 10)
        self.resize(380, 748)
        self.frmHome.setVisible(True)
        self.frmSpectrum.setVisible(False)
        self.frmSettings.setVisible(False)

        self.UpdateGUIFromBLEStatus(runAsync=0)

    def showEvent(self, event):
        self.sbSpectrumScanTime.setValue(1)
        self.txtSpectrumPathFileDir.setText(
            self._settings.value("ScanSettings/WorkDir")
        )

        self.tbMainSpectrum.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "spectral@3x.png")
        )
        self.tbMainHome.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "selected_home@3x.png"
            )
        )

        self.tbSpectrumBG.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "bg_btn_round_3@3x.png"
            )
        )
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png")
        )
        self.tbSpectrumScan.setEnabled(False)

        """
        self.timeB = QTimer(self)
        self.timeB.setInterval(250)
        self.timeB.timeout.connect(self.readInputButton)
        self.timeB.start()
        """

        # self.setDefaultMainHomeSettings()
        self.loadMainHomeSettings()

        self.sbSpectrumScanTime.textChanged.connect(self.on_homesettings_changed)
        self.sbSpectrumNoScans.textChanged.connect(self.on_homesettings_changed)
        self.txtSpectrumJsonFileName.textChanged.connect(self.on_homesettings_changed)
        self.txtSpectrumCsvFileName.textChanged.connect(self.on_homesettings_changed)
        self.txtSpectrumPathFileDir.textChanged.connect(self.on_homesettings_changed)

        if self._settings.value("AppSettings/button_enabled") == "1":
            print("button enabled flag = True")
            try:
                os.environ["BLINKA_MCP2221"] = "1"
                import board
                import digitalio

                self.timeB = QTimer(self)
                self.timeB.setInterval(2000)
                self.timeB.timeout.connect(self.readInputButton)
                self.timeB.start()

                self.button = digitalio.DigitalInOut(board.G0)
                self.button.direction = digitalio.Direction.INPUT
            except:
                print("button failed to enable")
        else:
            print("button enabled flag = False")

    def closeEvent(self, event):
        sys.exit(0)

    @qasync.asyncSlot()
    async def readInputButton(self):
        if self.button.value == True:
            if (
                self._bg_was_performed == True
                and self._ble_is_connected == True
                and (self._scan_sample_counter == 0)
            ):
                print("HIGH LEVEL")
                while self.button.value == True:
                    await asyncio.sleep(0.250)
                await self.doButtonScanLogic()
        else:
            if (
                self._bg_was_performed == True
                and self._ble_is_connected == True
                and (self._scan_sample_counter == 0)
            ):
                print("LOW LEVEL")

    def on_settings_changed(self):
        self.saveDeviceSettings()

    def on_homesettings_changed(self):
        self.saveMainHomeSettings()

    @qasync.asyncSlot()
    async def on_pbHomeSettings_clicked(self):
        self.loadDeviceSettings()
        self.loadMainHomeSettings()

        self.frmSettings.move(10, 10)
        self.resize(720, 748)
        self.frmHome.setVisible(False)
        self.frmSpectrum.setVisible(False)
        self.frmSettings.setVisible(True)

    def startSpinner(self):
        self.lblHomeSpinner.hide()
        self._movie = QMovie(
            self._settings.value("AppSettings/assets_dir") + "loader.gif"
        )
        self._movie.setScaledSize(self.lblHomeSpinner.size())
        self.lblHomeSpinner.setMovie(self._movie)
        self._movie.start()
        self.lblHomeSpinner.show()

    def stopSpinner(self):
        if self._movie != None:
            self._movie.stop()
            self.lblHomeSpinner.hide()

    @qasync.asyncSlot()
    async def on_pbHomeConnect_clicked(self):
        self.startSpinner()
        """
        await asyncio.sleep(0.1)
        
        if not self._ble_is_connected:
            self._ble_is_connected = True
        else:
            self._ble_is_connected = False
        """
        """
        if not self._ble_is_connected:
            if self._device_name == None:
                await self.handle_scan()
            try:
                await self.handle_connect()
            except:
                print("failed to connect")
        else:
            await self.handle_disconnect()
        """
        await self.handle_scan()
        if self._device_name != None:
            await self.handle_connect()
        await self.UpdateGUIFromBLEStatus()
        self.stopSpinner()

    @qasync.asyncSlot()
    async def on_tbMainHome_clicked(self):
        self.frmHome.move(10, 10)
        self.resize(380, 748)
        self.frmHome.setVisible(True)
        self.frmSpectrum.setVisible(False)
        self.frmSettings.setVisible(False)

        self.tbMainSpectrum.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "spectral@3x.png")
        )
        self.tbMainHome.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "selected_home@3x.png"
            )
        )

        self.loadMainHomeSettings()

        self.UpdateGUIFromBLEStatus()

    @qasync.asyncSlot()
    async def on_tbMainSpectrum_clicked(self):
        if self._ble_is_connected == False:
            subDialog = QDialog()
            subDialog.setWindowTitle("Sub Dialog")
            subDialog.exec()
        else:
            self.frmSpectrum.move(10, 10)
            self.resize(380, 748)
            self.frmHome.setVisible(False)
            self.frmSpectrum.setVisible(True)
            self.frmSettings.setVisible(False)

            self.tbMainSpectrum.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir")
                    + "selected_spectral@3x.png"
                )
            )
            self.tbMainHome.setIcon(
                QIcon(self._settings.value("AppSettings/assets_dir") + "home@3x.png")
            )

            self.loadMainHomeSettings()

    @qasync.asyncSlot()
    async def on_pbSettingsRestore_clicked(self):
        """
        self.saveDeviceSettings()
        self.frmHome.move(10, 10)
        self.resize(380, 748)
        self.frmHome.setVisible(True)
        self.frmSpectrum.setVisible(False)
        self.frmSettings.setVisible(False)
        """
        self.setDefaultSettings()
        self.loadDeviceSettings()

    @qasync.asyncSlot()
    async def on_tbSpectrumFindDir_clicked(self):
        dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Open Directory",
            directory="/home",
            options=QFileDialog.Option.ShowDirsOnly,
        )
        if dir != "":
            self.txtSpectrumPathFileDir.setText(dir)

    @qasync.asyncSlot()
    async def backgroundAnimation(self):
        self.tbSpectrumBG.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "bg_btn_round_2@3x.png"
            )
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumBG.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "bg_btn_round_1@3x.png"
            )
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumBG.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "bg_btn_round_2@3x.png"
            )
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumBG.setIcon(
            QIcon(
                self._settings.value("AppSettings/assets_dir") + "bg_btn_round_3@3x.png"
            )
        )
        await asyncio.sleep(0.25)

    @qasync.asyncSlot()
    async def scanAnimation(self):
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "stop_bt2@3x.png")
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "stop_bt1@3x.png")
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "stop_bt2@3x.png")
        )
        await asyncio.sleep(0.25)
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "stop_bt3@3x.png")
        )
        await asyncio.sleep(0.25)

    @qasync.asyncSlot()
    async def on_tbSpectrumBG_clicked(self):
        if self._scan_continuously == True:
            await asyncio.sleep(0.1)
            return

        self._bg_was_performed = False
        self._scan_sample_counter = 0
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png")
        )
        self.lblSpectrumInfoNumberOfScannedSamples.setText(
            "Number of Scanned Samples: " + str(self._scan_sample_counter)
        )
        self._scan_was_performed = False
        self.tbSpectrumScan.setEnabled(False)

        self.timeA = QTimer(self)
        self.timeA.setInterval(1000)
        self.timeA.timeout.connect(self.backgroundAnimation)
        self.timeA.start()

        await self.handle_runBackground()

        self.timeA.stop()
        await asyncio.sleep(1)
        self._bg_was_performed = True
        self.tbSpectrumScan.setIcon(
            QIcon(self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png")
        )
        self.tbSpectrumScan.setEnabled(True)

    @qasync.asyncSlot()
    async def doButtonScanLogic(self):
        if self._flag_run_scan == False:

            self._scan_sample_counter = 0

            self._scan_continuously = True
            self._flag_run_scan = True

            self.list = []
            self.tlist = []

            self.lblSpectrumInfoNumberOfScannedSamples.setText(
                "Number of Scanned Samples: " + str(self._scan_sample_counter)
            )

            self.timeA = QTimer(self)
            self.timeA.setInterval(1000)
            self.timeA.timeout.connect(self.scanAnimation)
            self.timeA.start()

            #######################################################
            # self.timeS = QTimer(self)
            # self.timeS.setInterval(10000 )
            # self.timeS.timeout.connect(self.ScanContinuously)
            # self.timeS.start()

            nScan = 0
            while (
                self.sbSpectrumNoScans.value() > nScan
            ) and self._scan_continuously == True:
                await self.ScanContinuously()
                await asyncio.sleep(1)
                nScan = nScan + 1

            e = datetime.datetime.now()
            self._start_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            # print(self._start_time)
            #######################################################

        else:
            self._scan_continuously = False
            self._flag_run_scan = False
            self._scan_was_performed = True

            if self.timeS != None:
                self.timeS.stop()

            e = datetime.datetime.now()
            self._end_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            # print(self._end_time)

            if self.timeA != None:
                self.timeA.stop()

            await asyncio.sleep(1)

            self.tbSpectrumScan.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png"
                )
            )
            # self._scan_sample_counter = 0
            self.tbSpectrumScan.setEnabled(True)

    @qasync.asyncSlot()
    async def on_tbSpectrumScan_clicked(self):
        await self.doButtonScanLogic()

    @qasync.asyncSlot()
    async def on_pbSpectrumSave_clicked(self):
        if self._scan_continuously == False:

            """if (
                self.current_client != None
                and self._start_time != None
                and self._end_time != None
            ):
                return
            """

            # Create dictionary object which is json representation
            json_data = {
                "Selected_Device_Name": self._device_name,
                "BAC_Current_Scan": [],
                "scans": {
                    "scan0": {
                        "samples": self.list,
                    },
                    "start_time": self._start_time,
                    "end_time": self._end_time,
                    "Sample_TimeStamps": [self.tlist],
                },
            }

            # Writing JSON data to a file using a file object
            with open(
                self._settings.value("AppSettings/temp_dir") + "temp.json", "w"
            ) as outfile:
                # json_data refers to the above JSON
                json.dump(json_data, outfile)

            ########################################################################
            if self.txtSpectrumPathFileDir != "":
                if self.txtSpectrumCsvFileName != "":
                    shutil.copyfile(
                        self._settings.value("AppSettings/temp_dir") + "temp.csv",
                        self.txtSpectrumPathFileDir.text()
                        + "/"
                        + self.txtSpectrumCsvFileName.text()
                        + ".csv",
                    )

                if self.txtSpectrumJsonFileName != "":
                    shutil.copyfile(
                        self._settings.value("AppSettings/temp_dir") + "temp.json",
                        self.txtSpectrumPathFileDir.text()
                        + "/"
                        + self.txtSpectrumJsonFileName.text()
                        + ".json",
                    )

                    await asyncio.sleep(0.1)

    @qasync.asyncSlot()
    async def on_pbSpectrumClear_clicked(self):
        if self._scan_continuously == False:

            self._bg_was_performed = False
            self._scan_sample_counter = 0
            self.tbSpectrumScan.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png"
                )
            )
            self.lblSpectrumInfoNumberOfScannedSamples.setText(
                "Number of Scanned Samples: " + str(self._scan_sample_counter)
            )
            self.tbSpectrumScan.setEnabled(False)
        await asyncio.sleep(0.1)

    @qasync.asyncSlot()
    async def UpdateGUIFromBLEStatus(self, runAsync=1):
        if self._ble_is_connected == False:
            # We ask to connect to the BLE device
            self.pbHomeConnect.setText("Connect")
            self.pbHomeSettings.setEnabled(False)
            # self.tbMainSpectrum.setEnabled(False)
            self.lblHomeInfo1.setText(
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Interface with NeoSpectra Micro </span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Development Kits using your </span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">PC</span></p></body></html>'
            )
            self.lblHomeInfo2.setText(
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Please Connected to a Kit</span></p></body></html>'
            )
            self.tbMainSpectrum.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir") + "spectral@3x.png"
                )
            )
            # self.tbMainHome.setIcon(QIcon(self._settings.value("AppSettings/assets_dir")+ "selected_home@3x.png"))
        else:
            # We connect to the BLE device
            self.pbHomeConnect.setText("Disconnect")
            self.pbHomeSettings.setEnabled(True)
            # self.tbMainSpectrum.setEnabled(True)
            if self._device_name != None:
                dev_name = self._device_name.replace("NeoSpectraMicro_", "", 1)
            else:
                dev_name = ""
            self.lblHomeInfo1.setText(
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Interfaced with NeoSpectra '
                + dev_name
                + '</span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Development Kit using your </span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">PC</span></p></body></html>'
            )
            self.lblHomeInfo2.setText(
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Connecteded to '
                + dev_name
                + "</span></p></body></html>"
            )
            self.tbMainSpectrum.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir")
                    + "selected_spectral@3x.png"
                )
            )
        if runAsync == 1:
            await asyncio.sleep(0.1)

    @cached_property
    def devices(self):
        return list()

    @property
    def current_client(self):
        return self._client

    async def build_client(self, device):
        if self._client is not None:
            await self._client.stop()
        self._client = QBleakClient(device)
        self._client.messageChanged.connect(self.handle_message_changed)
        await self._client.start()

    def Countdown(self):
        if self.countdw > 0:
            self.countdw -= 1
        else:
            self.time.stop()
            if self._device_name != None and self._device_curr != None:
                print(
                    "Connect with NeoSpectra \n"
                    "Micro Development Kits \n"
                    "using BLE on your PC"
                )
            else:
                print("Device not found\nPlease try again")
            print("Stop Timer")
            self.countdw = 15

    @qasync.asyncSlot()
    async def handle_scan(self):
        self._device_name = None
        self._device_address = None

        self.countdw = 15

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Countdown)

        print("Scanning for BLE devices...")
        self.time.start()
        self.devices.clear()
        try:
            flag_found_device = False
            devices = await BleakScanner.discover()
            self.devices.extend(devices)
            for i, device in enumerate(self.devices):
                if device.name != None and "NeoSpectraMicro_" in device.name:
                    print(device.name)
                    print("Found device :  \n" "" + device.name)
                    self._device_name = device.name
                    self._device_address = device.address
                    print(device.address)
                    self._device_curr = device
                    flag_found_device = True
            self.time.stop()
            if flag_found_device == False:
                print("No device found")
        except:
            self.time.stop()
            print("No device found")

    @qasync.asyncSlot()
    async def handle_connect(self):
        if self._ble_is_connected == False:
            print("Try connecting...")
            device = self._device_curr

            if isinstance(device, BLEDevice):
                await self.build_client(device)
                print("connection stablished.")
                self._ble_is_connected = True

            elif self._device_name != None:
                await self.build_client(self._device_address)
                print("connection stablished.")
                self._ble_is_connected = True
        else:
            if self.current_client is None:
                self._ble_is_connected = False
                return
            try:
                await self._client.stop()
                self._ble_is_connected = False
            except:
                # print("Done!")
                self._ble_is_connected = False

    @qasync.asyncSlot()
    async def handle_disconnect(self):
        if self.current_client is None:
            return
        if self._ble_is_connected == True:
            print("try disconnect")
            await self._client.stop()
            self._ble_is_connected = False

    def handle_message_changed(self, message):
        print(f"msg: {message.decode()}")

    @qasync.asyncSlot()
    async def handle_runBackground(self):
        if self.current_client is None:
            return
        self._bg_was_performed = False
        self._scan_was_performed = False

        await self.setOpticalSettings()
        # await asyncio.sleep(2)

        await self.setSourceSettings()
        # await asyncio.sleep(2)

        await self.runBackground()
        # await asyncio.sleep(2)

        # print("waiting for data")
        # while not self._client.data_received:
        # await asyncio.sleep(0.5)
        # print("data is ready")
        await asyncio.sleep(1)

    """
    def handle_runAbsorbance(self):
        if self.current_client is None:
            return

        if self._flag_run_scan == False:
            self._scan_sample_counter = 0

            self.time = QTimer(self)
            self.time.setInterval(10000)
            self.time.timeout.connect(self.ScanContinuously)
            self.time.start()
            self._scan_continuously = True

            e = datetime.datetime.now()
            self._start_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            #print(self._start_time)

            self._flag_run_scan = True
        else:
            self._scan_continuously = False
            self._flag_run_scan = False
            if self.time != None:
                self.time.stop()
            e = datetime.datetime.now()
            self._end_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            #print(self._end_time)
            # self.btnScan.setText("Scan")
    """

    @qasync.asyncSlot()
    async def ScanContinuously(self):
        if self._scan_continuously == False:
            return
        # self.time.stop()

        print("Scan No." + str(self._scan_sample_counter))
        self._scan_sample_counter += 1

        await self.runAbsorbance()

        # print("waiting for data")
        while not self._client.data_ready:
            await asyncio.sleep(0.5)
        # print("data is ready")

        mylist = []
        for i in range(0, 513):
            # mylist.append(random.uniform(34534.107267099898,22662.445061374456))
            mylist.append(self._client.values_array[i])
        self.list.extend(["sample" + str(self._scan_sample_counter), mylist])

        e = datetime.datetime.now()
        s_current_time = "%s/%s/%s %s:%s:%s" % (
            str(e.day).zfill(2),
            str(e.month).zfill(2),
            e.year,
            str(e.hour).zfill(2),
            str(e.minute).zfill(2),
            str(e.second).zfill(2),
        )
        self.tlist.append(s_current_time)

        file = open(self._settings.value("AppSettings/temp_dir") + "temp.csv", "a")
        file.write(
            "sample" + str(self._scan_sample_counter) + ", " + s_current_time + ", "
        )
        for item in mylist:
            file.write(str(item) + ", ")
        file.write("\n")
        file.close()

        self.lblSpectrumInfoNumberOfScannedSamples.setText(
            "Number of Scanned Samples: " + str(self._scan_sample_counter)
        )
        if self._scan_sample_counter == int(
            self._settings.value("ScanSettings/NumberOfScans")
        ):
            print("Stop by Max N Samples")

            self._scan_continuously = False
            self._flag_run_scan = False
            self._scan_was_performed = True

            # if self.timeS != None:

            e = datetime.datetime.now()
            self._end_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            # print(self._end_time)

            if self.timeA != None:
                self.timeA.stop()

            await asyncio.sleep(1)

            self.tbSpectrumScan.setIcon(
                QIcon(
                    self._settings.value("AppSettings/assets_dir") + "scan_bt3@3x.png"
                )
            )
            self.tbSpectrumScan.setEnabled(True)
            self._scan_sample_counter = 0
            if self.timeS != None:
                self.timeS.stop()

        # await asyncio.sleep(1)

        # self.time.start()
        """
        if self._scan_sample_counter == 2:
            #print("MAX SCANS")
            self._scan_continuously = False
            self._flag_run_scan = False
            if self.timeS != None:
                self.timeS.stop()
            e = datetime.datetime.now()
            self._end_time = "%s/%s/%s %s:%s:%s" % (
                str(e.day).zfill(2),
                str(e.month).zfill(2),
                e.year,
                str(e.hour).zfill(2),
                str(e.minute).zfill(2),
                str(e.second).zfill(2),
            )
            """
        # print(self._end_time)

    ###########################################################################################
    ## SPECTROMETER METHODS
    ###########################################################################################
    @qasync.asyncSlot()
    async def runAbsorbance(self):
        print("[runAbsorbance]")
        # OperationID = 5 (runAbsorbance)
        # scanTime = 232 (232 ms)
        # commonWavNum = 3 (257 points)
        # opticalGain = 0 (use the optical gain settings saved on DVK)
        # apodizationSel = 3 (Lorenz)
        # zeroPadding = 0 (32k points)
        # Mode = 0 ()
        # 3 (ASCII End of Text)
        # 5 (ASCII Enquiry)

        # declaring an integer value
        integer_val = self.sbSpectrumScanTime.value() * 1000
        # converting int to bytes with length
        # of the array as 2 and byter order as big
        bytes_val = integer_val.to_bytes(3, "little")
        # printing integer in byte representation
        # print(bytes_val[1])

        message_bytes = [5, bytes_val[0], bytes_val[1], bytes_val[2], 3, 0, 0, 3, 5]
        dataTX = bytearray(message_bytes)

        message = dataTX
        if message:
            await self.current_client.write(message)

        # while not QBleakClient.data_received == True:
        # await asyncio.sleep(0.2)

        # await asyncio.sleep(1)

    @qasync.asyncSlot()
    async def setOpticalSettings(self):
        print("[setOpticalSettings]")
        # setOpticalSettings
        # Description: Description: Select the optical gain settings to be used during the scan.
        # operationID : 27
        # optical gain value : Two bytes
        message_bytes = [27, 0, 0]
        dataTX = bytearray(message_bytes)

        message = dataTX
        if message:
            await self.current_client.write(message)

        # while not QBleakClient.data_received == True:
        # await asyncio.sleep(0.2)
        await asyncio.sleep(0.5)

    @qasync.asyncSlot()
    async def setSourceSettings(self):
        print("[setSourceSettings]")
        # setSourceSettings
        # Description : Description: Set all light source configurations needed to turn on/off the light source.
        # OperationID : 22
        # Lamps Count : One byte
        # Lamp Select : One byte
        # Reserved : Two bytes
        # T1 : One Byte
        # Delta T : One byte
        # Reserved : Two bytes
        # T2_C1 : One byte
        # T2_C2 : One byte
        # T2 max : One byte
        # 0 (ASCII)
        message_bytes = [22, 2, 0, 0, 0, 14, 2, 0, 0, 5, 35, 10, 0]
        dataTX = bytearray(message_bytes)

        message = dataTX
        if message:
            await self.current_client.write(message)

        # while not QBleakClient.data_received == True:
        # await asyncio.sleep(0.2)
        await asyncio.sleep(0.5)

    @qasync.asyncSlot()
    async def runBackground(self):
        print("[runBackground]")
        # runBackground
        # Description: Request to perform a background reading.
        # OperationID : 4
        # scanTime : Required (232) Duration of the scan in milliseconds with a minimum of 10 ms and a maximum of 2^24 ms
        # commonWavNum : Required (3) Specify the number of points used for the wave number: 3: 257 points.
        # opticalGain : Required (0) 0: use the optical gain settings saved on the DVK.
        # apodizationSel : Required (3) Select one of the apodization windows: 3: Lorenz
        # zeroPadding : Required (0)
        # Mode : Required (0)
        # ASCII 3 : ETX
        # ASCII 5 : ENQ

        # declaring an integer value
        integer_val = self.sbSpectrumScanTime.value() * 1000
        # converting int to bytes with length
        # of the array as 2 and byter order as big
        bytes_val = integer_val.to_bytes(3, "little")
        # printing integer in byte representation
        # print(bytes_val[1])
        message_bytes = [4, bytes_val[0], bytes_val[1], bytes_val[2], 3, 0, 0, 3, 5]
        dataTX = bytearray(message_bytes)

        message = dataTX
        if message:
            await self.current_client.write(message)

        # while not QBleakClient.data_received == True:
        # await asyncio.sleep(.25)

    def setDefaultMainHomeSettings(self):
        if self._settings == None:
            return

        self._settings.setValue("ScanSettings/ScanTime", 1)

        self._settings.setValue("ScanSettings/NumberOfScans", 5)

        self._settings.setValue("ScanSettings/JsonFileName", "noname")

        self._settings.setValue("ScanSettings/CsvFileName", "noname")

        self._settings.setValue("ScanSettings/WorkDir", "/Work")

        self._settings.setValue("ScanSettings/TempDir", "/Temp")
        self._settings.sync()

    def loadMainHomeSettings(self):
        if self._settings == None:
            return
        self.sbSpectrumScanTime.setValue(
            int(self._settings.value("ScanSettings/ScanTime"))
        )

        self.sbSpectrumNoScans.setValue(
            int(self._settings.value("ScanSettings/NumberOfScans"))
        )

        self.txtSpectrumJsonFileName.setText(
            self._settings.value("ScanSettings/JsonFileName")
        )
        self.txtSpectrumCsvFileName.setText(
            self._settings.value("ScanSettings/CsvFileName")
        )
        self.txtSpectrumPathFileDir.setText(
            self._settings.value("ScanSettings/WorkDir")
        )
        """
        self.(
            self._settings.value("ScanSettings/TempDir")
        )
        """

    def saveMainHomeSettings(self):
        # print("save config")

        self._settings.setValue(
            "ScanSettings/ScanTime", self.sbSpectrumScanTime.value()
        )

        self._settings.setValue(
            "ScanSettings/NumberOfScans", self.sbSpectrumNoScans.value()
        )

        self._settings.setValue(
            "ScanSettings/JsonFileName", self.txtSpectrumJsonFileName.text()
        )

        self._settings.setValue(
            "ScanSettings/CsvFileName", self.txtSpectrumCsvFileName.text()
        )

        self._settings.setValue(
            "ScanSettings/WorkDir", self.txtSpectrumPathFileDir.text()
        )

        self._settings.setValue("ScanSettings/TempDir", "")
        self._settings.sync()

    def loadDeviceSettings(self):
        if self._settings == None:
            return

        self.sbSettingsT1.setValue(
            int(self._settings.value("DeviceSettings/SourceSettings/T1"))
        )
        self.sbSettingsT2_C1.setValue(
            int(self._settings.value("DeviceSettings/SourceSettings/T2_C1"))
        )
        self.sbSettingsT2_C2.setValue(
            int(self._settings.value("DeviceSettings/SourceSettings/T2_C2"))
        )
        self.sbSettingsT2_MAX.setValue(
            int(self._settings.value("DeviceSettings/SourceSettings/T2_MAX"))
        )
        self.sbSettingsDeltaT.setValue(
            int(self._settings.value("DeviceSettings/SourceSettings/DeltaT"))
        )
        self.cbSettingsLampSelect.setCurrentIndex(
            int(self._settings.value("DeviceSettings/SourceSettings/LampSelect"))
        )
        self.cbSettingsLampCount.setCurrentIndex(
            int(self._settings.value("DeviceSettings/SourceSettings/LampCount"))
        )
        self.cbSettingsResolution.setCurrentIndex(
            int(self._settings.value("DeviceSettings/SourceSettings/Resolution"))
        )

        self.cbSettingsRunMode.setCurrentIndex(
            int(self._settings.value("DeviceSettings/MeasurementParameters/RunMode"))
        )
        self.cbSettingsOpticalGainSettings.setCurrentIndex(
            int(
                self._settings.value(
                    "DeviceSettings/MeasurementParameters/OpticalGainSettings"
                )
            )
        )

        self.cbSettingsEnableLinearInterpolation.setCurrentIndex(
            int(
                self._settings.value(
                    "DeviceSettings/DisplayData/EnableLinearInterpolation"
                )
            )
        )
        self.cbSettingsNumberDataPoints.setCurrentIndex(
            int(self._settings.value("DeviceSettings/DisplayData/NumberOfDataPoints"))
        )
        self.cbSettingsEnableFFTSettings.setCurrentIndex(
            int(self._settings.value("DeviceSettings/DisplayData/EnableFFTSettings"))
        )

        self.cbSettingsApodizationFunction.setCurrentIndex(
            int(self._settings.value("DeviceSettings/FFTSettings/ApodizationFunction"))
        )
        self.cbSettingsNumberFFTPoints.setCurrentIndex(
            int(self._settings.value("DeviceSettings/FFTSettings/NumberOfFFTPoints"))
        )

    def saveDeviceSettings(self):
        if self._settings == None:
            return

        self._settings.setValue(
            "DeviceSettings/SourceSettings/T1", self.sbSettingsT1.value()
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/T2_C1", self.sbSettingsT2_C1.value()
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/T2_C2", self.sbSettingsT2_C2.value()
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/T2_MAX", self.sbSettingsT2_MAX.value()
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/DeltaT", self.sbSettingsDeltaT.value()
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/LampSelect",
            self.cbSettingsLampSelect.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/LampCount",
            self.cbSettingsLampCount.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/SourceSettings/Resolution",
            self.cbSettingsResolution.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/MeasurementParameters/RunMode",
            self.cbSettingsRunMode.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/MeasurementParameters/OpticalGainSettings",
            self.cbSettingsOpticalGainSettings.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/DisplayData/EnableLinearInterpolation",
            self.cbSettingsEnableLinearInterpolation.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/DisplayData/NumberOfDataPoints",
            self.cbSettingsNumberDataPoints.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/DisplayData/EnableFFTSettings",
            self.cbSettingsEnableFFTSettings.currentIndex(),
        )

        self._settings.setValue(
            "DeviceSettings/FFTSettings/ApodizationFunction",
            self.cbSettingsApodizationFunction.currentIndex(),
        )
        self._settings.setValue(
            "DeviceSettings/FFTSettings/NumberOfFFTPoints",
            self.cbSettingsNumberFFTPoints.currentIndex(),
        )
        self._settings.sync()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # app.setStyleSheet(Path('app.qss').read_text())

    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = MainWindowApp()
    w.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec())
