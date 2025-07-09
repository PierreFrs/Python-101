from classes.Vehicle import Vehicle

class Voiture(Vehicle):
    def __init__(self, marque, couleur, motorisation, nb_portes):
        super().__init__(marque, couleur, motorisation)
        self.nb_portes = nb_portes

    def decrire(self):
        return f"{super().decrire()} - porte : {self.nb_portes}"