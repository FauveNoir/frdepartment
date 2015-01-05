#!/usr/bin/env python
# -*- coding: utf-8 -*-
# frdepartment : mainfile

import cli.app # probably not necessary
import sys
from optparse import OptionParser
from tabulate import tabulate
import argparse
from termcolor import colored

class bcolors:
	WARNING = '\033[01;31m' # Red
	ENDC    = '\033[0m'
	MAIN    = '\033[1m'
	ADEP    = '\033[01;31m' # Alphabetic code of department in red bold
	LITN    = '\033[1m' # fullname of department in white bold

coresp = [
["Ain", "01", "AN","Rhône-Alpes","metropolitan-department"],
["Aisne", "02", "AS","Picardie","metropolitan-department"],
["Allier", "03", "AL","Auvergne","metropolitan-department"],
["Alpes-de-Haute-Provence", "04", "AH","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Hautes-Alpes", "05", "HA","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Alpes-Maritimes", "06", "AM","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Ardèche", "07", "AC","Rhône-Alpes","metropolitan-department"],
["Ardennes", "08", "AR","Champagne-Ardenne","metropolitan-department"],
["Ariège", "09", "AG","Midi-Pyrénées","metropolitan-department"],
["Aube", "10", "AB","Champagne-Ardenne","metropolitan-department"],
["Aude", "11", "AD","Languedoc-Roussillon","metropolitan-department"],
["Aveyron", "12", "AV","Midi-Pyrénées","metropolitan-department"],
["Bouches-du-Rhône", "13", "BR","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Calvados", "14", "CV","Basse-Normandie","metropolitan-department"],
["Cantal", "15", "CT","Auvergne","metropolitan-department"],
["Charente", "16", "CH","Poitou-Charentes","metropolitan-department"],
["Charente-Maritime", "17", "CM","Poitou-Charentes","metropolitan-department"],
["Cher", "18", "CR","Centre","metropolitan-department"],
["Corrèze", "19", "CZ","Limousin","metropolitan-department"],
["Corse-du-sud", "2A", "CS","Corse","metropolitan-department"],
["Haute-Corse", "2B", "HC","Corse","metropolitan-department"],
["Côte-d’Or", "21", "CO","Bourgogne","metropolitan-department"],
["Côtes-d’Armor", "22", "CA","Bretagne","metropolitan-department"],
["Creuse", "23", "CE","Limousin","metropolitan-department"],
["Dordogne", "24", "DG","Aquitaine","metropolitan-department"],
["Doubs", "25", "DB","Franche-Comté","metropolitan-department"],
["Drôme", "26", "DM","Rhône-Alpes","metropolitan-department"],
["Eure", "27", "ER","Haute-Normandie","metropolitan-department"],
["Eure-et-Loir", "28", "EL","Centre","metropolitan-department"],
["Finistère", "29", "FI","Bretagne","metropolitan-department"],
["Gard", "30", "GA","Languedoc-Roussillon","metropolitan-department"],
["Haute-Garonne", "31", "HG","Midi-Pyrénées","metropolitan-department"],
["Gers", "32", "GR","Midi-Pyrénées","metropolitan-department"],
["Gironde", "33", "GD","Aquitaine","metropolitan-department"],
["Hérault", "34", "HT","Languedoc-Roussillon","metropolitan-department"],
["Ille-et-Vilaine", "35", "IV","Bretagne","metropolitan-department"],
["Indre", "36", "ID","Centre","metropolitan-department"],
["Indre-et-Loire", "37", "IL","Centre","metropolitan-department"],
["Isère", "38", "IS","Rhône-Alpes","metropolitan-department"],
["Jura", "39", "JR","Franche-Comté","metropolitan-department"],
["Landes", "40", "LD","Aquitaine","metropolitan-department"],
["Loir-et-Cher", "41", "LC","Centre","metropolitan-department"],
["Loire", "42", "LR","Rhône-Alpes","metropolitan-department"],
["Haute-Loire", "43", "HL","Auvergne","metropolitan-department"],
["Loire-Atlantique", "44", "LA","Pays de la Loire","metropolitan-department"],
["Loiret", "45", "LT","Centre","metropolitan-department"],
["Lot", "46", "LO","Midi-Pyrénées","metropolitan-department"],
["Lot-et-Garonne", "47", "LG","Aquitaine","metropolitan-department"],
["Lozère", "48", "LZ","Languedoc-Roussillon","metropolitan-department"],
["Maine-et-Loire", "49", "ML","Pays de la Loire","metropolitan-department"],
["Manche", "50", "MN","Basse-Normandie","metropolitan-department"],
["Marne", "51", "MR","Champagne-Ardenne","metropolitan-department"],
["Haute-Marne", "52", "HM","Champagne-Ardenne","metropolitan-department"],
["Mayenne", "53", "MY","Pays de la Loire","metropolitan-department"],
["Meurthe-et-Moselle", "54", "MM","Lorraine","metropolitan-department"],
["Meuse", "55", "MS","Lorraine","metropolitan-department"],
["Morbihan", "56", "MH","Bretagne","metropolitan-department"],
["Moselle", "57", "MO","Lorraine","metropolitan-department"],
["Nièvre", "58", "NV","Bourgogne","metropolitan-department"],
["Nord", "59", "ND","Nord-Pas-de-Calais","metropolitan-department"],
["Oise", "60", "OI","Picardie","metropolitan-department"],
["Orne", "61", "OR","Basse-Normandie","metropolitan-department"],
["Pas-de-Calais", "62", "PC","Nord-Pas-de-Calais","metropolitan-department"],
["Puy-de-Dôme", "63", "PD","Auvergne","metropolitan-department"],
["Pyrénées-Atlantiques", "64", "PA","Aquitaine","metropolitan-department"],
["Hautes-Pyrénées", "65", "HP","Midi-Pyrénées","metropolitan-department"],
["Pyrénées-Orientales", "66", "PO","Languedoc-Roussillon","metropolitan-department"],
["Bas-Rhin", "67", "BH","Alsace","metropolitan-department"],
["Haut-Rhin", "68", "HR","Alsace","metropolitan-department"],
["Rhône", "69", "RÔ","Rhône-Alpes","metropolitan-department"],
["Haute-Saône", "70", "HS","Franche-Comté","metropolitan-department"],
["Saône-et-Loire", "71", "SL","Bourgogne","metropolitan-department"],
["Sarthe", "72", "ST","Pays de la Loire","metropolitan-department"],
["Savoie", "73", "SV","Rhône-Alpes","metropolitan-department"],
["Haute-Savoie", "74", "HO","Rhône-Alpes","metropolitan-department"],
["Paris", "75", "PR","Île-de-France","metropolitan-department"],
["Seine-Maritime", "76", "SR","Haute-Normandie","metropolitan-department"],
["Seine-et-Marne", "77", "SM","Île-de-France","metropolitan-department"],
["Yvelines", "78", "YV","Île-de-France","metropolitan-department"],
["Deux-Sèvres", "79", "DS","Poitou-Charentes","metropolitan-department"],
["Somme", "80", "SO","Picardie","metropolitan-department"],
["Tarn", "81", "TR","Midi-Pyrénées","metropolitan-department"],
["Tarn-et-Garonne", "82", "TG","Midi-Pyrénées","metropolitan-department"],
["Var", "83", "VR","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Vaucluse", "84", "VA","Provence-Alpes-Côte d’Azur","metropolitan-department"],
["Vendée", "85", "VD","Pays de la Loire","metropolitan-department"],
["Vienne", "86", "VI","Poitou-Charentes","metropolitan-department"],
["Haute-Vienne", "87", "HV","Limousin","metropolitan-department"],
["Vosges", "88", "VG","Lorraine","metropolitan-department"],
["Yonne", "89", "YN","Bourgogne","metropolitan-department"],
["Territoire de Belfort", "90", "TB","Franche-Comté","metropolitan-department"],
["Essonne", "91", "ES","Île-de-France","metropolitan-department"],
["Hauts-de-Seine", "92", "HI","Île-de-France","metropolitan-department"],
["Seine-Saint-Denis", "93", "SD","Île-de-France","metropolitan-department"],
["Val-de-Marne", "94", "VM","Île-de-France","metropolitan-department"],
["Val-d’Oise", "95", "VO","Île-de-France","metropolitan-department"],

["Saint-Barthélemy", "977", "BL", None, "overseas-collectivity", "ISO 3166-2:BL"],
["Saint-Martin", "978", "MF", None, "overseas-collectivity", "ISO 3166-2:MF"],
["Nouvelle-Calédonie", "988", "NC", None, "overseas-collectivity", "ISO 3166-2:NC"],
["Polynésie française", "987", "PF", None, "overseas-collectivity", "ISO 3166-2:PF"],
["Saint-Pierre-et-Miquelon", "975", "PM", None, "overseas-collectivity", "ISO 3166-2:PM"],
["Terres australes françaises", "984", "TF", None, "overseas-collectivity", "ISO 3166-2:TF"],
["Wallis-et-Futuna", "986", "WF", None, "overseas-collectivity", "ISO 3166-2:WF"],

["Île de Clipperton", "989", "CP", None, "dependency", "ISO 3166-2:WF"],

["Guyane française", "973", "GF", None, "overseas-departments", "ISO 3166-2:GF"],
["Guadeloupe", "971", "GP", None, "overseas-departments", "ISO 3166-2:GP"],
["Martinique", "972", "MQ", None, "overseas-departments", "ISO 3166-2:MQ"],
["Réunion", "974", "RE", None, "overseas-departments", "ISO 3166-2:RE"],
["Mayotte", "976", "YT", None, "overseas-departments", "ISO 3166-2:YT"],
["Wallonie", None, "WL", None, "easter-egg"]
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

def codeOrNumberOrLitt(aDepartment,numberOrCode):
        if   numberOrCode in [aDepartment[0], aDepartment[1]]:
                return 0
        elif aDepartment[2] == numberOrCode:
                return 1


if len(sys.argv) < 2:
	sys.exit(1)

# teling the program with verbose is like telling it with -narl
if options.verbose:
	options.number = True
	options.lit    = True
	options.alpha  = True
	options.reg    = True


if options.listing: # listing is for printing a complete table of correspondance

	tableOfMetropolitanDepartment = []
	print bcolors.MAIN + "Départements métropolitains\n" + bcolors.ENDC
	for row in coresp:
		if row[4] == "metropolitan-department":
			tableOfMetropolitanDepartment.append([ row[0].decode('utf-8'), row[2].decode('utf-8'), row[1].decode('utf-8'), row[3].decode('utf-8') ])
	print tabulate(tableOfMetropolitanDepartment, headers=["Département".decode('utf-8'), "Code alphabétique".decode('utf-8'), "Code numérique".decode('utf-8'), "Région".decode('utf-8')])

	tableOfOverseasDepartment = []
	print bcolors.MAIN + "\n\nRégions mono-départementales d’outre-mer\n" + bcolors.ENDC
	for row in coresp:
		if row[4] == "overseas-departments":
			tableOfOverseasDepartment.append([ row[0].decode('utf-8'), row[2].decode('utf-8'), row[1].decode('utf-8') ])
	print tabulate(tableOfOverseasDepartment, headers=["Département".decode('utf-8'), "Code alphabétique".decode('utf-8'), "Code numérique".decode('utf-8') ])

	tableOfDpendency = []
	print bcolors.MAIN + "\n\nDépendances\n" + bcolors.ENDC
	for row in coresp:
		if row[4] == "dependency":
			tableOfDpendency.append([ row[0].decode('utf-8'), row[2].decode('utf-8'), row[1].decode('utf-8') ])
	print tabulate(tableOfDpendency, headers=["Département".decode('utf-8'), "Code alphabétique".decode('utf-8'), "Code numérique".decode('utf-8') ])

	tableOfOverseasCollectivity = []
	print bcolors.MAIN + "\n\nTerritoires mono-départementaux d’outre-mer\n" + bcolors.ENDC
	for row in coresp:
		if row[4] == "overseas-collectivity":
			tableOfOverseasCollectivity.append([ row[0].decode('utf-8'), row[2].decode('utf-8'), row[1].decode('utf-8') ])
	print tabulate(tableOfOverseasCollectivity, headers=["Département".decode('utf-8'), "Code alphabétique".decode('utf-8'), "Code numérique".decode('utf-8') ])



else: # listing is for printing a complete table of correspondance
        if len(sys.argv) > 2:
        	findedDepratment = askedDepartment(sys.argv[2]) # evaluating witch departement the user is searching and import on findedDepartment the whol information about it to be treated.
                isCodeOrNumberOrLitt = None
        else:
        	findedDepratment = askedDepartment(sys.argv[1]) # evaluating witch departement the user is searching and import on findedDepartment the whol information about it to be treated.
                isCodeOrNumberOrLitt = codeOrNumberOrLitt(findedDepratment,sys.argv[1])

	if findedDepratment[4] == "easter-egg":
		print("IPoT n’étant pas implémenté sur ce système, frdepartment ne peut assurer que la Wallonie sera un département français.")


	elif findedDepratment:
		if findedDepratment[0][0] in ("A", "U", "E", "I", "Y", "Î", "O"): #This test is for french syntax. Because in french languages, words begining by a voyel have to be preceded with “l’” and words  begining with a console, wave to be preced by noting.
			linguisticConjonction = "l’"
		else: # Other cases is a console.
			linguisticConjonction = ""

		if options.vverbose:

			if findedDepratment[4] == "metropolitan-department":
				print("Departement de {4}{0} en {1} de codes {2} (Réformé) et {3} (Insee).".format(bcolors.LITN + findedDepratment[0] + bcolors.ENDC, findedDepratment[3], bcolors.ADEP + findedDepratment[2] + bcolors.ENDC, findedDepratment[1], linguisticConjonction))

			elif findedDepratment[4] == "overseas-departments":
				print("Région et département d’Outre-mer de {4}{0} de codes {2} (ISO 3166-2:FR) et {3} (Insee).".format(bcolors.LITN + findedDepratment[0] + bcolors.ENDC, findedDepratment[3], bcolors.ADEP + findedDepratment[2] + bcolors.ENDC, findedDepratment[1], linguisticConjonction))
				if findedDepratment[5]:
					print "voir aussi", findedDepratment[5] + "."

			elif findedDepratment[4] == "overseas-collectivity":
				print("Territoire monodepartemental d’Outre-mer de {4}{0} de codes {2} (ISO 3166-2:FR) et {3} (Insee).".format(bcolors.LITN + findedDepratment[0] + bcolors.ENDC, findedDepratment[3], bcolors.ADEP + findedDepratment[2] + bcolors.ENDC, findedDepratment[1], linguisticConjonction))
				if findedDepratment[5]:
					print "voir aussi", findedDepratment[5] + "."

			elif findedDepratment[4] == "dependency":
				print("Dépendance de {4}{0} de codes {2} (ISO 3166-2:FR) et {3} (Insee).".format(bcolors.LITN + findedDepratment[0] + bcolors.ENDC, findedDepratment[3], bcolors.ADEP + findedDepratment[2] + bcolors.ENDC, findedDepratment[1], linguisticConjonction))
				if findedDepratment[5]:
					print "voir aussi", findedDepratment[5] + "."

		else:
			if options.reg and findedDepratment[4] != "metropolitan-department": # For overseas departement, terretiories and dependencies witch not bellong to any region.
				print bcolors.WARNING + "*" + bcolors.ENDC, "Le térritoire de {0}{1} est".format(linguisticConjonction, findedDepratment[0]),

				if findedDepratment[4] == "overseas-departments":
					print "une région mono-départementale d’outre mer."

				elif findedDepratment[4] == "overseas-collectivity":
					print "un département d’outre-mer non-régionnalisé."

				elif findedDepratment[4] == "dependency":
					print "une dépendance non-régionnalisé."

			elif options.lit:
				print bcolors.LITN + findedDepratment[0] + bcolors.ENDC,
			elif options.reg and findedDepratment[4] == "metropolitan-department":
				print findedDepratment[3],

			elif (options.alpha) or ( (not (options.number and options.alpha and options.lit and options.reg and options.listing and options.verbos and options.vverbose) ) and (isCodeOrNumberOrLitt == 0) ):
				print bcolors.ADEP + findedDepratment[2] + bcolors.ENDC,
			elif (options.number) or ( (not (options.number and options.alpha and options.lit and options.reg and options.listing and options.verbos and options.vverbose) ) and (isCodeOrNumberOrLitt == 1) ):
				print findedDepratment[1],

	else:
		print bcolors.WARNING + "*" + bcolors.ENDC,"No department match the name or code \"{0}\".".format(sys.argv[2])
		sys.exit(1)
