#!/usr/bin/python

from scapy.all import *

addr = raw_input('Please enter an ip address or domain name: ')

for ping in range(0,4):
	a=sr1(IP(dst=addr,ttl=128)/ICMP())
	print(a[IP].src)
	#a=IP(dst=addr,ttl=ping)/ICMP()
	#a.show()
