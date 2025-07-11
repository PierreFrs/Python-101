# classes/Magazine.py
from classes.Media import Media

class Magazine(Media):
    def __init__(self, titre, auteur, annee, edition : str, disponible = True):
        super().__init__(titre, auteur, annee, disponible)
        self._edition = edition

    @property
    def edition(self):
        return self._edition

    def afficher_informations(self):
        return super().afficher_informations() + f", Edition : {self.edition}"
