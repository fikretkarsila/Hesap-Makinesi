# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesap_makinesi_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 452)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #878d8b;\n"
"    color: #000000;\n"
"    border-color: #000000;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ekran = QtWidgets.QLineEdit(self.centralwidget)
        self.ekran.setGeometry(QtCore.QRect(10, 10, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Azonix")
        font.setPointSize(20)
        self.ekran.setFont(font)
        self.ekran.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #a6d072;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #000000;\n"
"    font-family: \"Azonix\";\n"
"\n"
"}")
        self.ekran.setCursorPosition(1)
        self.ekran.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ekran.setDragEnabled(True)
        self.ekran.setReadOnly(True)
        self.ekran.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ekran.setClearButtonEnabled(False)
        self.ekran.setObjectName("ekran")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tus_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_7.setFont(font)
        self.tus_7.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_7.setObjectName("tus_7")
        self.horizontalLayout.addWidget(self.tus_7)
        self.tus_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_8.setFont(font)
        self.tus_8.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_8.setObjectName("tus_8")
        self.horizontalLayout.addWidget(self.tus_8)
        self.tus_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_9.setFont(font)
        self.tus_9.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_9.setObjectName("tus_9")
        self.horizontalLayout.addWidget(self.tus_9)
        self.tus_carpi = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_carpi.setFont(font)
        self.tus_carpi.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_carpi.setObjectName("tus_carpi")
        self.horizontalLayout.addWidget(self.tus_carpi)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 361, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tus_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_4.setFont(font)
        self.tus_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_4.setObjectName("tus_4")
        self.horizontalLayout_2.addWidget(self.tus_4)
        self.tus_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_5.setFont(font)
        self.tus_5.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_5.setObjectName("tus_5")
        self.horizontalLayout_2.addWidget(self.tus_5)
        self.tus_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_6.setFont(font)
        self.tus_6.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_6.setObjectName("tus_6")
        self.horizontalLayout_2.addWidget(self.tus_6)
        self.tus_eksi = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_eksi.setFont(font)
        self.tus_eksi.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_eksi.setObjectName("tus_eksi")
        self.horizontalLayout_2.addWidget(self.tus_eksi)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 330, 361, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tus_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_1.setFont(font)
        self.tus_1.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_1.setObjectName("tus_1")
        self.horizontalLayout_3.addWidget(self.tus_1)
        self.tus_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_2.setFont(font)
        self.tus_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_2.setObjectName("tus_2")
        self.horizontalLayout_3.addWidget(self.tus_2)
        self.tus_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_3.setFont(font)
        self.tus_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_3.setObjectName("tus_3")
        self.horizontalLayout_3.addWidget(self.tus_3)
        self.tus_arti = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_arti.setFont(font)
        self.tus_arti.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_arti.setObjectName("tus_arti")
        self.horizontalLayout_3.addWidget(self.tus_arti)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 380, 360, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tus_negatif = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_negatif.setFont(font)
        self.tus_negatif.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_negatif.setObjectName("tus_negatif")
        self.horizontalLayout_4.addWidget(self.tus_negatif)
        self.tus_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_0.setFont(font)
        self.tus_0.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_0.setObjectName("tus_0")
        self.horizontalLayout_4.addWidget(self.tus_0)
        self.tus_virgul = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_virgul.setFont(font)
        self.tus_virgul.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_virgul.setObjectName("tus_virgul")
        self.horizontalLayout_4.addWidget(self.tus_virgul)
        self.tus_hesapla = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_hesapla.setFont(font)
        self.tus_hesapla.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_hesapla.setObjectName("tus_hesapla")
        self.horizontalLayout_4.addWidget(self.tus_hesapla)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 180, 361, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tus_1_bolu_x = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_1_bolu_x.setFont(font)
        self.tus_1_bolu_x.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_1_bolu_x.setObjectName("tus_1_bolu_x")
        self.horizontalLayout_5.addWidget(self.tus_1_bolu_x)
        self.tus_karesi = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_karesi.setFont(font)
        self.tus_karesi.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_karesi.setObjectName("tus_karesi")
        self.horizontalLayout_5.addWidget(self.tus_karesi)
        self.tus_kok = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_kok.setFont(font)
        self.tus_kok.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_kok.setObjectName("tus_kok")
        self.horizontalLayout_5.addWidget(self.tus_kok)
        self.tus_bolme = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_bolme.setFont(font)
        self.tus_bolme.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_bolme.setObjectName("tus_bolme")
        self.horizontalLayout_5.addWidget(self.tus_bolme)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 130, 360, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tus_yuzde = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.tus_yuzde.setMinimumSize(QtCore.QSize(86, 37))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_yuzde.setFont(font)
        self.tus_yuzde.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_yuzde.setObjectName("tus_yuzde")
        self.horizontalLayout_6.addWidget(self.tus_yuzde)
        self.tus_son_islem_iptal = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_son_islem_iptal.setFont(font)
        self.tus_son_islem_iptal.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_son_islem_iptal.setObjectName("tus_son_islem_iptal")
        self.horizontalLayout_6.addWidget(self.tus_son_islem_iptal)
        self.tus_ekrani_sil = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_ekrani_sil.setFont(font)
        self.tus_ekrani_sil.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_ekrani_sil.setObjectName("tus_ekrani_sil")
        self.horizontalLayout_6.addWidget(self.tus_ekrani_sil)
        self.tus_tek_tek_sil = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tus_tek_tek_sil.setFont(font)
        self.tus_tek_tek_sil.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #cdceb1;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: #dfdfc0;\n"
"    margin: 2px;\n"
"\n"
"}")
        self.tus_tek_tek_sil.setObjectName("tus_tek_tek_sil")
        self.horizontalLayout_6.addWidget(self.tus_tek_tek_sil)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ekran, self.tus_yuzde)
        MainWindow.setTabOrder(self.tus_yuzde, self.tus_son_islem_iptal)
        MainWindow.setTabOrder(self.tus_son_islem_iptal, self.tus_ekrani_sil)
        MainWindow.setTabOrder(self.tus_ekrani_sil, self.tus_tek_tek_sil)
        MainWindow.setTabOrder(self.tus_tek_tek_sil, self.tus_1_bolu_x)
        MainWindow.setTabOrder(self.tus_1_bolu_x, self.tus_karesi)
        MainWindow.setTabOrder(self.tus_karesi, self.tus_kok)
        MainWindow.setTabOrder(self.tus_kok, self.tus_bolme)
        MainWindow.setTabOrder(self.tus_bolme, self.tus_7)
        MainWindow.setTabOrder(self.tus_7, self.tus_8)
        MainWindow.setTabOrder(self.tus_8, self.tus_9)
        MainWindow.setTabOrder(self.tus_9, self.tus_carpi)
        MainWindow.setTabOrder(self.tus_carpi, self.tus_4)
        MainWindow.setTabOrder(self.tus_4, self.tus_5)
        MainWindow.setTabOrder(self.tus_5, self.tus_6)
        MainWindow.setTabOrder(self.tus_6, self.tus_eksi)
        MainWindow.setTabOrder(self.tus_eksi, self.tus_1)
        MainWindow.setTabOrder(self.tus_1, self.tus_2)
        MainWindow.setTabOrder(self.tus_2, self.tus_3)
        MainWindow.setTabOrder(self.tus_3, self.tus_arti)
        MainWindow.setTabOrder(self.tus_arti, self.tus_negatif)
        MainWindow.setTabOrder(self.tus_negatif, self.tus_0)
        MainWindow.setTabOrder(self.tus_0, self.tus_virgul)
        MainWindow.setTabOrder(self.tus_virgul, self.tus_hesapla)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ekran.setText(_translate("MainWindow", "0"))
        self.tus_7.setText(_translate("MainWindow", "7"))
        self.tus_8.setText(_translate("MainWindow", "8"))
        self.tus_9.setText(_translate("MainWindow", "9"))
        self.tus_carpi.setText(_translate("MainWindow", "x"))
        self.tus_4.setText(_translate("MainWindow", "4"))
        self.tus_5.setText(_translate("MainWindow", "5"))
        self.tus_6.setText(_translate("MainWindow", "6"))
        self.tus_eksi.setText(_translate("MainWindow", "-"))
        self.tus_1.setText(_translate("MainWindow", "1"))
        self.tus_2.setText(_translate("MainWindow", "2"))
        self.tus_3.setText(_translate("MainWindow", "3"))
        self.tus_arti.setText(_translate("MainWindow", "+"))
        self.tus_negatif.setText(_translate("MainWindow", "+/-"))
        self.tus_0.setText(_translate("MainWindow", "0"))
        self.tus_virgul.setText(_translate("MainWindow", ","))
        self.tus_hesapla.setText(_translate("MainWindow", "="))
        self.tus_1_bolu_x.setText(_translate("MainWindow", "¹/x"))
        self.tus_karesi.setText(_translate("MainWindow", "x²"))
        self.tus_kok.setText(_translate("MainWindow", "²√x"))
        self.tus_bolme.setText(_translate("MainWindow", "/"))
        self.tus_yuzde.setText(_translate("MainWindow", "%"))
        self.tus_son_islem_iptal.setText(_translate("MainWindow", "CE"))
        self.tus_ekrani_sil.setText(_translate("MainWindow", "C"))
        self.tus_tek_tek_sil.setText(_translate("MainWindow", "←"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
