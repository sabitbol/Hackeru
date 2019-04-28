#!/usr/bin/python

import zipfile2

zip = zipfile2.ZipFile('/home/shimon/protected.zip', 'r')
zipfile2.ZipFile.extractall(zip, pwd='2468')
