from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import pic_1_rc
import sys
import os
import datetime
import csv
import sqlite3
import ctypes
import subprocess
import time
from WorkList_db import WorkList_db_class

print(sys.version, "SubUI\n")

class Ui_MainWindow(QtWidgets.QDialog):
    plate_type = "Plate"
    cap_type = "Cap"
    ctrl_seq = "NC, PC"
    smp_count_1 = 0
    smp_count_2 = 0
    path1 = ""
    temp_src = ""
    bcd_list = []
    temp_bcd_list = []
    bcd_count = 0
    DB = WorkList_db_class()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        plrn_path = self.DB.display_path()

        self.setWindowTitle("Seegene WorkList")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(770, 800)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(97, -24, 680, 825))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_1 = QtWidgets.QWidget()
        self.Tab_1.setObjectName("Tab_1")
        self.lineEdit_smp_bcd = QtWidgets.QLineEdit(self.Tab_1)
        self.lineEdit_smp_bcd.setGeometry(QtCore.QRect(370, 100, 251, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_smp_bcd.setFont(font)
        self.lineEdit_smp_bcd.setStyleSheet("")
        self.lineEdit_smp_bcd.setObjectName("lineEdit_smp_bcd")
        self.toolButton_load = QtWidgets.QToolButton(self.Tab_1)
        self.toolButton_load.setGeometry(QtCore.QRect(233, 100, 28, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_load.setFont(font)
        self.toolButton_load.setStyleSheet("")
        self.toolButton_load.setObjectName("toolButton_load")
        self.pushButton_smp_ok = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_smp_ok.setGeometry(QtCore.QRect(191, 101, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_smp_ok.setFont(font)
        self.pushButton_smp_ok.setStyleSheet("background-color: rgb(77, 154, 231);\n"
                                             "color: rgb(255, 255, 255);")
        self.pushButton_smp_ok.setObjectName("pushButton_smp_ok")
        self.tableWidget_smp = QtWidgets.QTableWidget(self.Tab_1)
        self.tableWidget_smp.setGeometry(QtCore.QRect(70, 170, 511, 561))
        self.tableWidget_smp.setObjectName("tableWidget_smp")
        self.tableWidget_smp.setColumnCount(3)
        self.tableWidget_smp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_smp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_smp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_smp.setHorizontalHeaderItem(2, item)

        self.pushButton_copy = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_copy.setGeometry(QtCore.QRect(410, 136, 71, 28))
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_reload = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_reload.setGeometry(QtCore.QRect(490, 136, 71, 28))
        self.pushButton_reload.setObjectName("pushButton_reload")

        self.label_smp_count = QtWidgets.QLabel(self.Tab_1)
        self.label_smp_count.setGeometry(QtCore.QRect(29, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_smp_count.setFont(font)
        self.label_smp_count.setObjectName("label_smp_count")
        self.lineEdit_smp_count = QtWidgets.QLineEdit(self.Tab_1)
        self.lineEdit_smp_count.setGeometry(QtCore.QRect(138, 101, 50, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_smp_count.setFont(font)
        self.lineEdit_smp_count.setStyleSheet("")
        self.lineEdit_smp_count.setObjectName("lineEdit_smp_count")
        self.label_smp_bcd = QtWidgets.QLabel(self.Tab_1)
        self.label_smp_bcd.setGeometry(QtCore.QRect(300, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_smp_bcd.setFont(font)
        self.label_smp_bcd.setObjectName("label_smp_bcd")
        self.pushButton_next_1 = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_next_1.setGeometry(QtCore.QRect(530, 750, 93, 28))
        self.pushButton_next_1.setObjectName("pushButton_next_1")
        self.pushButton_arrow_1 = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_arrow_1.setGeometry(QtCore.QRect(315, 60, 16, 31))
        self.pushButton_arrow_1.setStyleSheet("image: url(:/newPrefix/pic_1.png);\n"
                                              "border-style: outset;\n"
                                              "border-width: 0px;\n"
                                              "border-color: black;\n"
                                              "padding: 1px;\n"
                                              "border-radius: 15px;\n"
                                              "")
        self.pushButton_arrow_1.setText("")
        self.pushButton_arrow_1.setObjectName("pushButton_arrow_1")
        self.pushButton_smp_info_1 = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_smp_info_1.setGeometry(QtCore.QRect(-1, 60, 325, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_smp_info_1.setFont(font)
        self.pushButton_smp_info_1.setStyleSheet("border-style: outset;\n"
                                                 "background-color: rgb(225, 225, 225);\n"
                                                 "border-width: 0px;\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pushButton_smp_info_1.setObjectName("pushButton_smp_info_1")
        self.pushButton_protocol_info_1 = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton_protocol_info_1.setGeometry(QtCore.QRect(324, 60, 360, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_protocol_info_1.setFont(font)
        self.pushButton_protocol_info_1.setStyleSheet("border-style: outset;\n"
                                                      "background-color: rgb(225, 225, 225);\n"
                                                      "border-width: 0px;\n"
                                                      "\n"
                                                      "\n"
                                                      "")
        self.pushButton_protocol_info_1.setObjectName("pushButton_protocol_info_1")
        self.pushButton_protocol_info_1.setEnabled(False)
        self.line_5 = QtWidgets.QFrame(self.Tab_1)
        self.line_5.setGeometry(QtCore.QRect(0, 85, 685, 8))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.lineEdit_smp_bcd.raise_()
        self.toolButton_load.raise_()
        self.pushButton_smp_ok.raise_()
        self.tableWidget_smp.raise_()
        self.label_smp_count.raise_()
        self.lineEdit_smp_count.raise_()
        self.label_smp_bcd.raise_()
        self.pushButton_next_1.raise_()
        self.pushButton_smp_info_1.raise_()
        self.pushButton_protocol_info_1.raise_()
        self.line_5.raise_()
        self.pushButton_arrow_1.raise_()
        self.tabWidget.addTab(self.Tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_protocol = QtWidgets.QLabel(self.tab_2)
        self.label_protocol.setGeometry(QtCore.QRect(30, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_protocol.setFont(font)
        self.label_protocol.setObjectName("label_protocol")
        self.pushButton_prev_1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_prev_1.setGeometry(QtCore.QRect(30, 750, 93, 28))
        self.pushButton_prev_1.setObjectName("pushButton_prev_1")
        self.listWidget_protocol = QtWidgets.QListWidget(self.tab_2) 
        self.listWidget_protocol.setGeometry(QtCore.QRect(110, 120, 370, 71))
        self.listWidget_protocol.setObjectName("listWidget_protocol")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_protocol.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_protocol.addItem(item)
        self.listWidget_protocol.setEnabled(False)
        self.pushButton_run = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_run.setGeometry(QtCore.QRect(530, 750, 93, 28))
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_run.setEnabled(False)

        self.pushButton_hidden = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_hidden.setGeometry(QtCore.QRect(462, 418, 20, 20))
        self.pushButton_hidden.setObjectName("pushButton_hidden")
        self.pushButton_hidden.setStyleSheet("border-style: outset;\n"
                                              "border-width: 0px;\n"
                                              "border-color: black;\n"
                                              "")
        self.label_tube_type = QtWidgets.QLabel(self.tab_2)
        self.label_tube_type.setGeometry(QtCore.QRect(30, 260, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tube_type.setFont(font)
        self.label_tube_type.setObjectName("label_tube_type")
        self.radioButton_tube_1 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_tube_1.setGeometry(QtCore.QRect(220, 260, 108, 19))
        self.radioButton_tube_1.setObjectName("radioButton_tube_1")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_tube_1)
        self.radioButton_tube_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_tube_2.setGeometry(QtCore.QRect(370, 260, 108, 19))
        self.radioButton_tube_2.setObjectName("radioButton_tube_2")
        self.buttonGroup_2.addButton(self.radioButton_tube_2)
        self.label_cap_type = QtWidgets.QLabel(self.tab_2)
        self.label_cap_type.setGeometry(QtCore.QRect(30, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cap_type.setFont(font)
        self.label_cap_type.setObjectName("label_cap_type")
        self.radioButton_cap_1 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_cap_1.setGeometry(QtCore.QRect(220, 320, 108, 19))
        self.radioButton_cap_1.setObjectName("radioButton_cap_1")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_cap_1)
        self.radioButton_cap_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_cap_2.setGeometry(QtCore.QRect(370, 320, 108, 19))
        self.radioButton_cap_2.setObjectName("radioButton_cap_2")
        self.buttonGroup_3.addButton(self.radioButton_cap_2)
        self.lineEdit_pcr_bcd = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_pcr_bcd.setGeometry(QtCore.QRect(210, 418, 251, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_pcr_bcd.setFont(font)
        self.lineEdit_pcr_bcd.setStyleSheet("")
        self.lineEdit_pcr_bcd.setObjectName("lineEdit_pcr_bcd")
        self.label_pcr_bcd = QtWidgets.QLabel(self.tab_2)
        self.label_pcr_bcd.setGeometry(QtCore.QRect(30, 412, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pcr_bcd.setFont(font)
        self.label_pcr_bcd.setObjectName("label_pcr_bcd")
        self.label_testcount = QtWidgets.QLabel(self.tab_2)
        self.label_testcount.setGeometry(QtCore.QRect(30, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_testcount.setFont(font)
        self.label_testcount.setObjectName("label_testcount")
        self.label_path = QtWidgets.QLabel(self.tab_2)
        self.label_path.setGeometry(QtCore.QRect(30, 660, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_testcount = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_testcount.setGeometry(QtCore.QRect(210, 445, 51, 20))
        self.textBrowser_testcount.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_testcount.setObjectName("textBrowser_testcount")
        self.pushButton_smp_info_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_smp_info_2.setGeometry(QtCore.QRect(-1, 60, 325, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_smp_info_2.setFont(font)
        self.pushButton_smp_info_2.setStyleSheet("border-style: outset;\n"
                                                 "background-color: rgb(225, 225, 225);\n"
                                                 "border-width: 0px;\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pushButton_smp_info_2.setObjectName("pushButton_smp_info_2")
        self.pushButton_arrow_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_arrow_2.setGeometry(QtCore.QRect(315, 60, 16, 31))
        self.pushButton_arrow_2.setStyleSheet("image: url(:/newPrefix/pic_1.png);\n"
                                              "border-style: outset;\n"
                                              "border-width: 0px;\n"
                                              "border-color: black;\n"
                                              "padding: 1px;\n"
                                              "border-radius: 15px;\n"
                                              "")
        self.pushButton_arrow_2.setText("")
        self.pushButton_arrow_2.setObjectName("pushButton_arrow_2")
        self.pushButton_protocol_info_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_protocol_info_2.setGeometry(QtCore.QRect(324, 60, 360, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_protocol_info_2.setFont(font)
        self.pushButton_protocol_info_2.setStyleSheet("border-style: outset;\n"
                                                      "background-color: rgb(225, 225, 225);\n"
                                                      "border-width: 0px;\n"
                                                      "\n"
                                                      "\n"
                                                      "")
        self.pushButton_protocol_info_2.setObjectName("pushButton_protocol_info_2")
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setGeometry(QtCore.QRect(0, 85, 685, 8))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.pushButton_prev_1.raise_()
        self.label_protocol.raise_()
        self.listWidget_protocol.raise_()
        self.pushButton_run.raise_()
        self.pushButton_hidden.raise_()
        self.label_tube_type.raise_()
        self.radioButton_tube_1.raise_()
        self.radioButton_tube_2.raise_()
        self.label_cap_type.raise_()
        self.radioButton_cap_1.raise_()
        self.radioButton_cap_2.raise_()
        self.lineEdit_pcr_bcd.raise_()
        self.label_pcr_bcd.raise_()
        self.label_testcount.raise_()
        self.textBrowser_testcount.raise_()
        self.pushButton_smp_info_2.raise_()
        self.pushButton_protocol_info_2.raise_()
        self.line_6.raise_()
        self.pushButton_arrow_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_ctrl_seq = QtWidgets.QLabel(self.tab_3)
        self.label_ctrl_seq.setGeometry(QtCore.QRect(30, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ctrl_seq.setFont(font)
        self.label_ctrl_seq.setObjectName("label_ctrl_seq")

        self.label_plrn_path = QtWidgets.QLabel(self.tab_3)
        self.label_plrn_path.setGeometry(QtCore.QRect(30, 150, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_plrn_path.setFont(font)
        self.label_plrn_path.setObjectName("label_plrn_path")
        self.textBrowser_plrn_path = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_plrn_path.setGeometry(QtCore.QRect(230, 150, 320, 40))
        self.textBrowser_plrn_path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path.setObjectName("textBrowser_plrn_path")
        self.textBrowser_plrn_path.setText(plrn_path[0][0])
        self.toolButton_plrn_path = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_plrn_path.setGeometry(QtCore.QRect(554, 149, 28, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_plrn_path.setFont(font)
        self.toolButton_plrn_path.setStyleSheet("")
        self.toolButton_plrn_path.setObjectName("toolButton_plrn_path")

        self.label_add_path_2 = QtWidgets.QLabel(self.tab_3)
        self.label_add_path_2.setGeometry(QtCore.QRect(65, 209, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(75)
        self.label_add_path_2.setFont(font)
        self.label_add_path_2.setObjectName("add_path_2")
        self.add_path_2 = QtWidgets.QCheckBox(self.tab_3)
        self.add_path_2.setGeometry(QtCore.QRect(135, 205, 30, 30))

        if plrn_path[0][1] != "":
            self.add_path_2.setChecked(True)
        self.textBrowser_plrn_path_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_plrn_path_2.setGeometry(QtCore.QRect(230, 200, 320, 40))
        self.textBrowser_plrn_path_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path_2.setObjectName("textBrowser_plrn_path_2")
        self.textBrowser_plrn_path_2.setText(plrn_path[0][1])
        self.textBrowser_plrn_path_2.setEnabled(False)
        self.toolButton_plrn_path_2 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_plrn_path_2.setGeometry(QtCore.QRect(554, 199, 28, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_plrn_path_2.setFont(font)
        self.toolButton_plrn_path_2.setText("...")
        self.toolButton_plrn_path_2.setStyleSheet("")
        self.toolButton_plrn_path_2.setObjectName("toolButton_plrn_path_2")
        self.toolButton_plrn_path_2.setEnabled(False)
        if self.add_path_2.isChecked() == True:
            self.textBrowser_plrn_path_2.setEnabled(True)
            self.toolButton_plrn_path_2.setEnabled(True)

        self.label_add_path_3 = QtWidgets.QLabel(self.tab_3)
        self.label_add_path_3.setGeometry(QtCore.QRect(65, 259, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(75)
        self.label_add_path_3.setFont(font)
        self.label_add_path_3.setObjectName("add_path_3")
        self.add_path_3 = QtWidgets.QCheckBox(self.tab_3)
        self.add_path_3.setGeometry(QtCore.QRect(135, 255, 30, 30))
        if plrn_path[0][2] != "":
            self.add_path_3.setChecked(True)
        self.textBrowser_plrn_path_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_plrn_path_3.setGeometry(QtCore.QRect(230, 250, 320, 40))
        self.textBrowser_plrn_path_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_plrn_path_3.setObjectName("textBrowser_plrn_path_3")
        self.textBrowser_plrn_path_3.setText(plrn_path[0][2])
        self.textBrowser_plrn_path_3.setEnabled(False)
        self.toolButton_plrn_path_3 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_plrn_path_3.setGeometry(QtCore.QRect(554, 249, 28, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_plrn_path_3.setFont(font)
        self.toolButton_plrn_path_3.setText("...")
        self.toolButton_plrn_path_3.setStyleSheet("")
        self.toolButton_plrn_path_3.setObjectName("toolButton_plrn_path_3")
        self.toolButton_plrn_path_3.setEnabled(False)
        if self.add_path_3.isChecked() == True:
            self.textBrowser_plrn_path_3.setEnabled(True)
            self.toolButton_plrn_path_3.setEnabled(True)

        self.radioButton_ncpc = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_ncpc.setGeometry(QtCore.QRect(250, 92, 108, 19))
        self.radioButton_ncpc.setObjectName("radioButton_ncpc")
        self.radioButton_ncpc.setChecked(True)
        self.buttonGroup_4 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_ncpc)
        self.radioButton_pcnc = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_pcnc.setGeometry(QtCore.QRect(400, 92, 108, 19))
        self.radioButton_pcnc.setObjectName("radioButton_pcnc")
        self.buttonGroup_4.addButton(self.radioButton_pcnc)
        self.tabWidget.addTab(self.tab_3, "")
        self.label_worklist = QtWidgets.QLabel(self.Tab_1)
        self.label_worklist.setGeometry(QtCore.QRect(0, -7, 685, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_worklist.setFont(font)
        self.label_worklist.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_worklist.setObjectName("label_worklist")

        self.label_worklist_2 = QtWidgets.QLabel(self.tab_2)
        self.label_worklist_2.setGeometry(QtCore.QRect(0, -7, 685, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_worklist_2.setFont(font)
        self.label_worklist_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_worklist_2.setObjectName("label_worklist_2")

        self.label_worklist_3 = QtWidgets.QLabel(self.tab_3)
        self.label_worklist_3.setGeometry(QtCore.QRect(0, -7, 685, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_worklist_3.setFont(font)
        self.label_worklist_3.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_worklist_3.setObjectName("label_worklist_3")

        self.widget_bar = QtWidgets.QWidget(self)
        self.widget_bar.setGeometry(QtCore.QRect(0, 0, 100, 800))
        self.widget_bar.setStyleSheet("background-color: rgb(3, 56, 125);")
        self.widget_bar.setObjectName("widget_bar")
        self.pushButton_Home = QtWidgets.QPushButton(self.widget_bar)
        self.pushButton_Home.setGeometry(QtCore.QRect(0, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Home.setFont(font)
        self.pushButton_Home.setStyleSheet("background-color: rgb(0, 40, 93);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-width: 0px;\n"
                                           "border-color: rgb(15, 123, 255);\n"
                                           "")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_Option = QtWidgets.QPushButton(self.widget_bar)
        self.pushButton_Option.setGeometry(QtCore.QRect(0, 141, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Option.setFont(font)
        self.pushButton_Option.setStyleSheet("background-color: rgb(0, 40, 93);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-width: 0px;\n"
                                             "border-color: rgb(15, 123, 255);\n"
                                             "")
        self.pushButton_Option.setObjectName("pushButton_Option")
        self.line_1 = QtWidgets.QFrame(self.Tab_1)
        self.line_1.setGeometry(QtCore.QRect(0, 59, 685, 8))
        self.line_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_1.setLineWidth(1)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 59, 685, 8))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(0, 59, 685, 8))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Seegene WorkList"))
        self.toolButton_load.setText(_translate("MainWindow", "..."))
        self.toolButton_plrn_path.setText(_translate("MainWindow", "..."))
        self.pushButton_smp_ok.setText(_translate("MainWindow", "OK"))
        item = self.tableWidget_smp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "WorkList Barcode"))
        item_2 = self.tableWidget_smp.horizontalHeaderItem(1)
        item_2.setText(_translate("MainWindow", "Instrument Barcode"))
        item_3 = self.tableWidget_smp.horizontalHeaderItem(2)
        item_3.setText(_translate("MainWindow", "Check"))
        self.label_smp_count.setText(_translate("MainWindow", "Sample Count"))
        self.label_smp_bcd.setText(_translate("MainWindow", "Barcode"))
        self.pushButton_next_1.setText(_translate("MainWindow", "Next"))
        self.pushButton_prev_1.setText(_translate("MainWindow", "Prev"))
        self.pushButton_smp_info_1.setText(_translate("MainWindow", "Sample Information"))
        self.pushButton_protocol_info_1.setText(_translate("MainWindow", "Protocol Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_1), _translate("MainWindow", "Tab_1"))
        self.label_protocol.setText(_translate("MainWindow", "Protocol"))
        __sortingEnabled = self.listWidget_protocol.isSortingEnabled()
        self.listWidget_protocol.setSortingEnabled(False)
        item = self.listWidget_protocol.item(0)
        item.setText(_translate("MainWindow", "nCoV"))
        item = self.listWidget_protocol.item(1)
        item.setText(_translate("MainWindow", "RP1"))
        # item = self.listWidget_protocol.item(2)
        # item.setText(_translate("MainWindow", "HPV"))
        self.listWidget_protocol.setSortingEnabled(__sortingEnabled)
        self.pushButton_run.setText(_translate("MainWindow", "Make"))
        self.pushButton_hidden.setText(_translate("MainWindow", ""))
        self.label_tube_type.setText(_translate("MainWindow", "Tube/Plate Type"))
        self.radioButton_tube_1.setText(_translate("MainWindow", "Plate"))
        self.radioButton_tube_2.setText(_translate("MainWindow", "8 - Strip Tube"))
        self.label_cap_type.setText(_translate("MainWindow", "Cap Type"))
        self.radioButton_cap_1.setText(_translate("MainWindow", "Cap"))
        self.radioButton_cap_2.setText(_translate("MainWindow", "Film"))
        self.label_pcr_bcd.setText(_translate("MainWindow", "PCR Reagent Barcode"))
        self.label_testcount.setText(_translate("MainWindow", "Test Count"))
        self.textBrowser_testcount.setHtml(_translate("MainWindow",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_smp_info_2.setText(_translate("MainWindow", "Sample Information"))
        self.pushButton_protocol_info_2.setText(_translate("MainWindow", "Protocol Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab_2"))
        self.label_ctrl_seq.setText(_translate("MainWindow", "PCR Control sequence"))
        self.label_plrn_path.setText(_translate("MainWindow", "plrn File path"))
        self.label_add_path_2.setText(_translate("MainWindow", "add path"))
        self.label_add_path_3.setText(_translate("MainWindow", "add path"))
        self.radioButton_ncpc.setText(_translate("MainWindow", "NC, PC"))
        self.radioButton_pcnc.setText(_translate("MainWindow", "PC, NC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab_3"))
        self.label_worklist.setText(_translate("MainWindow", " Seegene WorkList"))
        self.label_worklist_2.setText(_translate("MainWindow", " Seegene WorkList"))
        self.label_worklist_3.setText(_translate("MainWindow", " Seegene WorkList"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        self.pushButton_Option.setText(_translate("MainWindow", "Option"))
        self.pushButton_copy.setText(_translate("MainWindow", "Copy(All)"))
        self.pushButton_reload.setText(_translate("MainWindow", "Reload"))

        # Instrument Barcode Setting, Style Sheet
        self.Bcd_list()
        self.tableWidget_smp.resizeColumnsToContents()
        self.tableWidget_smp.resizeRowsToContents()

        self.tableWidget_smp.setStyleSheet("color: black;"
                                           "font: 15px;"
                                           "padding: 1px;"
                                           "header: 10px;"
                                           )
        self.tableWidget_smp.setColumnWidth(0, 210)
        self.tableWidget_smp.setColumnWidth(1, 210)
        self.tableWidget_smp.setColumnWidth(2, 60)

        # 버튼
        self.pushButton_next_1.setEnabled(False)
        self.pushButton_next_1.clicked.connect(self.page_2)
        self.pushButton_prev_1.clicked.connect(self.page_1)
        
        self.pushButton_Option.clicked.connect(self.page_option)
        self.pushButton_Home.clicked.connect(self.page_home)
        self.lineEdit_smp_count.returnPressed.connect(self.Count_smp)
        self.pushButton_smp_ok.clicked.connect(self.Count_smp)
        self.toolButton_load.clicked.connect(self.Load_csv)
        self.lineEdit_smp_bcd.returnPressed.connect(self.BCD_smp)
        self.buttonGroup_2.buttonClicked.connect(self.Select_plate)
        self.buttonGroup_3.buttonClicked.connect(self.Select_cap)
        self.buttonGroup_4.buttonClicked.connect(self.Select_ctrl)
        self.toolButton_plrn_path.clicked.connect(lambda : self.plrn_path(1))
        self.pushButton_run.clicked.connect(self.Run)

        

        self.lineEdit_pcr_bcd.returnPressed.connect(self.display_test_count)
        self.lineEdit_pcr_bcd.returnPressed.connect(self.check_test_count)
        self.pushButton_reload.clicked.connect(self.Reload)
        self.pushButton_copy.clicked.connect(self.Copy)

        self.pushButton_hidden.clicked.connect(self.Hidden)

        self.add_path_2.clicked.connect(lambda : self.enable_path(2)) # add path 체크
        self.add_path_3.clicked.connect(lambda : self.enable_path(3))
        self.toolButton_plrn_path_2.clicked.connect(lambda : self.plrn_path(2)) # add dir
        self.toolButton_plrn_path_3.clicked.connect(lambda : self.plrn_path(3))


    # plrn path 추가
    def enable_path(self, i):
        if i == 2:
            if self.add_path_2.isChecked() == True:
                self.textBrowser_plrn_path_2.setEnabled(True)
                self.toolButton_plrn_path_2.setEnabled(True)
            elif self.add_path_2.isChecked() == False:
                self.textBrowser_plrn_path_2.setEnabled(False)
                self.toolButton_plrn_path_2.setEnabled(False)
                self.DB.set_dir("", 2)
        elif i == 3:
            if self.add_path_3.isChecked() == True:
                self.textBrowser_plrn_path_3.setEnabled(True)
                self.toolButton_plrn_path_3.setEnabled(True)
            elif self.add_path_3.isChecked() == False:
                self.textBrowser_plrn_path_3.setEnabled(False)
                self.toolButton_plrn_path_3.setEnabled(False)
                self.DB.set_dir("", 3)


    # Hidden 바코드
    def Hidden(self):
        QtWidgets.QMessageBox.information(self, "System", "Hidden Barcode!")
        self.lineEdit_pcr_bcd.setText("Hidden Barcode")
        self.textBrowser_testcount.setText("100")
        self.check_test_count()


    # 기본 setting값 설정
    def update_setting(self):
        protocol_name, plate_type, cap_type = self.DB.load_setting()
        count = self.listWidget_protocol.count()
        for i in range(count):
            if protocol_name == self.listWidget_protocol.item(i).text():
                self.listWidget_protocol.setCurrentRow(i)
                break
            # if i == count - 1: # 리스트에 없을 경우 생성
            #     self.listWidget_protocol.addItem()
        if plate_type == self.radioButton_tube_1.text():
            self.radioButton_tube_1.setChecked(True)
        else:
            self.radioButton_tube_2.setChecked(True)
            self.radioButton_cap_2.setEnabled(False)
        if cap_type == self.radioButton_cap_1.text():
            self.radioButton_cap_1.setChecked(True)
        else:
            self.radioButton_cap_2.setChecked(True)

    def page_1(self):
        self.tabWidget.setCurrentIndex(0)

    def page_2(self):
        self.tabWidget.setCurrentIndex(1)
        self.update_setting()

    def page_option(self):
        self.tabWidget.setCurrentIndex(2)

    def page_home(self):
        self.tabWidget.setCurrentIndex(0)

    # PCR 시약 잔량 표시
    def display_test_count(self):
        pcr_bcd = self.lineEdit_pcr_bcd.text()
        test_count = self.DB.PCR_test_count(pcr_bcd)
        self.textBrowser_testcount.setText(test_count)

    def check_test_count(self):
        test_count = self.textBrowser_testcount.toPlainText()
        smp_count = self.tableWidget_smp.rowCount()
        if int(test_count) < smp_count :
            QtWidgets.QMessageBox.information(self, "System", "The remaining amount of PCR Reagent is insufficient.\nPlease Replace PCR Reagent.")
            self.pushButton_run.setEnabled(False)
        else:
            self.pushButton_run.setEnabled(True)

    # 라디오버튼 Type(Plate, Cap, Control)
    def Select_plate(self):
        if self.buttonGroup_2.checkedButton().text() == "8 - Strip Tube":
            self.radioButton_cap_2.setEnabled(False)
            self.radioButton_cap_1.setChecked(True)
            self.cap_type = "Cap"
        else:
            self.radioButton_cap_2.setEnabled(True)
        self.plate_type = self.buttonGroup_2.checkedButton().text()

    def Select_cap(self):
        self.cap_type = self.buttonGroup_3.checkedButton().text()

    def Select_ctrl(self):
        self.ctrl_seq = self.buttonGroup_4.checkedButton().text()


    # plrn 파일 경로 설정
    def plrn_path(self, i):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory()
        if i == 1:
            self.textBrowser_plrn_path.setText(dir_path)
            self.DB.set_dir(dir_path, 1)
        elif i == 2:
            self.textBrowser_plrn_path_2.setText(dir_path)
            self.DB.set_dir(dir_path, 2)
        elif i == 3:
            self.textBrowser_plrn_path_3.setText(dir_path)
            self.DB.set_dir(dir_path, 3)


    # 샘플 개수 OK
    def Count_smp(self):
        count = self.lineEdit_smp_count.text()
        Ui_MainWindow.bcd_count = count
        try:
            if int(count) < 1:
                QtWidgets.QMessageBox.information(self, "System", "Please Enter a Number of 1 or more.")
                self.lineEdit_smp_count.setText("")
            elif 0 < int(count) < 95:
                self.tableWidget_smp.setRowCount(int(count))
                for i in range(int(count)):
                    self.tableWidget_smp.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            elif 94 < int(count):
                QtWidgets.QMessageBox.information(self, "System", "The Maximum Number of Samples is 94.")
                self.lineEdit_smp_count.setText("")
            self.smp_count_1 = self.tableWidget_smp.rowCount()
            self.smp_count_2 = self.tableWidget_smp.rowCount()
        except:
            self.lineEdit_smp_count.setText("")
        self.Reload()

    # Load WorkList
    def Load_csv(self):
        csv_header = []
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'csv File(*.csv);; csv File(*.csv)')
        if fname[0]:
            csv_file = pd.read_csv(fname[0], encoding='CP949')
            rdr = csv.reader(csv_file)
            for line in rdr:
                csv_header.append(line)           
            load_bcd = csv_file['Barcode']
            bcd_val = load_bcd.values.tolist()
            self.tableWidget_smp.setRowCount(len(bcd_val))
            self.lineEdit_smp_count.setText(str(len(bcd_val)))
            for i in range(len(bcd_val)):
                self.tableWidget_smp.setItem(i, 0, QtWidgets.QTableWidgetItem(str(bcd_val[i])))
            Ui_MainWindow.temp_bcd_list = bcd_val
            self.smp_count_1 = self.tableWidget_smp.rowCount()
            self.smp_count_2 = self.tableWidget_smp.rowCount()
        else:
            QtWidgets.QMessageBox.information(self, "System", "No File selected.")
        self.Reload()


    # 샘플 바코드 입력
    def BCD_smp(self):
        if self.smp_count_1 > 0:
            bcd = self.lineEdit_smp_bcd.text()
            self.tableWidget_smp.setItem(self.smp_count_2 - self.smp_count_1, 0, QtWidgets.QTableWidgetItem(bcd))
            self.smp_count_1 -= 1
            self.lineEdit_smp_bcd.clear()
        else:
            self.lineEdit_smp_bcd.clear()

    # Run 버튼(DB에 정보 입력, plrn 생성)
    def Run(self):
        test_count = self.textBrowser_testcount.toPlainText()
        smp_count = self.tableWidget_smp.rowCount()
        count = int(test_count) - smp_count
        if self.listWidget_protocol.currentItem().text() != "" and self.lineEdit_pcr_bcd.text() != "" and count >= 0:
            smp_bcd = []
            date = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
            Protocol_Name = self.listWidget_protocol.currentItem().text()
            rowCount = self.tableWidget_smp.rowCount()
            pcr_bcd = self.lineEdit_pcr_bcd.text()
            for i in range(rowCount):
                smp_bcd.append(self.tableWidget_smp.item(i, 0).text())

            id_plrn = self.DB.Input_plrn_data(date, Protocol_Name, rowCount, self.plate_type, self.cap_type, self.ctrl_seq, pcr_bcd)
            self.DB.Input_sample_data(smp_bcd, id_plrn)
            self.DB.Use_PCR(pcr_bcd, rowCount)
            self.DB.make_plrn(id_plrn)
            self.DB.save_Temp(Protocol_Name, self.plate_type, self.cap_type)
            self.textBrowser_testcount.setText(str(count))

        elif self.listWidget_protocol.currentItem().text() == "" or self.lineEdit_pcr_bcd.text() == "":
            QtWidgets.QMessageBox.information(self, "System", "Please Enter all Protocol Information.")
            self.pushButton_run.setEnabled(False)

        elif count < 0 :
            QtWidgets.QMessageBox.information(self, "System", "The remaining amount of PCR Reagent is insufficient.\nPlease Replace PCR Reagent.")
            self.pushButton_run.setEnabled(False)

        self.close()

    # 초기 바코드 리스트 불러오기
    def Bcd_list(self):
        Ui_MainWindow.bcd_list = []
        Ui_MainWindow.temp_bcd_list = []

        temp = self.DB.Sel_Bcd()
        file = open(temp[0][0], "r", encoding="utf8")
        # 현재 비교할 텍스트 파일
        lines = file.readlines()  # list 형태로 읽어옴
        lines.pop(0)
        cnt = 0
        count = []
        background = []

        self.tableWidget_smp.setRowCount(len(lines))

        for i in range(len(lines)):
            Ui_MainWindow.bcd_list.append("")

        for line in lines:
            if not line:
                break

            temp3 = lines[cnt].split()

            if temp3[2] == Ui_MainWindow.bcd_list[cnt]:
                count.append("O")

            elif temp3[2] != Ui_MainWindow.bcd_list[cnt]:
                count.append("X")
                background.append(cnt)

            self.tableWidget_smp.setItem(cnt, 1, QtWidgets.QTableWidgetItem(str(temp3[2])))
            self.tableWidget_smp.setItem(cnt, 2, QtWidgets.QTableWidgetItem(str(count[cnt])))
            self.tableWidget_smp.setRowHeight(cnt, 60)
            cnt += 1

        file.close()

        for i in range(len(background)):
            self.tableWidget_smp.item(background[i], 1).setBackground(QtGui.QColor(255, 208, 208))
            self.tableWidget_smp.item(background[i], 2).setBackground(QtGui.QColor(255, 208, 208))

    # 바코드 갱신기능
    def Reload(self):
        temp = self.DB.Sel_Bcd()
        file = open(temp[0][0], "r", encoding="utf8")
        # 현재 비교할 텍스트 파일
        lines = file.readlines()  # list 형태로 읽어옴
        lines.pop(0)
        cnt = 0
        check = 0
        count = []
        background = []
        Ui_MainWindow.temp_bcd_list = []
        try:
            if len(lines) > int(self.lineEdit_smp_count.text()):
                self.tableWidget_smp.setRowCount(int(self.lineEdit_smp_count.text()))
            else:
                self.tableWidget_smp.setRowCount(len(lines))

            if len(lines) == int(self.lineEdit_smp_count.text()):
                for i in range(0, int(self.lineEdit_smp_count.text())):
                    Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())
            elif len(lines) < int(self.lineEdit_smp_count.text()):
                for i in range(len(lines)):
                    Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())
            elif len(lines) > int(self.lineEdit_smp_count.text()):
                for i in range(0, int(self.lineEdit_smp_count.text())):
                    Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())
        except Exception as err:
            print(err)

        try:
            for line in lines:
                if not line:
                    break
                if len(lines) > int(self.lineEdit_smp_count.text()):
                    break

                temp3 = lines[cnt].split()

                if temp3[2] == Ui_MainWindow.temp_bcd_list[cnt]:

                    print("{0}번째 해당 줄이 같습니다.".format(cnt))
                    print(temp3[2])
                    count.append("O")

                elif temp3[2] != Ui_MainWindow.temp_bcd_list[cnt]:
                    print("{0}번째 해당 줄이 다릅니다.".format(2))
                    print("1번 리스트 : " + temp3[2])
                    print("2번 리스트 : " + Ui_MainWindow.temp_bcd_list[cnt])
                    count.append("X")
                    background.append(cnt)

                self.tableWidget_smp.setItem(cnt, 0, QtWidgets.QTableWidgetItem(str(Ui_MainWindow.temp_bcd_list[cnt])))
                self.tableWidget_smp.setItem(cnt, 1, QtWidgets.QTableWidgetItem(str(temp3[2])))
                self.tableWidget_smp.setItem(cnt, 2, QtWidgets.QTableWidgetItem(str(count[cnt])))

                cnt += 1

            if len(lines) <= int(self.lineEdit_smp_count.text()):
                for i in range(len(lines)):
                    Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())

            elif len(lines) > int(self.lineEdit_smp_count.text()):
                for i in range(len(Ui_MainWindow.temp_bcd_list)):
                    Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())

            for i in range(len(background)):
                self.tableWidget_smp.item(background[i], 0).setBackground(QtGui.QColor(255, 208, 208))
                self.tableWidget_smp.item(background[i], 1).setBackground(QtGui.QColor(255, 208, 208))
                self.tableWidget_smp.item(background[i], 2).setBackground(QtGui.QColor(255, 208, 208))
        except Exception as err:
            print(err)

        try:
            if len(lines) > int(self.lineEdit_smp_count.text()):
                cnt = 0
                for line in lines:
                    if cnt == int(self.lineEdit_smp_count.text()):
                        break
                    temp3 = lines[cnt].split()

                    if temp3[2] == Ui_MainWindow.temp_bcd_list[cnt]:

                        print("{0}번째 해당 줄이 같습니다.".format(cnt))
                        print(temp3[2])
                        count.append("O")

                    elif temp3[2] != Ui_MainWindow.temp_bcd_list[cnt]:
                        print("{0}번째 해당 줄이 다릅니다.".format(2))
                        print("1번 리스트 : " + temp3[2])
                        print("2번 리스트 : " + Ui_MainWindow.temp_bcd_list[cnt])
                        count.append("X")
                        background.append(cnt)

                    self.tableWidget_smp.setItem(cnt, 0, QtWidgets.QTableWidgetItem(str(Ui_MainWindow.temp_bcd_list[cnt])))
                    self.tableWidget_smp.setItem(cnt, 1, QtWidgets.QTableWidgetItem(str(temp3[2])))
                    self.tableWidget_smp.setItem(cnt, 2, QtWidgets.QTableWidgetItem(str(count[cnt])))

                    cnt += 1

                if len(lines) <= int(self.lineEdit_smp_count.text()):
                    for i in range(len(lines)):
                        Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())

                elif len(lines) > int(self.lineEdit_smp_count.text()):
                    for i in range(int(self.lineEdit_smp_count.text())):
                        Ui_MainWindow.temp_bcd_list.append((self.tableWidget_smp.item(i, 0)).text())

                for i in range(len(background)):
                    self.tableWidget_smp.item(background[i], 0).setBackground(QtGui.QColor(255, 208, 208))
                    self.tableWidget_smp.item(background[i], 1).setBackground(QtGui.QColor(255, 208, 208))
                    self.tableWidget_smp.item(background[i], 2).setBackground(QtGui.QColor(255, 208, 208))
        except Exception as err:
            print(err)

        if len(background) == 0:
            check = 1

        if check == 1:
            self.pushButton_next_1.setEnabled(True)
        else:
            self.pushButton_next_1.setEnabled(False)
        file.close()

    # 바코드리스트 Copy기능
    def Copy(self):
        temp = self.DB.Sel_Bcd()
        self.pushButton_next_1.setEnabled(True)
        file = open(temp[0][0], "r", encoding="utf8")
        # 현재 비교할 텍스트 파일
        lines = file.readlines()  # list 형태로 읽어옴
        Ui_MainWindow.bcd_list = lines
        cnt = 0
        count = []
        lines.pop(0)

        self.tableWidget_smp.setRowCount(len(lines))

        for line in lines:
            if not line:
                break
            temp3 = lines[cnt].split()
            temp4 = Ui_MainWindow.bcd_list[cnt].split()

            if temp3[2] == temp4[2]:
                count.append("O")

            elif temp3[2] == temp4[2]:
                count.append("X")

            self.tableWidget_smp.setItem(cnt, 0, QtWidgets.QTableWidgetItem(str(temp3[2])))
            self.tableWidget_smp.setItem(cnt, 1, QtWidgets.QTableWidgetItem(str(temp3[2])))
            self.tableWidget_smp.setItem(cnt, 2, QtWidgets.QTableWidgetItem(str(count[cnt])))
            cnt += 1

        file.close()

        self.tableWidget_smp.setRowCount(len(lines))
