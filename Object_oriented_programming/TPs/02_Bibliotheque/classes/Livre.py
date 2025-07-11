# classes/Livres.py
from classes.Media import Media

class Livre(Media):
    def __init__(self, titre, auteur, annee, nombre_de_pages : int, disponible = True):
        super().__init__(titre, auteur, annee, disponible)
        self._nombre_de_pages = nombre_de_pages

    @property
    def nombre_de_pages(self):
        return self._nombre_de_pages

    def afficher_informations(self):
        return super().afficher_informations() + f", Nombre de pages : {self.nombre_de_pages}"

