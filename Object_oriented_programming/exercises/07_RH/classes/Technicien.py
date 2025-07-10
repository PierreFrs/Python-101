# classes/Technicien.py
from classes.Employe import Employe

class Technicien(Employe):
    def __init__(self, nom, salaire, specialite : str):
        super().__init__(nom, salaire)
        self._specialite = specialite

    @property
    def specialite(self):
        return self._specialite

    @specialite.setter
    def specialite(self, specialite):
        if isinstance(specialite, str):
            self._specialite = specialite
        else:
            raise ValueError
    
    def changer_specialite(self, nouvelle_spe : str):
        if nouvelle_spe != "" and isinstance(nouvelle_spe, str):
            self.specialite = nouvelle_spe
            print(f"La nouvelle spécialisté de {self.nom} est désormais : {self.specialite}.")
        elif nouvelle_spe == "":
            print("La nouvelle spécialité ne peut pas être nulle")
        else:
            raise ValueError
    
    def presentation(self):
        return f"Je suis {self.nom}, technicien spécialisé en {self.specialite}. Mon ID est {self.id_employe} et mon salaire est de {self.salaire}€."