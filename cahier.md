Nom de la commande `frdepartment`

# Nomenclature
CA	: Code alphabêtique réformé
CN	: Code numérique
NOM	: Le nom littéral du départemet

# Comportement à implémenter
La commande doit pouvoir :
* Fournir le CA d’après le CN ;
* Fournir le CA d’après le NOM ;

* Fournir le CN d’après le CA ;
* Fournir le CN d’aiprès le NOM;

* Fournir le NOM d’après le CA ;
* Fournir le NOM d’après le CN ;

* Fournir la région d’après le CA ;
* Fournir la région d’après le CN ;
* Fournir la région d’après le NOM ;

Invoqué sans paramettre mais avec seulement l’un de CA ou CN, `frdepartement` devra retourner l’autre.

# Nom des paramettres

* `-n --number`     retourne le CN ;
* `-a --alphabetic` retourne le CA ;
* `-l --literal`    retourne le NOM ;
* `-r --region`     retourne la région ;
* `-v --verbose`    presente la sortie humainement lisible ;
* `-vv`             presente une sortie encore plus lisible


