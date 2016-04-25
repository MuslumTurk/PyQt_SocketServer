# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anamenu.ui'
#
# Created: Fri Apr 15 13:07:10 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(539, 286)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 80, 61, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 80, 61, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.k_adi = QtGui.QLineEdit(self.centralwidget)
        self.k_adi.setGeometry(QtCore.QRect(392, 10, 141, 24))
        self.k_adi.setObjectName(_fromUtf8("k_adi"))
        self.k_pswrd = QtGui.QLineEdit(self.centralwidget)
        self.k_pswrd.setGeometry(QtCore.QRect(392, 40, 141, 24))
        self.k_pswrd.setObjectName(_fromUtf8("k_pswrd"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 40, 50, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Kayit Ol", None))
        self.pushButton_2.setText(_translate("MainWindow", "Giriş Yap", None))
        self.label.setText(_translate("MainWindow", "Kullanici Adi", None))
        self.label_2.setText(_translate("MainWindow", "Parola", None))

