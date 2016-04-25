# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(417, 485)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 411, 441))
        #self.textBrowser.setStyleSheet("background-image:url(anamenu.jpg)");
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 450, 301, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 450, 56, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 450, 51, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ptchat v0.1", None))
        self.label.setText(_translate("Form", "Mesajınız", None))
        self.pushButton.setText(_translate("Form", "Gönder", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    win = Ui_Form()
    win.setupUi(form)
    form.show()
    app.exec_()