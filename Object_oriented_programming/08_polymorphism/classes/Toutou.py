from classes.Animal import Animal
from classes.Carnivore import Carnivore

class Toutou(Animal, Carnivore):
    def __init__(self, nom, age):
        Animal.__init__(self, nom)
        Carnivore.__init__(self, age)

    def se_nourrir(self):
        Animal.se_nourrir(self)