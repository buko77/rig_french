#!/usr/bin/python
# -*- coding: utf-8 -*-
#script for download the streetname of Lyon
#need to complete the script for send the output in a file.csv
#need to clean the data

from BeautifulSoup import BeautifulSoup
import requests
file = open('rues.txt', 'w')
url = 'http://fr.wikipedia.org/wiki/Liste_des_rues,_places_et_ponts_de_Lyon'
r = requests.get(url)
soup = BeautifulSoup(r.text)
#soup2 = soup.decode('utf8')
villes = [a.text for a in soup.findAll('a')]
#villes2 = [a.text for a in soup.findAll('a', attrs={'a': 'title'})]
#villes2 = villes.decode('utf8')
for v in villes:
	file.write(v.encode('utf8')+'\n')
	


