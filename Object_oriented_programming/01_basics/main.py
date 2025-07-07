from classes.Chien import Chien

rex = Chien("Rex", 12, "Berger allemand")
toto = Chien("Toto", 5, "Berger suisse")

rex.aboyer()
rex.aboyer_sur(toto)
toto.aboyer_sur(rex)