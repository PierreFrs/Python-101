# classes/Scientifique.py

from classes.Travailleur import Travailleur

class Scientifique(Travailleur):
    def __init__(self, prenom, telephone, email, nom_entreprise, adresse_entreprise, telephone_pro, disciplines : list[str], type_scientifique : str):
        super().__init__(prenom, telephone, email, nom_entreprise, adresse_entreprise, telephone_pro)
        self._disciplines = disciplines
        self.type_scientifique = type_scientifique

    @property
    def disciplines(self):
        return self._disciplines
    
    @property
    def type_scientifique(self):
        return self._type_scientifique
    
    def __str__(self):
        return f"{super().__str__()}, disciplines : {self.disciplines}, type : {self.type_scientifique}"