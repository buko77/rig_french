#!/usr/bin/python
# -*- coding:utf8 -*- 
import csv
lol = list(csv.reader(open('prenoms.csv', 'rb'), delimiter='\t'))



for line in lol:
	if 'm' in line[1] and 'french' in line[2]:
		print line[0]


