#!/usr/bin/python
#-*- coding:utf8 -*-

import re

shakes = open("rues.txt", "r")

for line in shakes:
    if re.match("^(R|r)ue", line) or re.match("^Avenue", line) or re.match("^Boulevard", line) or re.match("^Place", line) or re.match("^Quai", line) or re.match("^Grande", line) or re.match("^Allée", line):
        print line
