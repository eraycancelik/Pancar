# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from . import widgets_rc

class Ui_Rapor(object):
    def setupUi(self, Rapor):
        Rapor.setObjectName("Rapor")
        Rapor.resize(346, 338)
        Rapor.setMinimumSize(QtCore.QSize(346, 338))
        Rapor.setMaximumSize(QtCore.QSize(346, 338))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icons/tofile.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Rapor.setWindowIcon(icon)
        Rapor.setStyleSheet("background-color: rgb(28,28,28);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Rapor)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(parent=Rapor)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 6))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 130))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 130))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.groupBox)
        self.frame_2.setStyleSheet("border:3px solid rgba(50,50,50,.2);\n"
"background-color: rgb(5,5,5);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(90, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.motor = QtWidgets.QLabel(parent=self.frame_2)
        self.motor.setObjectName("motor")
        self.horizontalLayout.addWidget(self.motor)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(parent=self.frame_2)
        self.line.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.arac = QtWidgets.QLabel(parent=self.frame_2)
        self.arac.setObjectName("arac")
        self.horizontalLayout_3.addWidget(self.arac)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(parent=self.frame_2)
        self.line_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.sanziman = QtWidgets.QLabel(parent=self.frame_2)
        self.sanziman.setObjectName("sanziman")
        self.horizontalLayout_4.addWidget(self.sanziman)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.line_3.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.cevre = QtWidgets.QLabel(parent=self.frame_2)
        self.cevre.setObjectName("cevre")
        self.horizontalLayout_5.addWidget(self.cevre)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame1 = QtWidgets.QFrame(parent=self.groupBox_2)
        self.frame1.setStyleSheet("border:3px solid rgba(50,50,50,.2);\n"
"background-color: rgb(5,5,5);")
        self.frame1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.frame1)
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.kullanici = QtWidgets.QLabel(parent=self.frame1)
        self.kullanici.setObjectName("kullanici")
        self.horizontalLayout_2.addWidget(self.kullanici)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_5 = QtWidgets.QFrame(parent=self.frame1)
        self.line_5.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_4.addWidget(self.line_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(parent=self.frame1)
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.arac_ismi = QtWidgets.QLabel(parent=self.frame1)
        self.arac_ismi.setObjectName("arac_ismi")
        self.horizontalLayout_6.addWidget(self.arac_ismi)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.frame1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_8.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"border-radius:4px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.rapor_olustur = QtWidgets.QCommandLinkButton(parent=self.frame_4)
        self.rapor_olustur.setMinimumSize(QtCore.QSize(0, 0))
        self.rapor_olustur.setStyleSheet("background-color: rgb(200,200,200);\n"
"box-shadow: 1px 1px 147px 0px rgba(156,66,66,0.72);\n"
"-webkit-box-shadow: 1px 1px 147px 0px rgba(156,66,66,0.72);\n"
"-moz-box-shadow: 1px 1px 147px 0px rgba(156,66,66,0.72);\n"
"border:2px solid rgb(5,5,5);")
        self.rapor_olustur.setDefault(True)
        self.rapor_olustur.setObjectName("rapor_olustur")
        self.verticalLayout_9.addWidget(self.rapor_olustur)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_11.addWidget(self.frame_3)

        self.retranslateUi(Rapor)
        QtCore.QMetaObject.connectSlotsByName(Rapor)

    def retranslateUi(self, Rapor):
        _translate = QtCore.QCoreApplication.translate
        Rapor.setWindowTitle(_translate("Rapor", "Rapor"))
        self.groupBox.setTitle(_translate("Rapor", "Raporlanacak Araç Bilgileri"))
        self.label.setText(_translate("Rapor", "Araç"))
        self.motor.setText(_translate("Rapor", "2 JZ"))
        self.label_2.setText(_translate("Rapor", "Motor "))
        self.arac.setText(_translate("Rapor", "Toyota Supra"))
        self.label_3.setText(_translate("Rapor", "Şanzıman"))
        self.sanziman.setText(_translate("Rapor", "W55 5-speed transmission"))
        self.label_12.setText(_translate("Rapor", "Çevre"))
        self.cevre.setText(_translate("Rapor", "Nürburgring "))
        self.groupBox_2.setTitle(_translate("Rapor", "Genel Bilgiler"))
        self.label_8.setText(_translate("Rapor", "Test Mühendisi"))
        self.kullanici.setText(_translate("Rapor", "Eray Cançelik"))
        self.label_9.setText(_translate("Rapor", "Araç"))
        self.arac_ismi.setText(_translate("Rapor", "Toyota supra mk3 2jz"))
        self.rapor_olustur.setText(_translate("Rapor", "Rapor oluştur  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rapor = QtWidgets.QDialog()
    ui = Ui_Rapor()
    ui.setupUi(Rapor)
    Rapor.show()
    sys.exit(app.exec())
