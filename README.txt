TP1 - CLASSES DIVINES:
==============================================

- Ryan Azoune - 20162578
- Celina Ghoraieb-Munoz - 20106039

==============================================

- Repositoire : https://github.com/munozcel/IFT3913-TP1

==============================================

Documentation:
--------------

Pour jls.py:
------------
Ce programme prend en entrée le chemin d'accès d'un dossier et produit en sortie un fichier CSV avec les colonnes:
- Chemin du fichier
- Nom du paquet
- Nom de la classe

Vous pouvez entrer dans la ligne de commande:
Par exemple:
python3 jls.py --path "ckjm/src/gr" > jls.csv
Où vous pouvez mettre le path de votre choix entre les " "
python3 jls.py --path "PATH" > jls.csv

Pour nvloc.js
-------------
Ce programme calcule le nombre de lignes de code non-vides

Vous pouvez entrer dans la ligne de commande:
Par exemple:
python3 nvloc.py --path "ckjm/src/gr/spinellis/ckjm/MethodVisitor.java"
Où vous pouvez mettre le path de votre choix entre les " "
python3 nvloc.py --path "PATH"

Pour lcsec.js
-------------
Ce programme prend comme entrée le chemin d'un dossier et crée en sortie un fichier CSV avec les même colonnes que
jls.py, mais également la métrique de couplage CSEC donc:
- Chemin du fichier
- Nom du paquet
- Nom de la classe
- Métrique de couplage CSEC

Vous pouvez entrer dans la ligne de commande:
Par exemple:
python lcsec.py --dir_path "ckjm/src/gr" --jls_path "jls.csv"
Où vous pouvez mettre le path de votre choix entre les " "

Pour egon.js
-------------
Ce programme compare les seuils supérieurs de toutes les classes dans le dossier et sous-dossiers en utilisant les
métriques NVLOC et CSEC.

Vous pouvez entrer dans la ligne de commande:
Par exemple:
En crént un fichier CSV:
python3 egon.py --path jfreechart/src/main/java/ --seuil 0.01> egon_top1.csv
python3 egon.py --path jfreechart/src/main/java/ --seuil 0.05 > egon_top05.csv
python3 egon.py --path jfreechart/src/main/java/ --seuil 0.10 > egon_top10.csv

Ou dans en imprimant dans la ligne de commande:
python3 egon.py --path "jfreechart/src/main/java/" --seuil 0.05










