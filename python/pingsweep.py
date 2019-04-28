#!/usr/bin/python

from scapy.all import *

a = sr1(IP(dst='192.168.1.187')/ICMP())

print(a[IP].src)
