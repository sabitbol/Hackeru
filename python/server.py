#!/usr/bin/python
from socket import *

s = socket()

ip = '0.0.0.0'

s.bind((ip, 8080))

s.listen(1)

var1, var2 = s.accept()

print "This is the client address:", var2

data = var1.recv(2048)

print 'This is the data:', data

var1.send('some info')

var1.close()

s.close()
