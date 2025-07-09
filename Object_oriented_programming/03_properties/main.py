### Properties ###
# @property @.setter
from classes.Chien import Chien

rex = Chien("Rex", 12, "Berger allemand")
toto = Chien("Toto", 5, "Berger suisse")

toto.nom = "15" # => error
print(toto.nom)

toto.aboyer()