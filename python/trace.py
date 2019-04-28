#!/usr/bin/python

from scapy.all import *

for i in range(1,31):
	a=sr1(IP(dst="google.com",ttl=i)/ICMP())
	print(a[IP].src)
