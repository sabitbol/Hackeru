#!/usr/bin/python

from scapy.all import *

a=send(IP(dst='192.168.44.147')/fuzz(UDP()),loop=1)
print a
