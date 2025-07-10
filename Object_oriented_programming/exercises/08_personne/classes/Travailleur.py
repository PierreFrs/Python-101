# classes/Travailler.py
from classes.Personne import Personne

class Travailleur(Personne):
    def __init__(self, prenom, telephone, email, nom_entreprise : str, adresse_entreprise : str, telephone_pro : str):
        super().__init__(prenom, telephone, email)
        self._nom_entreprise = nom_entreprise
        self._adresse_entreprise = adresse_entreprise
        self._telephone_pro = telephone_pro

    @property
    def nom_entreprise(self):
        return self._nom_entreprise
    
    @property
    def adresse_entreprise(self):
        return self._adresse_entreprise
    
    @property
    def telephone_pro(self):
        return self._telephone_pro
    
    def __str__(self):
        return f"{super().__str__()}, Nom de l'entreprise : {self.nom_entreprise}, Adresse de l'entreprise : {self.adresse_entreprise}, Téléphone professionnel : {self.telephone_pro}"