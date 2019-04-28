#!/usr/bin/python
   #Imports
from scapy.all import *
from socket import *

  #We create a new socket instance using UDP (SOCK_DGRAM)
sock = socket(AF_INET, SOCK_DGRAM)
  #We connect to 1.1.1.1 DNS server on port 53
sock.connect(('1.1.1.1', 53))
  #We build a (legal) DNS Packet
dnsQ = DNS(rd=1, qd=DNSQR(qname='ynet.co.il'))
  #Cast it to a string (in order to send it out)
dnsString = str(dnsQ)
  #Sending the string packet
sock.send(dnsString)
  # And reciving the response and casting it back to DNS
ls(DNS(sock.recv(4096)))
