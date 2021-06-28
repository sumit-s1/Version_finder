# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Version_Info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import islice
import configparser
import subprocess
import os
import fnmatch
import tkinter
import winreg
from win32 import win32security





class Ui_VersionInfo(object):

    def dropInfo(self):
        self.lblVersion.setText("")
        self.lblVersion.repaint()
        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.OkButton.setText("Please Wait..")
        self.OkButton.setStyleSheet("background-color: yellow; font: bold")
        self.OkButton.repaint()
        tch_type = self.dropTouchpoint.currentIndex()
        register = self.Reg.text()

        # Check if system is Online
        try:
            subprocess.check_call(['ping', '-n', '1', register], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            is_up = True
        except subprocess.CalledProcessError:
            is_up = False

        if is_up is True:

            if tch_type == 8 or tch_type == 9:
                if tch_type == 8:
                    try:
                        target = r"\\"+register
                        handle = win32security.LogonUser("sysmoduser", "NSWRO", "S3nS@tiON",
                                                         win32security.LOGON32_LOGON_NEW_CREDENTIALS,
                                                         win32security.LOGON32_PROVIDER_DEFAULT)
                        win32security.ImpersonateLoggedOnUser(handle)
                        rem_reg = winreg.ConnectRegistry(target, winreg.HKEY_LOCAL_MACHINE)
                        rem_key = winreg.OpenKey(rem_reg, r'SOFTWARE\Wow6432Node\PC-EFTPOS\LFD')
                        z = winreg.QueryValueEx(rem_key, "RelToDld")
                        win32security.RevertToSelf()
                        handle.Close()

                        self.lblVersion.setText("EFT Version in StoreServer: " + z[0])
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        rem_reg.Close()

                    except Exception:
                        self.lblVersion.setText("EFT Version not accessible/available")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                if tch_type == 9:
                    try:
                        register = register.lower()
                        if "." in register:
                            key = register.rsplit('.', 1)[1]
                            z = len(key)
                            if z == 1:
                                key = "00" + key
                            else:
                                key = "0" + key
                            reg1 = register.rsplit('.', 1)[0] + ".240"
                            target = r"\\"+reg1
                            handle = win32security.LogonUser("sysmoduser", "NSWRO", "S3nS@tiON",
                                                             win32security.LOGON32_LOGON_NEW_CREDENTIALS,
                                                             win32security.LOGON32_PROVIDER_DEFAULT)
                            win32security.ImpersonateLoggedOnUser(handle)
                            rem_reg = winreg.ConnectRegistry(target, winreg.HKEY_LOCAL_MACHINE)
                            rem_key = winreg.OpenKey(rem_reg, r'SOFTWARE\Wow6432Node\PC-EFTPOS\LFD')
                            i = 0
                            while True:
                                try:
                                    hit = winreg.EnumKey(rem_key, i)
                                    if key in hit:
                                        new_key = r'SOFTWARE\Wow6432Node\PC-EFTPOS\LFD' + "\\" + hit
                                        rem_key = winreg.OpenKey(rem_reg, new_key)
                                        z = winreg.QueryValueEx(rem_key, "ActiveSwRelease")
                                        win32security.RevertToSelf()
                                        handle.Close()
                                        self.lblVersion.setText("EFT Version in Register: " + z[0])
                                        self.OkButton.setText("Get Version")
                                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                        rem_reg.Close()
                                        break
                                    i += 1
                                except WindowsError:
                                    self.lblVersion.setText("Incorrect Parameters Entered")
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                    break

                        elif "rg" in register or "sc" in register or "ws" in register:
                            reg0 = register.lower()
                            if "rg" in reg0: reg1 = reg0.rsplit('rg', 1)[0] + "rs001"
                            if "sc" in reg0: reg1 = reg0.rsplit('sc', 1)[0] + "rs001"
                            if "ws" in reg0: reg1 = reg0.rsplit('rg', 1)[0] + "rs001"
                            key = register[-3:]
                            target = r"\\" + reg1
                            handle = win32security.LogonUser("sysmoduser", "NSWRO", "S3nS@tiON",
                                                             win32security.LOGON32_LOGON_NEW_CREDENTIALS,
                                                             win32security.LOGON32_PROVIDER_DEFAULT)
                            win32security.ImpersonateLoggedOnUser(handle)
                            rem_reg = winreg.ConnectRegistry(target, winreg.HKEY_LOCAL_MACHINE)
                            rem_key = winreg.OpenKey(rem_reg, r'SOFTWARE\Wow6432Node\PC-EFTPOS\LFD')
                            i = 0
                            while True:
                                try:
                                    hit = winreg.EnumKey(rem_key, i)
                                    if key in hit:
                                        new_key = r'SOFTWARE\Wow6432Node\PC-EFTPOS\LFD' + "\\" + hit
                                        rem_key = winreg.OpenKey(rem_reg, new_key)
                                        z = winreg.QueryValueEx(rem_key, "ActiveSwRelease")
                                        win32security.RevertToSelf()
                                        handle.Close()
                                        self.lblVersion.setText("EFT Version in Register: " + z[0])
                                        self.OkButton.setText("Get Version")
                                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                        rem_reg.Close()
                                        break
                                    i += 1
                                except WindowsError:
                                    self.lblVersion.setText("Incorrect Parameters Entered")
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                    break

                        else:
                            self.lblVersion.setText("Incorrect Parameters Entered")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                    except:
                        self.lblVersion.setText("Incorrect Parameters Entered")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


            else:
                pos_path = "//c$//Retalix//StoreServices//POSClient//"
                sco_path = "//c$//scot//install//InstallHistory.log"
                rs_path = "//c$//Retalix//StoreServices//Server//PosService//Extensions//"
                wks_path = "//c$//Windows//Build.ini"
                storerelease_pos_path = "//c$//Windows//Version.ini"
                storerelease_rs_path = "//d$//Upgrades//Version.ini"
                load_path = "\c$"
                pos_full_path = register + pos_path
                sco_full_path = register + sco_path
                rs_full_path = register + rs_path
                storerelease_fullpath = register + storerelease_pos_path
                storerelease_rs_fullpath = register + storerelease_rs_path
                wks_full_path = register + wks_path
                full_path1 = register + load_path

                try:

                    subprocess.call(r'net use z: /del', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    subprocess.call(r'net use z: \\' + full_path1 + ' /user:NSWRO\sysmoduser S3nS@tiON', shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception:
                    self.lblVersion.setText("System Offline or Error connecting to the destination\nPlease try again")
                    self.OkButton.setText("Get Version")
                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### POS Version ######
                if tch_type == 0:
                    flag = 0
                    try:
                        for f_name in os.listdir("//" + pos_full_path):
                            if fnmatch.fnmatch(f_name, '*WOW-POSClient-CI.txt'):
                                flag = 1
                                version = open("//" + pos_full_path + f_name, "r")
                                self.lblVersion.setText(version.readlines()[0])
                                self.OkButton.setText("Get Version")
                                self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                version.close()
                        if flag == 0:
                            for f_nam in os.listdir("//" + rs_full_path):
                                if fnmatch.fnmatch(f_nam, '*WOW-StoreServer-CI.txt'):
                                    version = open("//" + rs_full_path + f_nam, "r")
                                    self.lblVersion.setText(version.readlines()[0])
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                    version.close()

                    except FileNotFoundError:
                        self.lblVersion.setText("System Offline or Touch Point not found")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### FL Version ######
                elif tch_type == 1:
                    try:
                        flag = 0
                        sco_string = "This integration build is part of WoW FL Drop release version"
                        with open("//" + sco_full_path, "r") as file:
                            for line in file:
                                if sco_string in line:
                                    flag = 1
                                    self.lblVersion.setText(line)
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                        if flag == 0:
                            self.lblVersion.setText("System Offline or Touch Point not found")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except FileNotFoundError:
                        self.lblVersion.setText("System Offline or Touch Point not found")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### Store Sever ######
                elif tch_type == 2:
                    try:
                        flag = 0
                        for f_name in os.listdir("//" + rs_full_path):
                            if fnmatch.fnmatch(f_name, '*WOW-StoreServer-CI.txt'):
                                version = open("//" + rs_full_path + f_name, "r")
                                self.lblVersion.setText(version.readlines()[0])
                                flag = 1
                                self.OkButton.setText("Get Version")
                                self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                version.close()

                        if flag == 0:
                            self.lblVersion.setText("Incorrect Parameters for Store Server version")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                    except FileNotFoundError:
                        self.lblVersion.setText("Incorrect Parameters for Store Server version")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### POS/SCO Store Release ######
                elif tch_type == 3:
                    try:
                        storerelease_string = 'Full Version of this Upgrade'
                        with open("//" + storerelease_fullpath, "r") as file:
                            for line in file:
                                if storerelease_string in line:
                                    tempstring = list(islice(file, 1))[-1] + list(islice(file, 1))[-1] + list(islice(file, 1))[
                                        -1]
                                    self.lblVersion.setText(tempstring)
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except FileNotFoundError:
                        self.lblVersion.setText("System Offline or Touch Point not found")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### RS Store Release ######
                elif tch_type == 4:
                    try:
                        storerelease_string = 'Full Version of this Upgrade'
                        with open("//" + storerelease_rs_fullpath, "r") as file:
                            for line in file:
                                if storerelease_string in line:
                                    tempstring = list(islice(file, 1))[-1] + list(islice(file, 1))[-1] + list(islice(file, 1))[
                                        -1]
                                    self.lblVersion.setText(tempstring)
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except FileNotFoundError:
                        self.lblVersion.setText("Incorrect Parameters for Store Release")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### FL Store Server Patch######
                elif tch_type == 5:
                    try:
                        flag = 0
                        patch_string = "Successfully Installed Store Server-WoW Full "
                        with open("//" + sco_full_path, "r") as file:
                            for line in file:
                                if patch_string in line:
                                    flag = 1
                                    # a = (line.split(patch__string, 1)[1])
                                    self.lblVersion.setText("FL - Store Server Patch: " + line.split(patch_string, 1)[-1])
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                        if flag == 0:
                            self.lblVersion.setText("Incorrect parameters provided")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except FileNotFoundError:
                        self.lblVersion.setText("FL not installed or incorrect parameters provided")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### Data Pump Version ######
                elif tch_type == 6:
                    try:
                        flag = 0
                        dp_string = "Installing WOW_NCRDataPump"
                        with open("//" + sco_full_path, "r") as file:
                            for line in file:
                                if dp_string in line:
                                    flag = 1
                                    self.lblVersion.setText("Data Pump Version: " + line.split(dp_string, 1)[1])
                                    self.OkButton.setText("Get Version")
                                    self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                                    self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                        if flag == 0:
                            self.lblVersion.setText("DataPump not installed or incorrect parameters provided")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except FileNotFoundError:
                        self.lblVersion.setText("DataPump not installed or incorrect parameters provided")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                ##### Works Station Release Version ######
                elif tch_type == 7:
                    try:
                        flag = 0
                        config = configparser.RawConfigParser()
                        config.read(r"//" + wks_full_path, encoding='utf-16')
                        a = config.get('BUILDSTATUS', 'Release')
                        if a != "":
                            flag = 1
                            self.lblVersion.setText("Workstation Release: " + a)
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                        if flag == 0:
                            self.lblVersion.setText("Incorrect parameters provided")
                            self.OkButton.setText("Get Version")
                            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


                    except (configparser.NoSectionError, FileNotFoundError,  UnicodeError):
                        self.lblVersion.setText("Release Details Unavailable or Incorrect Parameters Provided")
                        self.OkButton.setText("Get Version")
                        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
                        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        else:
            self.lblVersion.setText("System is Offline or Inaccessible\nPlease try again")
            self.OkButton.setText("Get Version")
            self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
            self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))






    def setupUi(self, VersionInfo):
        VersionInfo.setObjectName("VersionInfo")
        VersionInfo.resize(696, 250)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        VersionInfo.setFont(font)
        VersionInfo.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(VersionInfo)
        self.centralwidget.setObjectName("centralwidget")

        self.dropTouchpoint = QtWidgets.QComboBox(self.centralwidget)
        self.dropTouchpoint.setGeometry(QtCore.QRect(105, 20, 210, 22))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.dropTouchpoint.setStyleSheet("background-color: Powderblue")
        self.dropTouchpoint.setFont(font)
        self.dropTouchpoint.setAutoFillBackground(True)
        self.dropTouchpoint.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.dropTouchpoint.setObjectName("dropTouchpoint")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")
        self.dropTouchpoint.addItem("")

        self.lblTouchpoint = QtWidgets.QLabel(self.centralwidget)
        self.lblTouchpoint.setGeometry(QtCore.QRect(15, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblTouchpoint.setFont(font)
        self.lblTouchpoint.setObjectName("lblTouchpoint")

        self.lblTouchpointName = QtWidgets.QLabel(self.centralwidget)
        self.lblTouchpointName.setGeometry(QtCore.QRect(370, 20, 171, 20))
        self.lblTouchpointName.setObjectName("lblTouchpointName")

        self.lblVersion = QtWidgets.QLabel(self.centralwidget)
        self.lblVersion.setGeometry(QtCore.QRect(15, 105, 665, 120))
        self.lblVersion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblVersion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblVersion.setLineWidth(13)
        self.lblVersion.setText("")
        self.lblVersion.setTextFormat(QtCore.Qt.RichText)
        self.lblVersion.setWordWrap(True)
        self.lblVersion.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.lblVersion.setStyleSheet("background-color: Ivory")
        self.lblVersion.setObjectName("lblVersion")

        self.Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.Reg.setGeometry(QtCore.QRect(525, 20, 150, 22))
        self.Reg.setStyleSheet("background-color: Powderblue")
        self.Reg.setObjectName("Reg")

        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(290, 70, 100, 28))
        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OkButton.setFlat(False)
        self.OkButton.setObjectName("OkButton")
        self.OkButton.setStyleSheet("background-color: Lightgreen; font: bold")
        # --------------------------Get Version-------------------------#
        self.OkButton.clicked.connect(self.dropInfo)
        # --------------------------------------------------------------#

        VersionInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VersionInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 26))
        self.menubar.setObjectName("menubar")
        VersionInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VersionInfo)
        self.statusbar.setObjectName("statusbar")
        VersionInfo.setStatusBar(self.statusbar)

        self.retranslateUi(VersionInfo)
        QtCore.QMetaObject.connectSlotsByName(VersionInfo)

    def retranslateUi(self, VersionInfo):
        _translate = QtCore.QCoreApplication.translate
        VersionInfo.setWindowIcon(QtGui.QIcon('icon_image.ico'))
        VersionInfo.setWindowTitle(_translate("VersionInfo", "Version Info_4.1"))
        self.dropTouchpoint.setItemText(0, _translate("VersionInfo", "R10 Drop - POS/SCO"))
        self.dropTouchpoint.setItemText(1, _translate("VersionInfo", "FL Drop - SCO Lane"))
        self.dropTouchpoint.setItemText(2, _translate("VersionInfo", "Store Server Drop"))
        self.dropTouchpoint.setItemText(3, _translate("VersionInfo", "POS/SCO Store Release"))
        self.dropTouchpoint.setItemText(4, _translate("VersionInfo", "Store Server Release"))
        self.dropTouchpoint.setItemText(5, _translate("VersionInfo", "FL - Store Server Patch"))
        self.dropTouchpoint.setItemText(6, _translate("VersionInfo", "Data Pump"))
        self.dropTouchpoint.setItemText(7, _translate("VersionInfo", "Workstation Store Release"))
        self.dropTouchpoint.setItemText(8, _translate("VersionInfo", "Store Server EFT Version"))
        self.dropTouchpoint.setItemText(9, _translate("VersionInfo", "POS/SCO EFT Version"))
        self.lblTouchpoint.setText(_translate("VersionInfo", "Version For:"))
        self.lblTouchpointName.setText(_translate("VersionInfo", "Touchpoint Name/IP"))
        self.OkButton.setText(_translate("VersionInfo", "Get Version"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    VersionInfo = QtWidgets.QMainWindow()
    ui = Ui_VersionInfo()
    ui.setupUi(VersionInfo)
    VersionInfo.show()
    sys.exit(app.exec_())
