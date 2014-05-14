#!/usr/bin/python
# -*- coding:utf8 -*- 
import csv
lol = list(csv.reader(open('prenoms.csv', 'rb'), delimiter='\t'))

for line in lol:
	if 'f' in line:
		print line[0]





