#!/usr/bin/python
# -*- encoding:utf8 -*-

#Ce script permet de générer une identité fictive qui comprend :
#Prénom (femme/homme)
#Nom (en capital)
#addresse et numéro(s)
#ville et code postal

#SCRIPT MADE BY BUKO 
#VERSION 1.0

import argparse
import random
parser = argparse.ArgumentParser(description="Generateur aleatoire d'identité fictive")

parser.add_argument('-g', '--genre', help="""Permet de selectionner le genre du profil:
					 m = masculin
					 f = feminin""", required=True)
args = vars(parser.parse_args())
def ext_pf():
	lines = open('pre_fem_fr.txt').read().decode('utf8').splitlines()
	myline = random.choice(lines)
	print(myline.encode('utf8'))

def ext_pm():
	lines = open('pre_masc_fr.txt').read().decode('utf8').splitlines()
	myline = random.choice(lines)
	print(myline.encode('utf8'))

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

def main():
	if args['genre'] == 'f':
		ext_pf()
		ext_nom()
		ext_rues()
		ext_ville()
	elif args['genre'] == 'm':
		ext_pm()
		ext_nom()
		ext_rues()
		ext_ville()
	
if __name__ == '__main__':
	main()
