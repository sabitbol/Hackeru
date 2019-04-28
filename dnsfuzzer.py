#!/usr/bin/python

from scapy.all import *

ip = raw_input('please enter an ip address: ')
a=send(IP(dst=ip)/TCP()/fuzz(DNS(id=6000)),loop=1)
print a
