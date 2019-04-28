#!/usr/bin/python

import time
from scapy.all import *

addr = raw_input('please enter an ip address or domain name: ')
a=IP(dst=addr,ttl=128)/UDP(dport=666,sport=666)
print(a.summary())
#a.summary()
time.sleep(3)
print(a.show())
