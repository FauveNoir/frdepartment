#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cli.app # probably not necessary
import sys
from optparse import OptionParser
import argparse

coresp = [
["Ain", "01", "AN","Rhône-Alpes","regularDepartment"],
["Aisne", "02", "AS","Picardie","regularDepartment"],
["Allier", "03", "AL","Auvergne","regularDepartment"],
["Alpes-de-Haute-Provence", "04", "AH","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Hautes-Alpes", "05", "HA","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Alpes-Maritimes", "06", "AM","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Ardèche", "07", "AC","Rhône-Alpes","regularDepartment"],
["Ardennes", "08", "AR","Champagne-Ardenne","regularDepartment"],
["Ariège", "09", "AG","Midi-Pyrénées","regularDepartment"],
["Aube", "10", "AB","Champagne-Ardenne","regularDepartment"],
["Aude", "11", "AD","Languedoc-Roussillon","regularDepartment"],
["Aveyron", "12", "AV","Midi-Pyrénées","regularDepartment"],
["Bouches-du-Rhône", "13", "BR","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Calvados", "14", "CV","Basse-Normandie","regularDepartment"],
["Cantal", "15", "CT","Auvergne","regularDepartment"],
["Charente", "16", "CH","Poitou-Charentes","regularDepartment"],
["Charente-Maritime", "17", "CM","Poitou-Charentes","regularDepartment"],
["Cher", "18", "CR","Centre","regularDepartment"],
["Corrèze", "19", "CZ","Limousin","regularDepartment"],
["Corse-du-sud", "2A", "CS","Corse","regularDepartment"],
["Haute-Corse", "2B", "HC","Corse","regularDepartment"],
["Côte-d’Or", "21", "CO","Bourgogne","regularDepartment"],
["Côtes-d’Armor", "22", "CA","Bretagne","regularDepartment"],
["Creuse", "23", "CE","Limousin","regularDepartment"],
["Dordogne", "24", "DG","Aquitaine","regularDepartment"],
["Doubs", "25", "DB","Franche-Comté","regularDepartment"],
["Drôme", "26", "DM","Rhône-Alpes","regularDepartment"],
["Eure", "27", "ER","Haute-Normandie","regularDepartment"],
["Eure-et-Loir", "28", "EL","Centre","regularDepartment"],
["Finistère", "29", "FI","Bretagne","regularDepartment"],
["Gard", "30", "GA","Languedoc-Roussillon","regularDepartment"],
["Haute-Garonne", "31", "HG","Midi-Pyrénées","regularDepartment"],
["Gers", "32", "GR","Midi-Pyrénées","regularDepartment"],
["Gironde", "33", "GD","Aquitaine","regularDepartment"],
["Hérault", "34", "HT","Languedoc-Roussillon","regularDepartment"],
["Ille-et-Vilaine", "35", "IV","Bretagne","regularDepartment"],
["Indre", "36", "ID","Centre","regularDepartment"],
["Indre-et-Loire", "37", "IL","Centre","regularDepartment"],
["Isère", "38", "IS","Rhône-Alpes","regularDepartment"],
["Jura", "39", "JR","Franche-Comté","regularDepartment"],
["Landes", "40", "LD","Aquitaine","regularDepartment"],
["Loir-et-Cher", "41", "LC","Centre","regularDepartment"],
["Loire", "42", "LR","Rhône-Alpes","regularDepartment"],
["Haute-Loire", "43", "HL","Auvergne","regularDepartment"],
["Loire-Atlantique", "44", "LA","Pays de la Loire","regularDepartment"],
["Loiret", "45", "LT","Centre","regularDepartment"],
["Lot", "46", "LO","Midi-Pyrénées","regularDepartment"],
["Lot-et-Garonne", "47", "LG","Aquitaine","regularDepartment"],
["Lozère", "48", "LZ","Languedoc-Roussillon","regularDepartment"],
["Maine-et-Loire", "49", "ML","Pays de la Loire","regularDepartment"],
["Manche", "50", "MN","Basse-Normandie","regularDepartment"],
["Marne", "51", "MR","Champagne-Ardenne","regularDepartment"],
["Haute-Marne", "52", "HM","Champagne-Ardenne","regularDepartment"],
["Mayenne", "53", "MY","Pays de la Loire","regularDepartment"],
["Meurthe-et-Moselle", "54", "MM","Lorraine","regularDepartment"],
["Meuse", "55", "MS","Lorraine","regularDepartment"],
["Morbihan", "56", "MH","Bretagne","regularDepartment"],
["Moselle", "57", "MO","Lorraine","regularDepartment"],
["Nièvre", "58", "NV","Bourgogne","regularDepartment"],
["Nord", "59", "ND","Nord-Pas-de-Calais","regularDepartment"],
["Oise", "60", "OI","Picardie","regularDepartment"],
["Orne", "61", "OR","Basse-Normandie","regularDepartment"],
["Pas-de-Calais", "62", "PC","Nord-Pas-de-Calais","regularDepartment"],
["Puy-de-Dôme", "63", "PD","Auvergne","regularDepartment"],
["Pyrénées-Atlantiques", "64", "PA","Aquitaine","regularDepartment"],
["Hautes-Pyrénées", "65", "HP","Midi-Pyrénées","regularDepartment"],
["Pyrénées-Orientales", "66", "PO","Languedoc-Roussillon","regularDepartment"],
["Bas-Rhin", "67", "BH","Alsace","regularDepartment"],
["Haut-Rhin", "68", "HR","Alsace","regularDepartment"],
["Rhône", "69", "RÔ","Rhône-Alpes","regularDepartment"],
["Haute-Saône", "70", "HS","Franche-Comté","regularDepartment"],
["Saône-et-Loire", "71", "SL","Bourgogne","regularDepartment"],
["Sarthe", "72", "ST","Pays de la Loire","regularDepartment"],
["Savoie", "73", "SV","Rhône-Alpes","regularDepartment"],
["Haute-Savoie", "74", "HO","Rhône-Alpes","regularDepartment"],
["Paris", "75", "PR","Île-de-France","regularDepartment"],
["Seine-Maritime", "76", "SR","Haute-Normandie","regularDepartment"],
["Seine-et-Marne", "77", "SM","Île-de-France","regularDepartment"],
["Yvelines", "78", "YV","Île-de-France","regularDepartment"],
["Deux-Sèvres", "79", "DS","Poitou-Charentes","regularDepartment"],
["Somme", "80", "SO","Picardie","regularDepartment"],
["Tarn", "81", "TR","Midi-Pyrénées","regularDepartment"],
["Tarn-et-Garonne", "82", "TG","Midi-Pyrénées","regularDepartment"],
["Var", "83", "VR","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Vaucluse", "84", "VA","Provence-Alpes-Côte d’Azur","regularDepartment"],
["Vendée", "85", "VD","Pays de la Loire","regularDepartment"],
["Vienne", "86", "VI","Poitou-Charentes","regularDepartment"],
["Haute-Vienne", "87", "HV","Limousin","regularDepartment"],
["Vosges", "88", "VG","Lorraine","regularDepartment"],
["Yonne", "89", "YN","Bourgogne","regularDepartment"],
["Territoire de Belfort", "90", "TB","Franche-Comté","regularDepartment"],
["Essonne", "91", "ES","Île-de-France","regularDepartment"],
["Hauts-de-Seine", "92", "HI","Île-de-France","regularDepartment"],
["Seine-Saint-Denis", "93", "SD","Île-de-France","regularDepartment"],
["Val-de-Marne", "94", "VM","Île-de-France","regularDepartment"],
["Val-d’Oise", "95", "VO","Île-de-France","regularDepartment"]
]

