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

import pathlib

class Ui_MainWindow(QMainWindow):
    _settings = None

    def __init__(self):
        QMainWindow.__init__(self)


        self._settings = QSettings(
            QDir().currentPath() + "/settings.ini", QSettings.Format.IniFormat)

        #self._settings = QSettings("settings.ini", QSettings.Format.IniFormat)

        #if not pathlib.Path("settings.ini").is_file():
        #self.setDefaultSettings()
        print(self._settings.value("ScanSettings/WorkDir"))

        self.setupUi(Ui_MainWindow)
        self.retranslateUi(Ui_MainWindow)

    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")

        self.frmHome = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmHome.setGeometry(QtCore.QRect(10, 10, 360, 611))
        self.frmHome.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmHome.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmHome.setObjectName("frmHome")
        self.lblHomeBackground = QtWidgets.QLabel(parent=self.frmHome)
        self.lblHomeBackground.setGeometry(QtCore.QRect(0, 0, 360, 611))
        self.lblHomeBackground.setStyleSheet(
            "\n"
            "\n"
            'border-image: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'home_background@3x.jpg");'
        )
        self.lblHomeBackground.setText("")
        self.lblHomeBackground.setObjectName("lblHomeBackground")
        self.lblHomeInfo1 = QtWidgets.QLabel(parent=self.frmHome)
        self.lblHomeInfo1.setGeometry(QtCore.QRect(30, 300, 301, 111))
        self.lblHomeInfo1.setStyleSheet(
            "QLabel {\n"
            "  background-color: #60000000;\n"
            "  color: #fff; /* color: #464d55; */\n"
            "  font-weight: 600;\n"
            "}\n"
            "QLabel#heading {\n"
            "  color: #0f1925;\n"
            "  font-size: "
            + self._settings.value("AppSettings/label_font_sizepx1")
            + ";\n"
            "  margin-bottom: 10px;\n"
            "}\n"
            "\n"
            "QLabel#subheading {\n"
            "  color: #0f1925;\n"
            "  font-size: 12px;\n"
            "  font-weight: normal;\n"
            "  margin-bottom: 10px;\n"
            "}"
        )
        self.lblHomeInfo1.setObjectName("lblHomeInfo1")
        self.pbHomeConnect = QtWidgets.QPushButton(parent=self.frmHome)
        self.pbHomeConnect.setGeometry(QtCore.QRect(30, 540, 131, 41))
        self.pbHomeConnect.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbHomeConnect.setObjectName("pbHomeConnect")
        self.pbHomeSettings = QtWidgets.QPushButton(parent=self.frmHome)
        self.pbHomeSettings.setGeometry(QtCore.QRect(200, 540, 131, 41))
        self.pbHomeSettings.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "  background-color: #a2a4a7;\n"
            "  border: 3px solid #5c5c5d;\n"
            "}"
        )
        self.pbHomeSettings.setObjectName("pbHomeSettings")
        self.lblHomeLogo = QtWidgets.QLabel(parent=self.frmHome)
        self.lblHomeLogo.setGeometry(QtCore.QRect(140, 240, 211, 41))
        self.lblHomeLogo.setStyleSheet(
            '/*background-image: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'mainlogo@3x.png");*/\n'
            "\n"
            'border-image: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'mainlogo@3x.png");\n'
            "\n"
            ""
        )
        self.lblHomeLogo.setText("")
        self.lblHomeLogo.setObjectName("lblHomeLogo")
        self.lblHomeInfo2 = QtWidgets.QLabel(parent=self.frmHome)
        self.lblHomeInfo2.setGeometry(QtCore.QRect(30, 480, 301, 51))
        self.lblHomeInfo2.setStyleSheet(
            "QLabel {\n"
            "  background-color: #60000000;\n"
            "  color: #fff; /* color: #464d55; */\n"
            "  font-weight: 600;\n"
            "}\n"
            "QLabel#heading {\n"
            "  color: #0f1925;\n"
            "  font-size: "
            + self._settings.value("AppSettings/label_font_sizepx1")
            + ";\n"
            "  margin-bottom: 10px;\n"
            "}\n"
            "\n"
            "QLabel#subheading {\n"
            "  color: #0f1925;\n"
            "  font-size: 12px;\n"
            "  font-weight: normal;\n"
            "  margin-bottom: 10px;\n"
            "}"
        )
        self.lblHomeInfo2.setObjectName("lblHomeInfo2")
        self.lblHomeSpinner = QtWidgets.QLabel(parent=self.frmHome)
        self.lblHomeSpinner.setGeometry(QtCore.QRect(147, 415, 61, 61))
        self.lblHomeSpinner.setText("")
        self.lblHomeSpinner.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblHomeSpinner.setObjectName("lblHomeSpinner")
        self.lblHomeBackground.raise_()
        self.pbHomeConnect.raise_()
        self.pbHomeSettings.raise_()
        self.lblHomeInfo1.raise_()
        self.lblHomeLogo.raise_()
        self.lblHomeInfo2.raise_()
        self.lblHomeSpinner.raise_()
        self.frmSpectrum = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmSpectrum.setGeometry(QtCore.QRect(390, 10, 360, 611))
        self.frmSpectrum.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmSpectrum.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmSpectrum.setObjectName("frmSpectrum")
        self.pbSpectrumSaveBG = QtWidgets.QPushButton(parent=self.frmSpectrum)
        self.pbSpectrumSaveBG.setGeometry(QtCore.QRect(20, 0, 131, 41))
        self.pbSpectrumSaveBG.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbSpectrumSaveBG.setObjectName("pbSpectrumSaveBG")
        self.pbSpectrumRestoreBG = QtWidgets.QPushButton(parent=self.frmSpectrum)
        self.pbSpectrumRestoreBG.setGeometry(QtCore.QRect(200, 0, 131, 41))
        self.pbSpectrumRestoreBG.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbSpectrumRestoreBG.setObjectName("pbSpectrumRestoreBG")
        self.pbSpectrumSave = QtWidgets.QPushButton(parent=self.frmSpectrum)
        self.pbSpectrumSave.setGeometry(QtCore.QRect(200, 540, 131, 41))
        self.pbSpectrumSave.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbSpectrumSave.setObjectName("pbSpectrumSave")
        self.pbSpectrumClear = QtWidgets.QPushButton(parent=self.frmSpectrum)
        self.pbSpectrumClear.setGeometry(QtCore.QRect(30, 540, 131, 41))
        self.pbSpectrumClear.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbSpectrumClear.setObjectName("pbSpectrumClear")
        self.lblSpectrumSeconds = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumSeconds.setGeometry(QtCore.QRect(270, 90, 58, 31))
        self.lblSpectrumSeconds.setObjectName("lblSpectrumSeconds")
        self.lblSpectrumInfoScanTime = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumInfoScanTime.setGeometry(QtCore.QRect(30, 90, 71, 31))
        self.lblSpectrumInfoScanTime.setObjectName("lblSpectrumInfoScanTime")
        self.sbSpectrumScanTime = QtWidgets.QSpinBox(parent=self.frmSpectrum)
        self.sbSpectrumScanTime.setGeometry(QtCore.QRect(110, 90, 151, 31))
        self.sbSpectrumScanTime.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame2.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSpectrumScanTime.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.sbSpectrumScanTime.setObjectName("sbSpectrumScanTime")
        self.txtSpectrumJsonFileName = QtWidgets.QLineEdit(parent=self.frmSpectrum)
        self.txtSpectrumJsonFileName.setGeometry(QtCore.QRect(90, 410, 151, 31))
        self.txtSpectrumJsonFileName.setStyleSheet(
            "QLineEdit {\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid #e0e4e7;\n"
            "  padding: 5px 15px;\n"
            "  background-color: #fff;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "  border: 1px solid #d0e3ff;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "  color: #767e89;\n"
            "}"
        )
        self.txtSpectrumJsonFileName.setObjectName("txtSpectrumJsonFileName")
        self.lblSpectrumInfoNumberOfScannedSamples = QtWidgets.QLabel(
            parent=self.frmSpectrum
        )
        self.lblSpectrumInfoNumberOfScannedSamples.setGeometry(
            QtCore.QRect(30, 360, 291, 31)
        )
        self.lblSpectrumInfoNumberOfScannedSamples.setObjectName(
            "lblSpectrumInfoNumberOfScannedSamples"
        )
        self.lblSpectrumInfoSaveAs = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumInfoSaveAs.setGeometry(QtCore.QRect(30, 410, 71, 31))
        self.lblSpectrumInfoSaveAs.setObjectName("lblSpectrumInfoSaveAs")
        self.lblSpectrumExtensionJson = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumExtensionJson.setGeometry(QtCore.QRect(250, 410, 71, 31))
        self.lblSpectrumExtensionJson.setObjectName("lblSpectrumExtensionJson")
        self.txtSpectrumCsvFileName = QtWidgets.QLineEdit(parent=self.frmSpectrum)
        self.txtSpectrumCsvFileName.setGeometry(QtCore.QRect(90, 450, 151, 31))
        self.txtSpectrumCsvFileName.setStyleSheet(
            "QLineEdit {\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid #e0e4e7;\n"
            "  padding: 5px 15px;\n"
            "  background-color: #fff;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "  border: 1px solid #d0e3ff;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "  color: #767e89;\n"
            "}"
        )
        self.txtSpectrumCsvFileName.setObjectName("txtSpectrumCsvFileName")
        self.lblSpectrumExtensionCsv = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumExtensionCsv.setGeometry(QtCore.QRect(250, 450, 71, 31))
        self.lblSpectrumExtensionCsv.setObjectName("lblSpectrumExtensionCsv")
        self.label_7 = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.label_7.setGeometry(QtCore.QRect(30, 500, 71, 31))
        self.label_7.setObjectName("label_7")
        self.txtSpectrumPathFileDir = QtWidgets.QLineEdit(parent=self.frmSpectrum)
        self.txtSpectrumPathFileDir.setEnabled(True)
        self.txtSpectrumPathFileDir.setGeometry(QtCore.QRect(60, 500, 221, 31))
        self.txtSpectrumPathFileDir.setStyleSheet(
            "QLineEdit {\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid #e0e4e7;\n"
            "  padding: 5px 15px;\n"
            "  background-color: #fff;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "  border: 1px solid #d0e3ff;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "  color: #767e89;\n"
            "}"
        )
        self.txtSpectrumPathFileDir.setObjectName("txtSpectrumPathFileDir")
        self.tbSpectrumFindDir = QtWidgets.QToolButton(parent=self.frmSpectrum)
        self.tbSpectrumFindDir.setGeometry(QtCore.QRect(290, 500, 41, 31))
        self.tbSpectrumFindDir.setStyleSheet(
            "QToolButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "}\n"
            "QToolButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.tbSpectrumFindDir.setObjectName("tbSpectrumFindDir")
        self.tbSpectrumBG = QtWidgets.QToolButton(parent=self.frmSpectrum)
        self.tbSpectrumBG.setGeometry(QtCore.QRect(130, 150, 90, 90))
        self.tbSpectrumBG.setStyleSheet(
            "QToolButton {\n"
            'qproperty-icon: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'bg_btn_round_3@3x.png");\n'
            "background-position:4px left;\n"
            "    font-weight: 1;\n"
            "    border-radius: 0px;\n"
            "    padding: 0px 0px;\n"
            "    margin-top: 0px;\n"
            "    outline: 0px;\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            '    qproperty-icon: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'bg_btn_round_1@3x.png");\n'
            "}\n"
            ""
        )
        self.tbSpectrumBG.setText("")
        self.tbSpectrumBG.setIconSize(QtCore.QSize(90, 90))
        self.tbSpectrumBG.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly
        )
        self.tbSpectrumBG.setObjectName("tbSpectrumBG")
        self.tbSpectrumScan = QtWidgets.QToolButton(parent=self.frmSpectrum)
        self.tbSpectrumScan.setGeometry(QtCore.QRect(130, 260, 90, 90))
        self.tbSpectrumScan.setStyleSheet(
            "QToolButton {\n"
            'qproperty-icon: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'scan_bt3@3x.png");\n'
            "background-position:4px left;\n"
            "    font-weight: 1;\n"
            "    border-radius: 0px;\n"
            "    padding: 0px 0px;\n"
            "    margin-top: 0px;\n"
            "    outline: 0px;\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            '    qproperty-icon: url("'
            + self._settings.value("AppSettings/assets_dir")
            + 'scan_bt1@3x.png");\n'
            "}\n"
            "\n"
            ""
        )
        self.tbSpectrumScan.setText("")
        self.tbSpectrumScan.setIconSize(QtCore.QSize(90, 90))
        self.tbSpectrumScan.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly
        )
        self.tbSpectrumScan.setObjectName("tbSpectrumScan")

        self.lblSpectrumInfoNoScans = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumInfoNoScans.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.lblSpectrumInfoNoScans.setObjectName("lblSpectrumInfoNoScans")
        self.lblSpectrumNoScans = QtWidgets.QLabel(parent=self.frmSpectrum)
        self.lblSpectrumNoScans.setGeometry(QtCore.QRect(270, 50, 58, 31))
        self.lblSpectrumNoScans.setObjectName("lblSpectrumNoScans")
        self.sbSpectrumNoScans = QtWidgets.QSpinBox(parent=self.frmSpectrum)
        self.sbSpectrumNoScans.setGeometry(QtCore.QRect(110, 50, 151, 31))
        
        self.sbSpectrumNoScans.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame2.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )

        self.sbSpectrumNoScans.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sbSpectrumNoScans.setObjectName("sbSpectrumNoScans")
        
        self.frmSettings = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmSettings.setGeometry(QtCore.QRect(770, 10, 701, 611))
        self.frmSettings.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmSettings.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmSettings.setObjectName("frmSettings")
        self.lnSettingsSourceSettings = QtWidgets.QFrame(parent=self.frmSettings)
        self.lnSettingsSourceSettings.setGeometry(QtCore.QRect(30, 80, 301, 16))
        self.lnSettingsSourceSettings.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.lnSettingsSourceSettings.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lnSettingsSourceSettings.setObjectName("lnSettingsSourceSettings")
        self.lblSettingsSettings = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsSettings.setGeometry(QtCore.QRect(30, 30, 71, 31))
        self.lblSettingsSettings.setObjectName("lblSettingsSettings")
        self.pbSettingsRestore = QtWidgets.QPushButton(parent=self.frmSettings)
        self.pbSettingsRestore.setGeometry(QtCore.QRect(530, 540, 141, 41))
        self.pbSettingsRestore.setStyleSheet(
            "QPushButton {\n"
            "  background-color: #fe7a01;\n"
            "  color: #fff;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid rgb(253, 129, 13);\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: #0b5ed7;\n"
            "  border: 3px solid #9ac3fe;\n"
            "}"
        )
        self.pbSettingsRestore.setObjectName("pbSettingsRestore")
        self.lblSettingsSourceSettings = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsSourceSettings.setGeometry(QtCore.QRect(30, 60, 131, 31))
        self.lblSettingsSourceSettings.setObjectName("lblSettingsSourceSettings")
        self.lblSettingsT1 = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsT1.setGeometry(QtCore.QRect(40, 100, 21, 31))
        self.lblSettingsT1.setObjectName("lblSettingsT1")
        self.sbSettingsT1 = QtWidgets.QSpinBox(parent=self.frmSettings)
        self.sbSettingsT1.setGeometry(QtCore.QRect(100, 100, 61, 31))
        self.sbSettingsT1.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSettingsT1.setObjectName("sbSettingsT1")
        self.lblSettingsT2_C1 = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsT2_C1.setGeometry(QtCore.QRect(40, 140, 51, 31))
        self.lblSettingsT2_C1.setObjectName("lblSettingsT2_C1")
        self.sbSettingsT2_C1 = QtWidgets.QSpinBox(parent=self.frmSettings)
        self.sbSettingsT2_C1.setGeometry(QtCore.QRect(100, 140, 61, 31))
        self.sbSettingsT2_C1.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSettingsT2_C1.setObjectName("sbSettingsT2_C1")
        self.sbSettingsT2_C2 = QtWidgets.QSpinBox(parent=self.frmSettings)
        self.sbSettingsT2_C2.setGeometry(QtCore.QRect(260, 140, 61, 31))
        self.sbSettingsT2_C2.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSettingsT2_C2.setObjectName("sbSettingsT2_C2")
        self.lblSettingsT2_C2 = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsT2_C2.setGeometry(QtCore.QRect(200, 140, 51, 31))
        self.lblSettingsT2_C2.setObjectName("lblSettingsT2_C2")
        self.sbSettingsT2_MAX = QtWidgets.QSpinBox(parent=self.frmSettings)
        self.sbSettingsT2_MAX.setGeometry(QtCore.QRect(260, 100, 61, 31))
        self.sbSettingsT2_MAX.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSettingsT2_MAX.setObjectName("sbSettingsT2_MAX")
        self.lblSettingsT2_MAX = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsT2_MAX.setGeometry(QtCore.QRect(200, 100, 51, 31))
        self.lblSettingsT2_MAX.setObjectName("lblSettingsT2_MAX")
        self.lblSettingsDeltaT = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsDeltaT.setGeometry(QtCore.QRect(200, 180, 51, 31))
        self.lblSettingsDeltaT.setObjectName("lblSettingsDeltaT")
        self.sbSettingsDeltaT = QtWidgets.QSpinBox(parent=self.frmSettings)
        self.sbSettingsDeltaT.setGeometry(QtCore.QRect(260, 180, 61, 31))
        self.sbSettingsDeltaT.setStyleSheet(
            "QSpinBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-arrow:disabled,\n"
            "QSpinBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.sbSettingsDeltaT.setObjectName("sbSettingsDeltaT")
        self.lblSettingsLampCount = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsLampCount.setGeometry(QtCore.QRect(40, 280, 81, 31))
        self.lblSettingsLampCount.setObjectName("lblSettingsLampCount")
        self.lblSettingsLampSelect = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsLampSelect.setGeometry(QtCore.QRect(40, 240, 81, 31))
        self.lblSettingsLampSelect.setObjectName("lblSettingsLampSelect")
        self.label_19 = QtWidgets.QLabel(parent=self.frmSettings)
        self.label_19.setGeometry(QtCore.QRect(40, 320, 81, 31))
        self.label_19.setObjectName("label_19")
        self.lblSettingsMeasurementParameters = QtWidgets.QLabel(
            parent=self.frmSettings
        )
        self.lblSettingsMeasurementParameters.setGeometry(
            QtCore.QRect(30, 390, 191, 31)
        )
        self.lblSettingsMeasurementParameters.setObjectName(
            "lblSettingsMeasurementParameters"
        )
        self.lnSettingsMeasurementParameters = QtWidgets.QFrame(parent=self.frmSettings)
        self.lnSettingsMeasurementParameters.setGeometry(QtCore.QRect(30, 410, 301, 16))
        self.lnSettingsMeasurementParameters.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.lnSettingsMeasurementParameters.setFrameShadow(
            QtWidgets.QFrame.Shadow.Sunken
        )
        self.lnSettingsMeasurementParameters.setObjectName(
            "lnSettingsMeasurementParameters"
        )
        self.label_21 = QtWidgets.QLabel(parent=self.frmSettings)
        self.label_21.setGeometry(QtCore.QRect(30, 430, 81, 31))
        self.label_21.setObjectName("label_21")
        self.cbSettingsRunMode = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsRunMode.setGeometry(QtCore.QRect(220, 430, 101, 32))
        self.cbSettingsRunMode.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsRunMode.setObjectName("cbSettingsRunMode")
        self.cbSettingsRunMode.addItem("")
        self.cbSettingsRunMode.addItem("")
        self.label_22 = QtWidgets.QLabel(parent=self.frmSettings)
        self.label_22.setGeometry(QtCore.QRect(30, 470, 131, 31))
        self.label_22.setObjectName("label_22")
        self.cbSettingsOpticalGainSettings = QtWidgets.QComboBox(
            parent=self.frmSettings
        )
        self.cbSettingsOpticalGainSettings.setGeometry(QtCore.QRect(220, 470, 101, 32))
        self.cbSettingsOpticalGainSettings.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsOpticalGainSettings.setObjectName(
            "cbSettingsOpticalGainSettings"
        )
        self.cbSettingsOpticalGainSettings.addItem("")
        self.lblSettingsInfoOpticalGainSettings = QtWidgets.QLabel(
            parent=self.frmSettings
        )
        self.lblSettingsInfoOpticalGainSettings.setGeometry(
            QtCore.QRect(30, 500, 301, 31)
        )
        self.lblSettingsInfoOpticalGainSettings.setObjectName(
            "lblSettingsInfoOpticalGainSettings"
        )
        self.lnSettingsDisplayData = QtWidgets.QFrame(parent=self.frmSettings)
        self.lnSettingsDisplayData.setGeometry(QtCore.QRect(360, 80, 301, 16))
        self.lnSettingsDisplayData.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.lnSettingsDisplayData.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lnSettingsDisplayData.setObjectName("lnSettingsDisplayData")
        self.lblSettingsDisplayData = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsDisplayData.setGeometry(QtCore.QRect(360, 60, 191, 31))
        self.lblSettingsDisplayData.setObjectName("lblSettingsDisplayData")
        self.lblSettingsNumberDataPoints = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsNumberDataPoints.setGeometry(QtCore.QRect(370, 200, 151, 31))
        self.lblSettingsNumberDataPoints.setObjectName("lblSettingsNumberDataPoints")
        self.cbSettingsNumberDataPoints = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsNumberDataPoints.setGeometry(QtCore.QRect(560, 200, 101, 32))
        self.cbSettingsNumberDataPoints.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsNumberDataPoints.setObjectName("cbSettingsNumberDataPoints")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.cbSettingsNumberDataPoints.addItem("")
        self.lblSettingsInfoNumberDataPoints = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsInfoNumberDataPoints.setGeometry(
            QtCore.QRect(370, 240, 301, 111)
        )
        self.lblSettingsInfoNumberDataPoints.setWordWrap(True)
        self.lblSettingsInfoNumberDataPoints.setObjectName(
            "lblSettingsInfoNumberDataPoints"
        )
        self.lblSettingsInfoEnableLinearInterpolation = QtWidgets.QLabel(
            parent=self.frmSettings
        )
        self.lblSettingsInfoEnableLinearInterpolation.setGeometry(
            QtCore.QRect(370, 140, 301, 41)
        )
        self.lblSettingsInfoEnableLinearInterpolation.setWordWrap(True)
        self.lblSettingsInfoEnableLinearInterpolation.setObjectName(
            "lblSettingsInfoEnableLinearInterpolation"
        )
        self.lblSettingsInfoEnableFFTSettings = QtWidgets.QLabel(
            parent=self.frmSettings
        )
        self.lblSettingsInfoEnableFFTSettings.setGeometry(
            QtCore.QRect(370, 400, 311, 21)
        )
        self.lblSettingsInfoEnableFFTSettings.setWordWrap(True)
        self.lblSettingsInfoEnableFFTSettings.setObjectName(
            "lblSettingsInfoEnableFFTSettings"
        )
        self.lblSettingsFFTSettings = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsFFTSettings.setGeometry(QtCore.QRect(370, 420, 191, 31))
        self.lblSettingsFFTSettings.setObjectName("lblSettingsFFTSettings")
        self.lnSettingsFFTSettings = QtWidgets.QFrame(parent=self.frmSettings)
        self.lnSettingsFFTSettings.setGeometry(QtCore.QRect(370, 440, 301, 16))
        self.lnSettingsFFTSettings.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.lnSettingsFFTSettings.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lnSettingsFFTSettings.setObjectName("lnSettingsFFTSettings")
        self.lblSettingsNumberFFTPoints = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsNumberFFTPoints.setGeometry(QtCore.QRect(370, 500, 131, 31))
        self.lblSettingsNumberFFTPoints.setObjectName("lblSettingsNumberFFTPoints")
        self.lblSettingsApodizationFunction = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsApodizationFunction.setGeometry(QtCore.QRect(370, 460, 141, 31))
        self.lblSettingsApodizationFunction.setObjectName(
            "lblSettingsApodizationFunction"
        )
        self.cbSettingsApodizationFunction = QtWidgets.QComboBox(
            parent=self.frmSettings
        )
        self.cbSettingsApodizationFunction.setGeometry(QtCore.QRect(560, 460, 101, 32))
        self.cbSettingsApodizationFunction.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsApodizationFunction.setObjectName(
            "cbSettingsApodizationFunction"
        )
        self.cbSettingsApodizationFunction.addItem("")
        self.cbSettingsApodizationFunction.addItem("")
        self.cbSettingsApodizationFunction.addItem("")
        self.cbSettingsApodizationFunction.addItem("")
        self.cbSettingsNumberFFTPoints = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsNumberFFTPoints.setGeometry(QtCore.QRect(560, 500, 101, 32))
        self.cbSettingsNumberFFTPoints.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsNumberFFTPoints.setObjectName("cbSettingsNumberFFTPoints")
        self.cbSettingsNumberFFTPoints.addItem("")
        self.cbSettingsNumberFFTPoints.addItem("")
        self.cbSettingsNumberFFTPoints.addItem("")
        self.lblSettingsEnableLinearInterpolation = QtWidgets.QLabel(
            parent=self.frmSettings
        )
        self.lblSettingsEnableLinearInterpolation.setGeometry(
            QtCore.QRect(370, 100, 171, 31)
        )
        self.lblSettingsEnableLinearInterpolation.setObjectName(
            "lblSettingsEnableLinearInterpolation"
        )
        self.cbSettingsEnableLinearInterpolation = QtWidgets.QComboBox(
            parent=self.frmSettings
        )
        self.cbSettingsEnableLinearInterpolation.setGeometry(
            QtCore.QRect(560, 100, 101, 32)
        )
        self.cbSettingsEnableLinearInterpolation.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsEnableLinearInterpolation.setObjectName(
            "cbSettingsEnableLinearInterpolation"
        )
        self.cbSettingsEnableLinearInterpolation.addItem("")
        self.cbSettingsEnableLinearInterpolation.addItem("")
        self.lblSettingsEnableFFTSettings = QtWidgets.QLabel(parent=self.frmSettings)
        self.lblSettingsEnableFFTSettings.setGeometry(QtCore.QRect(370, 360, 171, 31))
        self.lblSettingsEnableFFTSettings.setObjectName("lblSettingsEnableFFTSettings")
        self.cbSettingsEnableFFTSettings = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsEnableFFTSettings.setGeometry(QtCore.QRect(560, 360, 101, 32))
        self.cbSettingsEnableFFTSettings.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsEnableFFTSettings.setObjectName("cbSettingsEnableFFTSettings")
        self.cbSettingsEnableFFTSettings.addItem("")
        self.cbSettingsEnableFFTSettings.addItem("")
        self.cbSettingsLampSelect = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsLampSelect.setGeometry(QtCore.QRect(130, 240, 191, 32))
        self.cbSettingsLampSelect.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsLampSelect.setObjectName("cbSettingsLampSelect")
        self.cbSettingsLampSelect.addItem("")
        self.cbSettingsLampSelect.addItem("")
        self.cbSettingsLampCount = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsLampCount.setGeometry(QtCore.QRect(130, 280, 191, 32))
        self.cbSettingsLampCount.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsLampCount.setObjectName("cbSettingsLampCount")
        self.cbSettingsLampCount.addItem("")
        self.cbSettingsLampCount.addItem("")
        self.cbSettingsLampCount.addItem("")
        self.cbSettingsResolution = QtWidgets.QComboBox(parent=self.frmSettings)
        self.cbSettingsResolution.setGeometry(QtCore.QRect(130, 320, 191, 32))
        self.cbSettingsResolution.setStyleSheet(
            "QComboBox {\n"
            "    padding-right: 15px; /* make room for the arrows */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "frame.png) 4;\n"
            "    border-width: 3;\n"
            "}\n"
            "\n"
            "QComboBox::up-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: top right; /* position at the top right corner */\n"
            "\n"
            "    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup.png) 1;\n"
            "    border-width: 1px;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spinup_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::up-arrow:disabled, QComboBox::up-arrow:off { /* off state when value is max */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "up_arrow_disabled.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-button {\n"
            "    subcontrol-origin: border;\n"
            "    subcontrol-position: bottom right; /* position at bottom right corner */\n"
            "\n"
            "    width: 16px;\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown.png) 1;\n"
            "    border-width: 1px;\n"
            "    border-top-width: 0;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:hover {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_hover.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-button:pressed {\n"
            "    border-image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "spindown_pressed.png) 1;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:disabled,\n"
            "QComboBox::down-arrow:off { /* off state when value in min */\n"
            "   image: url("
            + self._settings.value("AppSettings/assets_dir")
            + "down_arrow_disabled.png);\n"
            "}"
        )
        self.cbSettingsResolution.setObjectName("cbSettingsResolution")
        self.cbSettingsResolution.addItem("")
        self.cbSettingsResolution.addItem("")
        self.tbMainHome = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tbMainHome.setGeometry(QtCore.QRect(40, 640, 90, 90))
        self.tbMainHome.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tbMainHome.setAutoFillBackground(False)
        self.tbMainHome.setStyleSheet(
            "QToolButton {\n"
            '  qproperty-icon: url( "('
            + self._settings.value("AppSettings/assets_dir")
            + 'selected_home@3x.png");\n'
            "  background-color: #00000000;\n"
            "    background-position:4px left;\n"
            "  color: #ff484848;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid #00000000;\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "\n"
            "}"
        )
        self.tbMainHome.setIconSize(QtCore.QSize(48, 48))
        self.tbMainHome.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tbMainHome.setObjectName("tbMainHome")
        self.tbMainSpectrum = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tbMainSpectrum.setEnabled(True)
        self.tbMainSpectrum.setGeometry(QtCore.QRect(250, 640, 90, 90))
        
        self.tbMainSpectrum.setStyleSheet(
            "QToolButton {\n"
            '  qproperty-icon: url( "('
            + self._settings.value("AppSettings/assets_dir")
            + 'selected_spectral@3x.png");\n'
            "  background-color: #00000000;\n"
            "    background-position:4px left;\n"
            "  color: #ff484848;\n"
            "  font-weight: 600;\n"
            "  border-radius: 8px;\n"
            "  border: 1px solid #00000000;\n"
            "  padding: 5px 15px;\n"
            "  margin-top: 10px;\n"
            "  outline: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            'qproperty-icon: url('
            + self._settings.value("AppSettings/assets_dir")
            + 'spectral@3x.png);\n'
            "background-color: #a2a4a7;\n"
            "border: 3px solid #5c5c5d;\n"
            "\n"
            "}"
        )
        
        self.tbMainSpectrum.setIconSize(QtCore.QSize(48, 48))
        self.tbMainSpectrum.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tbMainSpectrum.setObjectName("tbMainSpectrum")

        self.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Ui_MainWindow", "NeoSpectra Micro"))
        self.lblHomeInfo1.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Interface with NeoSpectra Micro </span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Development Kits using your </span></p><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">PC</span></p></body></html>',
            )
        )
        self.pbHomeConnect.setText(_translate("Ui_MainWindow", "Connect"))
        self.pbHomeSettings.setText(_translate("Ui_MainWindow", "Settings"))
        self.lblHomeInfo2.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + ';">Please Connect to a Kit</span></p></body></html>',
            )
        )
        self.pbSpectrumSaveBG.setText(_translate("Ui_MainWindow", "Save BG"))
        self.pbSpectrumRestoreBG.setText(_translate("Ui_MainWindow", "Restore BG"))
        self.pbSpectrumSave.setText(_translate("Ui_MainWindow", "Save"))
        self.pbSpectrumClear.setText(_translate("Ui_MainWindow", "Clear"))
        self.lblSpectrumSeconds.setText(_translate("Ui_MainWindow", "seconds"))
        self.lblSpectrumInfoScanTime.setText(_translate("Ui_MainWindow", "Scan Time:"))
        self.txtSpectrumJsonFileName.setText(_translate("Ui_MainWindow", "untitled"))
        self.lblSpectrumInfoNumberOfScannedSamples.setText(
            _translate("Ui_MainWindow", "Number of Scanned Samples: 0")
        )
        self.lblSpectrumInfoSaveAs.setText(_translate("Ui_MainWindow", "Save As:"))
        self.lblSpectrumExtensionJson.setText(_translate("Ui_MainWindow", ".json"))
        self.txtSpectrumCsvFileName.setText(_translate("Ui_MainWindow", "untitled"))
        self.lblSpectrumExtensionCsv.setText(_translate("Ui_MainWindow", ".csv"))
        self.label_7.setText(_translate("Ui_MainWindow", "To:"))
        self.txtSpectrumPathFileDir.setText(_translate("Ui_MainWindow", "/temp/"))
        self.tbSpectrumFindDir.setText(_translate("Ui_MainWindow", "..."))

        self.lblSpectrumInfoNoScans.setText(_translate("MainWindow", "No. Of Scans:"))
        self.lblSpectrumNoScans.setText(_translate("MainWindow", "scans"))

        self.lblSettingsSettings.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p><span style=" font-size:'
                + self._settings.value("AppSettings/label_font_sizept1")
                + '; font-weight:700;">Settings</span></p></body></html>',
            )
        )
        self.pbSettingsRestore.setText(_translate("Ui_MainWindow", "Restore Defaults"))
        self.lblSettingsSourceSettings.setText(
            _translate("Ui_MainWindow", "SOURCE SETTINGS")
        )
        self.lblSettingsT1.setText(_translate("Ui_MainWindow", "T1"))
        self.lblSettingsT2_C1.setText(_translate("Ui_MainWindow", "T2_C1"))
        self.lblSettingsT2_C2.setText(_translate("Ui_MainWindow", "T2_C2"))
        self.lblSettingsT2_MAX.setText(_translate("Ui_MainWindow", "T2_MAX"))
        self.lblSettingsDeltaT.setText(_translate("Ui_MainWindow", "Delta T"))
        self.lblSettingsLampCount.setText(_translate("Ui_MainWindow", "Lamp Count"))
        self.lblSettingsLampSelect.setText(_translate("Ui_MainWindow", "Lamp Select"))
        self.label_19.setText(_translate("Ui_MainWindow", "Resolution"))
        self.lblSettingsMeasurementParameters.setText(
            _translate("Ui_MainWindow", "MEASUREMENT PARAMETERS")
        )
        self.label_21.setText(_translate("Ui_MainWindow", "Run Mode"))
        self.cbSettingsRunMode.setItemText(0, _translate("Ui_MainWindow", "Single"))
        self.cbSettingsRunMode.setItemText(1, _translate("Ui_MainWindow", "Continous"))
        self.label_22.setText(_translate("Ui_MainWindow", "Optical Gain Settings"))
        self.cbSettingsOpticalGainSettings.setItemText(
            0, _translate("Ui_MainWindow", "Default")
        )
        self.lblSettingsInfoOpticalGainSettings.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; color:#797979;">Select gain settings most suitable to your measurement.</span></p></body></html>',
            )
        )
        self.lblSettingsDisplayData.setText(_translate("Ui_MainWindow", "DISPLAY DATA"))
        self.lblSettingsNumberDataPoints.setText(
            _translate("Ui_MainWindow", "Number of Data Points")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            0, _translate("Ui_MainWindow", "65 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            1, _translate("Ui_MainWindow", "129 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            2, _translate("Ui_MainWindow", "257 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            3, _translate("Ui_MainWindow", "513 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            4, _translate("Ui_MainWindow", "1024 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            5, _translate("Ui_MainWindow", "2048 pts")
        )
        self.cbSettingsNumberDataPoints.setItemText(
            6, _translate("Ui_MainWindow", "4096 pts")
        )
        self.lblSettingsInfoNumberDataPoints.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; color:#797979;">Select the number of data points for the wavelength vector. Raw data contain by default XXXX data points across the spectral range. The raw data are linearly interpolated to generate the number of data points that you select. Under-sampling results in losing some data but ensures speedy processing and communication. Over-sampling does not provide additional information, but provides smoother spectra.</span></p></body></html>',
            )
        )
        self.lblSettingsInfoEnableLinearInterpolation.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; color:#797979;">If disabled, you\'ll get the raw data from the connected NeoSpectra. If enabled, you can ensure that all NeoSpectra units provide the same wavelength vector.</span></p></body></html>',
            )
        )
        self.lblSettingsInfoEnableFFTSettings.setText(
            _translate(
                "Ui_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; color:#797979;">Select settings for processing Fourier Transform.</span></p></body></html>',
            )
        )
        self.lblSettingsFFTSettings.setText(_translate("Ui_MainWindow", "FFT Settings"))
        self.lblSettingsNumberFFTPoints.setText(
            _translate("Ui_MainWindow", "Number of FFT Points")
        )
        self.lblSettingsApodizationFunction.setText(
            _translate("Ui_MainWindow", "Apodization Function")
        )
        self.cbSettingsApodizationFunction.setItemText(
            0, _translate("Ui_MainWindow", "Boxcar")
        )
        self.cbSettingsApodizationFunction.setItemText(
            1, _translate("Ui_MainWindow", "Gaussian")
        )
        self.cbSettingsApodizationFunction.setItemText(
            2, _translate("Ui_MainWindow", "Happ-Genzel")
        )
        self.cbSettingsApodizationFunction.setItemText(
            3, _translate("Ui_MainWindow", "Lorenz")
        )
        self.cbSettingsNumberFFTPoints.setItemText(
            0, _translate("Ui_MainWindow", "8 K")
        )
        self.cbSettingsNumberFFTPoints.setItemText(
            1, _translate("Ui_MainWindow", "16 K")
        )
        self.cbSettingsNumberFFTPoints.setItemText(
            2, _translate("Ui_MainWindow", "32 K")
        )
        self.lblSettingsEnableLinearInterpolation.setText(
            _translate("Ui_MainWindow", "Enable Linear Interpolation")
        )
        self.cbSettingsEnableLinearInterpolation.setItemText(
            0, _translate("Ui_MainWindow", "Enabled")
        )
        self.cbSettingsEnableLinearInterpolation.setItemText(
            1, _translate("Ui_MainWindow", "Disabled")
        )
        self.lblSettingsEnableFFTSettings.setText(
            _translate("Ui_MainWindow", "Enable FFT Settings")
        )
        self.cbSettingsEnableFFTSettings.setItemText(
            0, _translate("Ui_MainWindow", "Enabled")
        )
        self.cbSettingsEnableFFTSettings.setItemText(
            1, _translate("Ui_MainWindow", "Disabled")
        )
        self.cbSettingsLampSelect.setItemText(0, _translate("Ui_MainWindow", "0"))
        self.cbSettingsLampSelect.setItemText(1, _translate("Ui_MainWindow", "1"))
        self.cbSettingsLampCount.setItemText(0, _translate("Ui_MainWindow", "0"))
        self.cbSettingsLampCount.setItemText(1, _translate("Ui_MainWindow", "1"))
        self.cbSettingsLampCount.setItemText(2, _translate("Ui_MainWindow", "2"))
        self.cbSettingsResolution.setItemText(
            0, _translate("Ui_MainWindow", "16 nm @ 1500 nm")
        )
        self.cbSettingsResolution.setItemText(
            1, _translate("Ui_MainWindow", "32 nm @ 1500 nm")
        )
        self.tbMainHome.setText(_translate("Ui_MainWindow", "Home"))
        self.tbMainSpectrum.setText(_translate("Ui_MainWindow", "Spectrum"))

    def setDefaultSettings(self):
        if self._settings == None:
            return

        self._settings.setValue(
            "AppSettings/temp_dir",
            "/Users/fbetancourt/Desktop/NeoSpectraMicroPython/Temp/",
        )
        self._settings.setValue(
            "AppSettings/assets_dir",
            "/Users/fbetancourt/Desktop/NeoSpectraMicroPython/Assets/",
        )

        self._settings.setValue("AppSettings/label_font_sizept1", "18pt")
        self._settings.setValue("AppSettings/label_font_sizepx1", "18px")

        self._settings.setValue("DeviceSettings/SourceSettings/T1", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/T2_C1", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/T2_C2", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/T2_MAX", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/DeltaT", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/LampSelect", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/LampCount", 0)
        self._settings.setValue("DeviceSettings/SourceSettings/Resolution", 0)

        self._settings.setValue("DeviceSettings/MeasurementParameters/RunMode", 0)
        self._settings.setValue(
            "DeviceSettings/MeasurementParameters/OpticalGainSettings", 0
        )

        self._settings.setValue(
            "DeviceSettings/DisplayData/EnableLinearInterpolation", 0
        )
        self._settings.setValue("DeviceSettings/DisplayData/NumberOfDataPoints", 0)
        self._settings.setValue("DeviceSettings/DisplayData/EnableFFTSettings", 0)

        self._settings.setValue("DeviceSettings/FFTSettings/ApodizationFunction", 0)
        self._settings.setValue("DeviceSettings/FFTSettings/NumberOfFFTPoints", 0)

        self._settings.sync()
