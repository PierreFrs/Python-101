### Class attributes ###
from classes.Chien import Chien

rex = Chien("Rex", 12, "Berger allemand")
toto = Chien("Toto", 5, "Berger suisse")

# print(Chien.instance_chien)
# print(rex.instance_chien)
# print(toto.instance_chien)
toto.afficher_nombre_chiens()
rex.afficher_nombre_chiens()
Chien.afficher_nombre_chiens()