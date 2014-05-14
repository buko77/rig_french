#!/usr/bin/python
# -*- encoding:utf8 -*-
import argparse
import random
parser = argparse.ArgumentParser(description="Generateur aleatoire d'identité fictive")

parser.add_argument('-s', '--sexe', help="""Permet de selectionner le sexe du profil:
					 m = masculin
					 f = feminin""", required=True)
args = vars(parser.parse_args())
def ext_pf():
	lines = open('pre_fem_fr.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline)

def ext_pm():
	lines = open('pre_masc_fr.txt').read().splitlines()
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

def main():
	if args['sexe'] == 'f':
		ext_pf()
		ext_nom()
		ext_rues()
		ext_ville()
	elif args['sexe'] == 'm':
		ext_pm()
		ext_nom()
		ext_rues()
		ext_ville()
	
if __name__ == '__main__':
	main()
