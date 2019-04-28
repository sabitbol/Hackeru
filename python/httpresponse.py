#!/usr/bin/python

import time
import urllib

response = urllib.urlopen("https://ynet.co.il/")
print response.code

if response.code == 200:
	print "Page loaded Successfully"

time.sleep(3)
dir(response.headers)

print response.read()

time.sleep(3)

print response.url
