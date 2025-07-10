# classes/Manager.py
from classes.Employe import Employe

class Manager(Employe):
    def __init__(self, nom, salaire, equipe : list):
        super().__init__(nom, salaire)
        self._equipe = equipe

    @property
    def equipe(self):
        return self._equipe

    @equipe.setter
    def equipe(self, equipe):
        if isinstance(equipe, list):
            self._equipe = equipe
        else:
            raise ValueError
        
    def ajouter_employe(self, employe : Employe):
        if isinstance(employe, Employe):
            self.equipe.append(employe)
            print(f"{employe.nom} a rejoint l'équipe de {self.nom}.")
        else:
            raise ValueError
    
    def presentation(self):
        names = ", ".join([emp.nom for emp in self.equipe])
        return f"Je suis {self.nom}, manager. Mon ID est {self.id_employe}. Je supervise une équipe de {len(self.equipe)} personnes : {names}. Mon salaire est de {self.salaire}€."