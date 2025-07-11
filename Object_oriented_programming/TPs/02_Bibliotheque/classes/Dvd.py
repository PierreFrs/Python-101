# classes/Dvd.py
from classes.Media import Media

class Dvd(Media):
    def __init__(self, titre, auteur, annee, duree : int, disponible = True):
        super().__init__(titre, auteur, annee, disponible)
        self._duree = duree

    @property
    def duree(self):
        return self._duree

    def afficher_informations(self):
        return super().afficher_informations() + f", Durée (en minutes) : {self.duree}"