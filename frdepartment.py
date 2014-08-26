#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cli.app # probably not necessary
import argparse
from optparse import OptionParser

progname = "frdepartment"

usage = "usage: %prog [ [-n] [-a] [-l] [-r] ( NAME | NUMERICAL_CODE | ALPHBETIC_CODE ) | --list | -v | -vv ]"
parser = OptionParser(usage=usage, version="%prog 0.1")


parser.add_option("-n",  "--number",     help="print the number code of the department",                                 default=False, action="store_true")
parser.add_option("-a",  "--alphabetic", help="print the two-letters reformed code of the department",                   default=False, action="store_true")
parser.add_option("-l",  "--litteral",   help="print the full litteral name of the department",                          default=False, action="store_true")
parser.add_option("-r",  "--region",     help="print the full-name of the region witch the department is bellonging to", default=False, action="store_true")
parser.add_option("--list",              help="show a table of the departments with theres codes and exit",              default=False, action="store_true", dest="verbose")
parser.add_option("-v",  "--verbose",    help="print the whole information on the output (it's like -nalr)",             default=False, action="store_true", dest="verbose")
parser.add_option("--vv",                help="print the whole information in a litteral sentence",                     default=False, action="store_true", dest="verbose")

(options, args) = parser.parse_args()
<<<<<<< HEAD


def askedDepartment(nuberOrCodeToEvaluate):
	for row in coresp:
		for cell in [row[0], row[1], row[2]]:
			if cell == nuberOrCodeToEvaluate:
				return row

if sys.argv[1] != ['-h', '-v', '--vv', '--list']:
	print askedDepartment(sys.argv[2])
=======
>>>>>>> parent of 76a4a61... The correspondance table was added and now, the script is responding
