#!/usr/bin/python

from socket import *

ports = [
80,
22,
443
]
ip = raw_input("Enter IP Address: ")

for i in ports:




	try:
		s = socket()
		s.connect((ip, i ))
		print "Port", i, "is open"
		s.close()
	except:
		print "Port", i, "is closed"
