#!/usr/bin/env python
import cli.app

@cli.app.CommandLineApp
def frdepartment(app):
	pass

frdepartment.add_param("-n",  "--number",     help="Print the number code of the department",                                 default=False, action="store_true")
frdepartment.add_param("-a",  "--alphabetic", help="Print the two-letters reformed code of the department",                   default=False, action="store_true")
frdepartment.add_param("-l",  "--litteral",   help="Print the full litteral name of the department",                          default=False, action="store_true")
frdepartment.add_param("-r",  "--region",     help="Print the full-name of the region witch the department is bellonging to", default=False, action="store_true")
frdepartment.add_param("-v",  "--verbose",    help="Print the whole information on the output (it's like -nalr)",             default=False, action="store_true")
frdepartment.add_param("-vv",                 help="Print the whole information in a litteral sentence ",                     default=False, action="store_true")

if __name__ == "__main__":
	frdepartment.run()
