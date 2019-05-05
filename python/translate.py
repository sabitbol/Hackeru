#!/usr/bin/python

import urllib

ufile = urllib.urlopen("https://www.morfix.co.il/home")
text = ufile.readlines()

# ^ curl

printline = 0

for line in text:
	if printline == 1:
		ans = line.split('<')[0]  # = cut -d"<" -f1
		print ans.decode('utf-8')[::-1].strip() # [::-1] = rev ; strip = remove spaces
		printline = 0
	if "normal_translation_div" in line:
		printline = 1
	# ^ grep + A1