usage = "usage: %prog [ [-n] [-a] [-l] [-r] ( NAME | NUMERICAL_CODE | ALPHBETIC_CODE ) | --list | -v | -vv ]"
parser = OptionParser(usage=usage, version="%prog 0.1")


parser.add_option("-n",  "--number",     help="print the number code of the department",                                 default=False, action="store_true", dest="number")
parser.add_option("-a",  "--alphabetic", help="print the two-letters reformed code of the department",                   default=False, action="store_true", dest="alpha")
parser.add_option("-l",  "--litteral",   help="print the full litteral name of the department",                          default=False, action="store_true", dest="lit")
parser.add_option("-r",  "--region",     help="print the full-name of the region witch the department is bellonging to", default=False, action="store_true", dest="reg")
parser.add_option("--list",              help="show a table of the departments with theres codes and exit",              default=False, action="store_true", dest="listing")
parser.add_option("-v",  "--verbose",    help="print the whole information on the output (it's like -nalr)",             default=False, action="store_true", dest="verbose")
parser.add_option("--vv",                help="print the whole information in a litteral sentence",                      default=False, action="store_true", dest="vverbose")

(options, args) = parser.parse_args()


# Determinate the department the user search from the numeric code, the alphabetic code and the full name as listed in  coresp[]
def askedDepartment(nuberOrCodeToEvaluate):
	for row in coresp:
		for cell in [row[0], row[1], row[2]]:
			if cell == nuberOrCodeToEvaluate:
				return row
	return False

# teling the program with verbose is like telling it with -narl
if options.verbose:
	options.number = True
	options.lit    = True
	options.alpha  = True
	options.reg    = True



if options.listing == False: # listing is for printing a complete table of correspondance
	findedDepratment = askedDepartment(sys.argv[2]) # evaluating witch departement the user is searching and import on findedDepartment the whol information about it to be treated.

	if findedDepratment:
		if options.vverbose:
			print("Departement de {0} en {1} de codes {2} (Réformé) et {3} (Insee).".format(findedDepratment[0], findedDepratment[3], findedDepratment[2], findedDepratment[1]))
		else:
			if options.lit:
				print findedDepratment[0],
			if options.reg:
				print findedDepratment[3],
			if options.alpha:
				print findedDepratment[2],
			if options.number:
				print findedDepratment[1],
	else:
		print("No department match the name or code \"{0}\".".format(sys.argv[2]))
		sys.exit(1)
