#!/usr/bin/python

from scapy.all import *
import time
s = input('Please choose a Number: ')
time.sleep(2)
print 'the number you chose is: ', s
a=sniff(s)
print(a)
'''
a.summary()
b=a[1]
b.show()
'''
