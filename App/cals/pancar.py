# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

sys.path.append("..")
import res_rc
from PyQt6 import QtCore, QtGui, QtWidgets
from graphs import EngineDataGraph
import sys
from engine import Motor
from utils import kmh_to_ms
import shelve
import webbrowser
from calculations import (
    overall_resist_forces,
    cs_overall_resist_forces,
    tractive_f,
    final_force,
)
from gearbox_new import GearBox_Ui_Dialog
from vehicle_new import Vehicle_Ui_Dialog
from env_new import Env_Ui_Dialog


class Ui_VehicleDynamicsApp(object):
    def setupUi(self, VehicleDynamicsApp):
        VehicleDynamicsApp.setObjectName("VehicleDynamicsApp")
        VehicleDynamicsApp.resize(880, 550)
        VehicleDynamicsApp.setMinimumSize(QtCore.QSize(880, 550))
        VehicleDynamicsApp.setMaximumSize(QtCore.QSize(880, 550))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        font.setItalic(False)
        font.setKerning(True)
        VehicleDynamicsApp.setFont(font)
        VehicleDynamicsApp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        VehicleDynamicsApp.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/img/assets/dark-car-from-side-vector-9761198.jpg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        VehicleDynamicsApp.setWindowIcon(icon)
        VehicleDynamicsApp.setToolTipDuration(-1)
        VehicleDynamicsApp.setStyleSheet(
            'font: 350 9pt "Bahnschrift SemiLight";\n'
            "background-color: rgb(22,22,22);\n"
            "color:rgb(255,255,255);"
        )
        VehicleDynamicsApp.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(VehicleDynamicsApp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 881, 491))
        self.label.setStyleSheet(
            "background-color: rgb(30, 30, 30);\n" "background-color: rgb(5,5,5);"
        )
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(410, 10, 461, 471))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 441, 16))
        self.progressBar.setStyleSheet(
            "color:rgb(0,0,0);\n"
            "background-color: rgb(198, 198, 198);\n"
            "gridline-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            ""
        )
        self.progressBar.setProperty("value", 25)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 340, 441, 121))
        self.groupBox.setMinimumSize(QtCore.QSize(1, 1))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(
            "color:rgb(170, 0, 0);\n" 'font: 700 italic 9pt "Segoe UI";'
        )
        self.groupBox.setObjectName("groupBox")
        ##################################################################################################################
        self.torque_rpm = QtWidgets.QPushButton(self.groupBox)
        self.torque_rpm.setGeometry(QtCore.QRect(10, 30, 134, 34))
        self.torque_rpm.setMinimumSize(QtCore.QSize(1, 1))
        self.torque_rpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.torque_rpm.setStyleSheet(
            "QPushButton{\n"
            "border-radius:5px;\n"
            "color:rgb(239, 239, 239);\n"
            'font: 10pt "Gill Sans MT";\n'
            "background-color: rgb(9, 9, 9);\n"
            "}\n"
            "QPushButton:hover {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color:rgb(239, 239, 239);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color: rgb(0, 85, 0);\n"
            "}"
        )
        self.torque_rpm.setObjectName("torque_rpm")
        self.torque_rpm.clicked.connect(self.func_torque_rpm)
        ##################################################################################################################
        self.rpm_v = QtWidgets.QPushButton(self.groupBox)
        self.rpm_v.setGeometry(QtCore.QRect(290, 30, 141, 34))
        self.rpm_v.setMinimumSize(QtCore.QSize(1, 1))
        self.rpm_v.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rpm_v.setStyleSheet(
            "QPushButton{\n"
            "border-radius:5px;\n"
            "color:rgb(239, 239, 239);\n"
            'font: 10pt "Gill Sans MT";\n'
            "background-color: rgb(9, 9, 9);\n"
            "}\n"
            "QPushButton:hover {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color:rgb(239, 239, 239);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color: rgb(0, 85, 0);\n"
            "}"
        )
        self.rpm_v.setIconSize(QtCore.QSize(16, 20))
        self.rpm_v.setObjectName("rpm_v")

        self.rpm_v.clicked.connect(self.func_rpm_v)
        ##################################################################################################################
        self.torque_rpm_power = QtWidgets.QPushButton(self.groupBox)
        self.torque_rpm_power.setEnabled(True)
        self.torque_rpm_power.setGeometry(QtCore.QRect(150, 30, 134, 34))
        self.torque_rpm_power.setMinimumSize(QtCore.QSize(1, 1))
        self.torque_rpm_power.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.torque_rpm_power.setStyleSheet(
            "QPushButton{\n"
            "border-radius:5px;\n"
            "color:rgb(239, 239, 239);\n"
            'font: 10pt "Gill Sans MT";\n'
            "background-color: rgb(9, 9, 9);\n"
            "}\n"
            "QPushButton:hover {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color:rgb(239, 239, 239);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color: rgb(0, 85, 0);\n"
            "}"
        )
        self.torque_rpm_power.setObjectName("torque_rpm_power")
        self.torque_rpm_power.clicked.connect(self.func_torque_rpm_power)
        ##################################################################################################################
        self.F_v = QtWidgets.QPushButton(self.groupBox)
        self.F_v.setGeometry(QtCore.QRect(10, 70, 201, 34))
        self.F_v.setMinimumSize(QtCore.QSize(1, 1))
        self.F_v.setMaximumSize(QtCore.QSize(16777215, 40))
        self.F_v.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.F_v.setStyleSheet(
            "QPushButton{\n"
            "border-radius:5px;\n"
            "color:rgb(239, 239, 239);\n"
            'font: 10pt "Gill Sans MT";\n'
            "background-color: rgb(9, 9, 9);\n"
            "}\n"
            "QPushButton:hover {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color:rgb(239, 239, 239);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color: rgb(0, 85, 0);\n"
            "}"
        )
        self.F_v.setObjectName("F_v")
        self.F_v.clicked.connect(self.func_f_v)
        ##################################################################################################################
        self.Fnet_v = QtWidgets.QPushButton(self.groupBox)
        self.Fnet_v.setGeometry(QtCore.QRect(220, 70, 211, 34))
        self.Fnet_v.setMinimumSize(QtCore.QSize(1, 1))
        self.Fnet_v.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Fnet_v.setStyleSheet(
            "QPushButton{\n"
            "border-radius:5px;\n"
            "color:rgb(239, 239, 239);\n"
            'font: 10pt "Gill Sans MT";\n'
            "background-color: rgb(9, 9, 9);\n"
            "}\n"
            "QPushButton:hover {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color:rgb(239, 239, 239);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "color:rgb(9, 9, 9);\n"
            "background-color: rgb(0, 85, 0);\n"
            "}"
        )
        self.Fnet_v.setObjectName("Fnet_v")
        self.Fnet_v.clicked.connect(self.func_fnet_v)
        ##################################################################################################################
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 441, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.torque_rpm_list = QtWidgets.QListWidget(self.layoutWidget)
        self.torque_rpm_list.setStyleSheet(
            "background-color: rgb(76, 76, 76);\n"
            'font: 10pt "Segoe UI";\n'
            "alternate-background-color: rgb(85, 0, 0);\n"
            "selection-color: rgb(85, 0, 0);\n"
            "gridline-color: rgb(85, 0, 0);\n"
            "selection-background-color: rgba(85, 0, 0,0.1);\n"
            ""
        )
        self.torque_rpm_list.setObjectName("torque_rpm_list")
        db = shelve.open("engines.db")
        dkeys = list(db.keys())
        dkeys.sort()
        self.torque_rpm_list.addItems([x for x in dkeys])
        self.torque_rpm.repaint()
        QtCore.QCoreApplication.processEvents()
        self.verticalLayout.addWidget(self.torque_rpm_list)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet(
            'font: 700 7pt "Segoe UI";\n' "color:rgb(210,210,210);"
        )
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gearbox_list = QtWidgets.QListWidget(self.layoutWidget)
        self.gearbox_list.setStyleSheet(
            "background-color: rgb(76, 76, 76);\n"
            'font: 10pt "Segoe UI";\n'
            "alternate-background-color: rgb(85, 0, 0);\n"
            "selection-color: rgb(85, 0, 0);\n"
            "gridline-color: rgb(85, 0, 0);\n"
            "selection-background-color: rgba(85, 0, 0,0.1);\n"
            ""
        )
        self.gearbox_list.setObjectName("gearbox_list")
        db = shelve.open("gearboxes.db")
        dkeys = list(db.keys())
        dkeys.sort()
        self.gearbox_list.addItems([x for x in dkeys])
        self.verticalLayout_3.addWidget(self.gearbox_list)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet(
            'font: 700 7pt "Segoe UI";\n' "color:rgb(210,210,210);"
        )
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 178, 439, 142))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.car_param = QtWidgets.QListWidget(self.layoutWidget1)
        self.car_param.setStyleSheet(
            "background-color: rgb(76, 76, 76);\n"
            'font: 10pt "Segoe UI";\n'
            "alternate-background-color: rgb(85, 0, 0);\n"
            "selection-color: rgb(85, 0, 0);\n"
            "gridline-color: rgb(85, 0, 0);\n"
            "selection-background-color: rgba(85, 0, 0,0.1);\n"
            ""
        )
        self.car_param.setObjectName("car_param")
        db = shelve.open("vehicles.db")
        dkeys = list(db.keys())
        dkeys.sort()
        self.car_param.addItems([x for x in dkeys])
        self.verticalLayout_4.addWidget(self.car_param)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(
            'font: 700 7pt "Segoe UI";\n' "color:rgb(210,210,210);"
        )
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.env_param = QtWidgets.QListWidget(self.layoutWidget1)
        self.env_param.setStyleSheet(
            "background-color: rgb(76, 76, 76);\n"
            'font: 10pt "Segoe UI";\n'
            "alternate-background-color: rgb(85, 0, 0);\n"
            "selection-color: rgb(85, 0, 0);\n"
            "gridline-color: rgb(85, 0, 0);\n"
            "selection-background-color: rgba(85, 0, 0,0.1);\n"
            ""
        )
        self.env_param.setObjectName("env_param")
        db = shelve.open("environments.db")
        dkeys = list(db.keys())
        dkeys.sort()
        self.env_param.addItems([x for x in dkeys])
        self.verticalLayout_5.addWidget(self.env_param)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setStyleSheet(
            'font: 700 7pt "Segoe UI";\n' "color:rgb(210,210,210);"
        )
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 391, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 391, 271))
        self.label_2.setStyleSheet(
            "background-image: url(:/img/assets/dark-car-from-side-vector-9761198.jpg);\n"
            "border-radius:25px;"
        )
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap(":/img/assets/dark-car-from-side-vector-9761198.jpg")
        )
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 369, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(90, 30, 67, 25))
        self.label_5.setObjectName("label_5")
        self.user_info = QtWidgets.QLineEdit(self.groupBox_3)
        self.user_info.setGeometry(QtCore.QRect(170, 30, 161, 25))
        self.user_info.setMinimumSize(QtCore.QSize(1, 1))
        self.user_info.setStyleSheet(
            "color:rgb(0,0,0);\n" "background-color: rgb(168, 168, 168);"
        )
        self.user_info.setObjectName("user_info")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 369, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.vehicle_brand = QtWidgets.QLineEdit(self.groupBox_2)
        self.vehicle_brand.setGeometry(QtCore.QRect(170, 30, 161, 25))
        self.vehicle_brand.setMinimumSize(QtCore.QSize(1, 20))
        self.vehicle_brand.setStyleSheet(
            "color:rgb(0,0,0);\n" "background-color: rgb(168, 168, 168);"
        )
        self.vehicle_brand.setText("")
        self.vehicle_brand.setObjectName("vehicle_brand")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 62, 25))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 112, 25))
        self.label_3.setObjectName("label_3")
        self.engine_brand = QtWidgets.QLineEdit(self.groupBox_2)
        self.engine_brand.setEnabled(True)
        self.engine_brand.setGeometry(QtCore.QRect(170, 60, 161, 25))
        self.engine_brand.setMinimumSize(QtCore.QSize(1, 1))
        self.engine_brand.setStyleSheet(
            "color:rgb(0,0,0);\n" "background-color: rgb(168, 168, 168);"
        )
        self.engine_brand.setDragEnabled(False)
        self.engine_brand.setClearButtonEnabled(False)
        self.engine_brand.setObjectName("engine_brand")
        VehicleDynamicsApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VehicleDynamicsApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 34))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuHakk_nda = QtWidgets.QMenu(self.menubar)
        self.menuHakk_nda.setObjectName("menuHakk_nda")
        VehicleDynamicsApp.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(VehicleDynamicsApp)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        font.setItalic(False)
        font.setKerning(True)
        self.toolBar.setFont(font)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setToolTip("")
        self.toolBar.setStatusTip("")
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setObjectName("toolBar")
        VehicleDynamicsApp.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionKapat = QtWidgets.QAction(VehicleDynamicsApp)
        font = QtGui.QFont()
        self.actionKapat.setFont(font)
        self.actionKapat.setObjectName("actionKapat")
        self.actionProgram_Kaynaklar = QtWidgets.QAction(VehicleDynamicsApp)
        font = QtGui.QFont()
        self.actionProgram_Kaynaklar.setFont(font)
        self.actionProgram_Kaynaklar.setObjectName("actionProgram_Kaynaklar")
        self.actionProgram_Kaynaklar.triggered.connect(self.about)
        self.car_entry = QtWidgets.QAction(VehicleDynamicsApp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/img/assets/vehicle.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.car_entry.setIcon(icon1)
        self.car_entry.setMenuRole(QtWidgets.QAction.NoRole)
        self.car_entry.setObjectName("car_entry")
        self.gearbox_entry = QtWidgets.QAction(VehicleDynamicsApp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/img/assets/gearbox2.jpg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.gearbox_entry.setIcon(icon2)
        self.gearbox_entry.setMenuRole(QtWidgets.QAction.NoRole)
        self.gearbox_entry.setObjectName("gearbox_entry")
        self.environment_entry = QtWidgets.QAction(VehicleDynamicsApp)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/img/assets/road.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.environment_entry.setIcon(icon3)
        self.environment_entry.setMenuRole(QtWidgets.QAction.NoRole)
        self.environment_entry.setObjectName("environment_entry")
        self.engine_entry = QtWidgets.QAction(VehicleDynamicsApp)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/img/assets/engine.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.engine_entry.setIcon(icon4)
        self.engine_entry.setMenuRole(QtWidgets.QAction.NoRole)
        self.engine_entry.setObjectName("engine_entry")
        self.actionDosyaya_Aktar = QtWidgets.QAction(VehicleDynamicsApp)
        self.actionDosyaya_Aktar.setObjectName("actionDosyaya_Aktar")
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionDosyaya_Aktar)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionKapat)
        self.menuHakk_nda.addAction(self.actionProgram_Kaynaklar)
        self.menuHakk_nda.addSeparator()
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuHakk_nda.menuAction())
        self.toolBar.addAction(self.engine_entry)
        self.toolBar.addAction(self.gearbox_entry)
        self.toolBar.addAction(self.car_entry)
        self.toolBar.addAction(self.environment_entry)
        self.toolBar.addSeparator()
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(VehicleDynamicsApp)
        self.actionKapat.triggered.connect(VehicleDynamicsApp.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(VehicleDynamicsApp)
        VehicleDynamicsApp.setTabOrder(self.vehicle_brand, self.engine_brand)
        VehicleDynamicsApp.setTabOrder(self.engine_brand, self.user_info)
        VehicleDynamicsApp.setTabOrder(self.user_info, self.torque_rpm_list)
        VehicleDynamicsApp.setTabOrder(self.torque_rpm_list, self.gearbox_list)
        VehicleDynamicsApp.setTabOrder(self.gearbox_list, self.car_param)
        VehicleDynamicsApp.setTabOrder(self.car_param, self.env_param)
        VehicleDynamicsApp.setTabOrder(self.env_param, self.torque_rpm)
        VehicleDynamicsApp.setTabOrder(self.torque_rpm, self.torque_rpm_power)
        VehicleDynamicsApp.setTabOrder(self.torque_rpm_power, self.rpm_v)
        VehicleDynamicsApp.setTabOrder(self.rpm_v, self.F_v)
        VehicleDynamicsApp.setTabOrder(self.F_v, self.Fnet_v)

    def retranslateUi(self, VehicleDynamicsApp):
        _translate = QtCore.QCoreApplication.translate
        VehicleDynamicsApp.setWindowTitle(
            _translate("VehicleDynamicsApp", "Pancar V1.0")
        )
        self.groupBox.setTitle(
            _translate("VehicleDynamicsApp", "Araç Performans Grafikleri")
        )
        self.torque_rpm.setText(_translate("VehicleDynamicsApp", "Motor tork-devir"))
        self.rpm_v.setText(_translate("VehicleDynamicsApp", "Araç devir-hız"))
        self.torque_rpm_power.setText(
            _translate("VehicleDynamicsApp", "Motor tork-devir-güç")
        )
        self.F_v.setText(_translate("VehicleDynamicsApp", "Çekiş gücü-hız (F araç)"))
        self.Fnet_v.setText(_translate("VehicleDynamicsApp", "Çekiş gücü-hız (F net)"))
        ################################################################################################
        __sortingEnabled = self.torque_rpm_list.isSortingEnabled()
        self.torque_rpm_list.setSortingEnabled(False)
        self.torque_rpm_list.setSortingEnabled(__sortingEnabled)
        ###################################################################################
        self.label_6.setText(_translate("VehicleDynamicsApp", "Tork-Devir Listesi"))
        ##################################################################################################
        __sortingEnabled = self.gearbox_list.isSortingEnabled()
        self.gearbox_list.setSortingEnabled(False)
        item = self.gearbox_list.item(0)
        item.setText(
            _translate("VehicleDynamicsApp", "Toyota supra 5 ileri vites kutusu")
        )
        item = self.gearbox_list.item(1)
        item.setText(_translate("VehicleDynamicsApp", "Nissan GTR 6 ileri vites kutus"))
        self.gearbox_list.setSortingEnabled(__sortingEnabled)
        ####################################################################################
        self.label_7.setText(_translate("VehicleDynamicsApp", "Şanzıman Parametreleri"))
        ##################################################################################################
        __sortingEnabled = self.car_param.isSortingEnabled()
        self.car_param.setSortingEnabled(False)
        item = self.car_param.item(0)
        item.setText(_translate("VehicleDynamicsApp", "Toyota Supra "))
        item = self.car_param.item(1)
        item.setText(_translate("VehicleDynamicsApp", "Nissan GTR R34"))
        self.car_param.setSortingEnabled(__sortingEnabled)
        ####################################################################################

        self.label_8.setText(_translate("VehicleDynamicsApp", "Araç Parametreleri"))
        ##################################################################################################
        __sortingEnabled = self.env_param.isSortingEnabled()
        self.env_param.setSortingEnabled(False)
        item = self.env_param.item(0)
        item.setText(_translate("VehicleDynamicsApp", "Analiz 1"))
        item = self.env_param.item(1)
        item.setText(_translate("VehicleDynamicsApp", "Yüksek Eğim"))
        self.env_param.setSortingEnabled(__sortingEnabled)
        ####################################################################################
        self.label_9.setText(
            _translate("VehicleDynamicsApp", "Çevre Koşulları parametreleri")
        )
        self.groupBox_3.setTitle(
            _translate("VehicleDynamicsApp", "Kullanıcı Bilgileri")
        )
        self.label_5.setText(_translate("VehicleDynamicsApp", "İsim Soyisim"))
        self.groupBox_2.setTitle(_translate("VehicleDynamicsApp", "Araç Bilgileri"))
        self.label_4.setText(_translate("VehicleDynamicsApp", "Araç Modeli"))
        self.label_3.setText(_translate("VehicleDynamicsApp", "Motor ismi/numarası"))
        self.menuDosya.setTitle(_translate("VehicleDynamicsApp", "Dosya"))
        self.menuHakk_nda.setTitle(_translate("VehicleDynamicsApp", "Hakkında"))
        self.toolBar.setWindowTitle(_translate("VehicleDynamicsApp", "toolBar"))
        self.actionKapat.setText(_translate("VehicleDynamicsApp", "Kapat"))
        self.actionProgram_Kaynaklar.setText(
            _translate("VehicleDynamicsApp", "Program Kaynakları")
        )
        self.car_entry.setText(_translate("VehicleDynamicsApp", "Araç"))
        self.car_entry.triggered.connect(self.vehicle)
        self.gearbox_entry.setText(_translate("VehicleDynamicsApp", "Dişli Kutusu"))
        self.gearbox_entry.triggered.connect(self.gearbox)
        self.environment_entry.setText(_translate("VehicleDynamicsApp", "Çevre"))
        self.environment_entry.triggered.connect(self.environment)
        self.engine_entry.setText(_translate("VehicleDynamicsApp", "Motor tork-rpm"))
        self.engine_entry.triggered.connect(self.engine)
        self.actionDosyaya_Aktar.setText(
            _translate("VehicleDynamicsApp", "Dosyaya Aktar")
        )

    def about(self):
        url = "https://github.com/eraycancelik/vehicle_dynamics"
        webbrowser.open(url)
        print("triggered")

    def func_rpm_v(self):
        arac_graph.rpm_v_graph(  # viteslere göre motor hızı vs araç hızı grafiği
            list=arac_v_list,
            rpm=engine_db[arac_rpm_name],
        )

    def func_torque_rpm(self):
        arac_graph.torque_rpm_graph()  # araç tork vs rpm grafiği

    def func_torque_rpm_power(self):
        arac_graph.plot_torque_rpm_hp_graph()  # araç tork vs rpm,güç grafiği

    def func_fnet_v(self):
        arac_graph.cs_final_tractive_force_vs_vehicle_speed(
            f_list=final_force(
                resist_f=cs_resist_forces,
                tractive_f=tractive_f(
                    tork_list=tork_times_gear_list,
                    r_w=arac.tekerlek_yaricap,
                    t_efficiency=arac.ao_verimi,
                ),
            ),
            hiz_list=arac_v_list,
        )

    def func_f_v(self):
        arac_graph.only_tractive_effort_vs_vehicle_speed(
            tractive_f_list=tractive_f(
                tork_list=tork_times_gear_list,
                r_w=arac.tekerlek_yaricap,
                t_efficiency=arac.ao_verimi,
            ),
            hiz_list=arac_v_list,
        )

    def engine(self):
        pass

    def vehicle(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Vehicle_Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def environment(self):
        Dialog = QtWidgets.QDialog()
        ui = Env_Ui_Dialog()
        ui.setupUi(Dialog)
        self.Dialog.show()

    def gearbox(self):
        Dialog = QtWidgets.QDialog()
        ui = GearBox_Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()


if __name__ == "__main__":
    import sys
    from engine import Motor
    from utils import kmh_to_ms
    import shelve
    from graphs import EngineDataGraph
    from calculations import (
        overall_resist_forces,
        cs_overall_resist_forces,
        tractive_f,
        final_force,
    )

    engine_db = shelve.open("engines.db")
    arac_tork_name = "2jz_tork"
    arac_rpm_name = "2jz_rpm"
    disli_kutusu = [3.23, 2.52, 1.66, 1.22, 1, 3.45]
    dif_orani = 3.45
    yaricap = 0.299  # metre
    verim = 0.85
    yuvarlanma_katsiyi = 0.015
    w_arac = 1500
    # aerodinamik direnç katsayıları
    hava_yogunlugu = 1
    ruzgar_hizi = 20  # km/saat
    izdusum = 4
    ae_katsayi = 0.19
    yol_egimi = 0
    arac = Motor(
        gearBox=disli_kutusu,
        oran_diferansiyel=dif_orani,
        tekerlek_yaricap=yaricap,
        ao_verimi=verim,
        arac_kutlesi=w_arac,
        yuvarlanma_katsiyi=yuvarlanma_katsiyi,
        ro_hava_yogunlugu=hava_yogunlugu,
        v_ruzgar=kmh_to_ms(ruzgar_hizi),
        af_arac_izdusum_alanı=izdusum,
        cd_aerodinamik_direnc_katsayisi=ae_katsayi,
        yol_egimi=yol_egimi,
    )
    tork_times_gear_list = arac.torque_rev_per_gear(
        tork_list=engine_db[arac_tork_name], overall_gear_ratio=arac.gearBox
    )
    arac_v_list = arac.velocity_rpm(rpm=engine_db[arac_rpm_name], gear_box=arac.gearBox)
    windy_v_list = arac.windy_velocity_rpm(
        rpm=engine_db[arac_rpm_name], gear_box=arac.gearBox, ruzgar_hizi=arac.v_ruzgar
    )
    resist_forces = overall_resist_forces(
        arac_kutlesi=arac.arac_kutlesi,
        cekim_ivmesi=arac.cekim_ivmesi,
        yuvarlanma_katsiyi=arac.yuvarlanma_katsiyi,
        yol_egimi=arac.yol_egimi,
        p_yogunluk=arac.ro_hava_yogunlugu,
        cw_aero=arac.cd_aerodinamik_direnc_katsayisi,
        Af_izdusum=arac.af_arac_izdusum_alanı,
        hiz_list=windy_v_list,
    )

    cs_resist_forces = cs_overall_resist_forces(
        arac_kutlesi=arac.arac_kutlesi,
        cekim_ivmesi=arac.cekim_ivmesi,
        yuvarlanma_katsiyi=arac.yuvarlanma_katsiyi,
        yol_egimi=arac.yol_egimi,
        p_yogunluk=arac.ro_hava_yogunlugu,
        cw_aero=arac.cd_aerodinamik_direnc_katsayisi,
        Af_izdusum=arac.af_arac_izdusum_alanı,
        hiz_list=arac_v_list,
        ruzgar_hizi=arac.v_ruzgar,
    )
    ########################################################################################
    arac_graph = EngineDataGraph(
        engine_db, arac_tork_name, arac_rpm_name, "rb 26 motoru"
    )

    ##########################################################
    app = QtWidgets.QApplication(sys.argv)
    VehicleDynamicsApp = QtWidgets.QMainWindow()
    print(QtWidgets.QStyleFactory.keys())
    app.setStyle("Fusion")
    ui = Ui_VehicleDynamicsApp()
    ui.setupUi(VehicleDynamicsApp)
    VehicleDynamicsApp.show()
    sys.exit(app.exec_())
