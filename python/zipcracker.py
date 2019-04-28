#!/usr/bin/python

import zipfile2

passw = ['1234', '9876', '2468']
zip = zipfile2.ZipFile('/home/shimon/zipCracker/protected.zip', 'r')
for i in passw:
	try:
		zipfile2.ZipFile.extractall(zip, pwd=i)
	except:
		continue
