#!/usr/bin/python

from socket import *
"""
ports = [
80,
22,
443
]
"""

ip = raw_input("Enter IP Address: ")

for port in range(1, 100):

	try:
		s = socket()
		s.connect((ip, port ))
		s.send("\n\r")
		banner = s.recv(2048)
		print "Port", port, "is open"
		print banner
		s.close()
	except:
		continue
		#print "Port", port, "is closed"
