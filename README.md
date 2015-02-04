frdepartment
============

`frdepartment` is a Python program <abbr title="Command Line Interface">CLI</abbr> which converts names of [french department](https://en.wikipedia.org/wiki/French_department) into theire codes and vice versa, according to [`ISO 3166-2:FR`](https://en.wikipedia.org/wiki/ISO_3166-2:FR).

This program also mainly provides the support of my own [reform](http://taniere.info/ordinator/pprojets/departement/) (French only) of numeric codes into alphabetic codes.

# Parameters

+ `-n`,  `--number`     prints the number code of the department
+ `-a`,  `--alphabetic` prints the two-letters reformed code of the department
+ `-l`,  `--litteral`   prints the full litteral name of the department
+ `-r`,  `--region`     prints the full name of the region witch the department is belonging
+ `--list`              shows a table of the departments with theres codes and exit
+ `-v`,  `--verbose`    prints the whole information on the output (it's like `-nalr`)
+ `--vv`                prints the whole information in a litteral sentence
