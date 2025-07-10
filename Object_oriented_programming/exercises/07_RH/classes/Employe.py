# classes/Employe.py

class Employe:
    id_counter = 0
    
    def __init__(self, nom : str, salaire : float):
        Employe.id_counter += 1
        self._nom = nom
        self._salaire = salaire
        self._id_employe = Employe.id_counter
        print(f"{self.nom} a rejoint notre glorieuse entreprise !")

    @property
    def nom(self):
        return self._nom

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, salaire):
        if isinstance(salaire, float):
            self._salaire = salaire
        else:
            raise ValueError

    @property
    def id_employe(self):
        return self._id_employe
    
    def presentation(self):
        return f"Je suis {self.nom}, mon ID est {self.id_employe}, et mon salaire est de {self.salaire}€"
    
    def augmenter_salaire(self, pourcentage):
        if (pourcentage > 0) and isinstance(pourcentage, float):
            self.salaire += self.salaire * (pourcentage / 100)
            print(f"Le nouveau salaire de {self.nom} est désormais de {self.salaire}, hoorah !")
        elif not isinstance(pourcentage, float):
            raise ValueError
        elif (pourcentage <= 0):
            print("Le montant ne peut pas être inférieur ou égale à 0")
        else:
            print("Une erreur empèche l'augementation du salaire")
    
    @classmethod
    def total_salaire(cls, liste_employes):
        total = 0
        for employe in liste_employes:
            total += employe.salaire
        return total



