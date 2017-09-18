# -*- coding: UTF-8 -*-

import threading
import time

BUFSIZ=1024

class RecvThread(threading.Thread):
	"""docstring for RecvThread"""
	def __init__(self, tcpClientSock, addr):
		super(RecvThread, self).__init__()
		self.tcpClientSock = tcpClientSock
		self.addr = addr

    def run(self):
    	try:
		    data=self.tcpClientSock.recv(BUFSIZ)
		except:
		    print(e)
		    self.tcpClientSock.close()
		    self.join()

