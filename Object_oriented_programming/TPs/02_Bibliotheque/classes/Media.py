# classes/Media.py
class Media:
    def __init__(self, titre : str, auteur : str, annee : int, disponible : bool = True):
        self._titre = titre
        self._auteur = auteur
        self._annee = annee
        self._disponible = disponible

    @property
    def titre(self):
        return self._titre

    @property
    def auteur(self):
        return self._auteur

    @property
    def annee(self):
        return self._annee

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        if isinstance(value, bool):
            self._disponible = value
        else:
            raise ValueError
    
    def afficher_informations(self):
        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année : {self.annee}, Disponible : {self.disponible}"
    
    def changer_disponibilite(self):
        self.disponible != self.disponible