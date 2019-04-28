#!/usr/bin/python

import time
from scapy.all import *

addr = raw_input('Please enter an ip address or Domain name: ')
a=IP(dst=addr,ttl=128)/TCP(window=5700)
print(a.summary())
time.sleep(3)
print(a.show())
