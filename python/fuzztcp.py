#!/usr/bin/python

from scapy.all import *

a=send(IP(dst='192.168.44.147')/fuzz(TCP(window=5000)),loop=1)
print a
