# Class definition
class Chien:
    def __init__(self, nom, age, race): # self => this
        self.nom = nom
        self.age = age
        self.race = race
        print(f"Naissance de {self.nom} !")

    def aboyer(self):
        print(f"{self.nom} waf waf")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")