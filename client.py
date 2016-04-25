# -*- coding: utf-8 -*- 
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from login import Ui_MainWindow  #(kayit)
from mainmenu import Ui_MainWindow2   #(anasayfa)
from message import Ui_Form    #(sohbet)
import MySQLdb
import socket,cPickle,os

class FirstLogin(QtGui.QMainWindow,Ui_Form):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.text_isle)
		host = "localhost"
		port = 12397
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.connect((host, port))
		self.name = "Admin"
		self.server.sendall(self.name)
		data = self.server.recv(1024)
		print (data)
		if data != "#gir":
			sys.exit(1)

	def text_isle(self):
		
		if (len(self.ui.lineEdit.text()) == 0):
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("Bos Mesaj Gonderemezsiniz.!")
			msg.setWindowTitle("WARNING")
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()
		else:

			msg = str(self.ui.lineEdit.text())
			self.server.sendall(msg)
			cpikle = self.server.recv(1024)
			dumps = cPickle.loads(str(cpikle))
			self.ymetin = ""
			for i in dumps:
				self.ymetin += str.format("{} : {}\n" , i['client'][1], i['message'])
			self.ui.textBrowser.setText(self.ymetin)
			self.ui.lineEdit.setText("")
			

class Giris(QtGui.QMainWindow,Ui_MainWindow2):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self,parent)
		self.ui=Ui_MainWindow2()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.sign_up)
		self.ui.pushButton_2.clicked.connect(self.login)
		self.window2 = None
		self.frstlgn = None
	
	def login(self):
		try:
			# Execute the SQL command
			db = MySQLdb.connect("127.0.0.1","root","password","Python" ) #localhost - username - password - databasename
			cursor = db.cursor()
			sql = ("SELECT * FROM Kullanicilar")
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				fname = row[0]
				lname = row[1]
				pswrd = row[2]
				
				if (self.ui.k_adi.text() == fname and int(self.ui.k_pswrd.text()) == pswrd):
					self.ui.statusbar.showMessage("Giris Basarili")
					self.frstlgn = FirstLogin(self.frstlgn)
					self.frstlgn.show()
					self.close() 
				else:
					self.ui.statusbar.showMessage("Error: Username or Password Not Defined")

					print "FIRSTNAME :%s ---> LASTNAME :%s  ---> PASSWORD:%s" % (fname, lname, pswrd)
		except:
			print ("Error: unable to fecth data ")
			
	def sign_up(self):
		self.window2 = Main(self.window2)
		self.window2.show()
		self.close()

class Main(QtGui.QMainWindow,Ui_MainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton2.clicked.connect(self.kayit)
		self.ui.pushButton2.setToolTip("Kayit Ol")
		self.grs=None


	def kayit(self):
		username = self.ui.lineEdit.text()
		email = self.ui.lineEdit_2.text()
		password = int(self.ui.lineEdit_3.text())

		db = MySQLdb.connect("localhost","root","password","Python" )
		cursor = db.cursor()
		#cursor.execute("DROP TABLE IF EXISTS Kullanicilar")
		#sql = """ CREATE TABLE Kullanicilar (ADI CHAR(20) NOT NULL , SOYADI CHAR(20) NOT NULL , YAS INT )"""
		sql = "INSERT INTO Kullanicilar(ADI,SOYADI,PAROLA) VALUES('%s','%s','%d')" %(username,email,password)
		cursor.execute(sql)
		db.commit()
		self.ui.statusbar.showMessage("kayit eklendi")
		self.ui.lineEdit.setText("")
		self.ui.lineEdit_2.setText("") 
		self.ui.lineEdit_3.setText("")   
		db.close()
		self.grs = Giris(self.grs)
		self.grs.show()
		self.close()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Giris()
	window.show()
	sys.exit(app.exec_())