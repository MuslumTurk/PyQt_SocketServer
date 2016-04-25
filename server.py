# -*- coding: utf-8 -*-
#!/usr/bin/python

import socketserver
import datetime
import pickle
import threading

bagli_clientlar = []
mesajlar = []

class MyHandler(socketserver.BaseRequestHandler):

	def handle(self):
		print ("Connected from :" ,self.client_address)

		username = self.request.recv(1024)
		bagli_clientlar.append({'client': self.client_address,
								'name': username, 'date': datetime.datetime.now()})
		gir = '#gir'
		self.request.sendall(gir.encode('utf-8'))
		while True:
			try:	
				msg = self.request.recv(1024)
				mesajlar.append({'client': (self.client_address[0], username),
								 'date': datetime.datetime.now(), 'message': msg})
				self.request.sendall(pickle.dumps(mesajlar,2))
				print ("\n" + username.decode('utf-8') +" -> "+ msg.decode('utf-8'))
			except:
				self.request.close()
				continue

		print ("Disconnect from :", self.client_address)

def baglanti_kur(host,port,classname):
	server = socketserver.ThreadingTCPServer((host,port),classname)
	server.serve_forever()
	

if __name__=="__main__":
	baglanti_kur('localhost',12397,MyHandler)
		
