#!/bin/bash

for i in {1..30}; do
	ping google.com -c1 -W1 -t$i |grep From |cut -d"(" -f2|cut -d")" -f1
done
