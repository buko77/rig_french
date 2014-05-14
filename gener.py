#!/usr/bin/python
# -*- encoding:utf8 -*-
import random

def ext_pf():
	lines = open('pre_fem_fr.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline)

def ext_nom():
	lines = open('noms.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline)

def ext_rues():
	lines = open('rues_net.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline), random.randint(0,110)



def ext_ville():
	lines = open('villes_cp.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline)


ext_pf()
ext_nom()
ext_rues()
ext_ville()


