# classes/WaterTank.py
class WaterTank:
    volume_total = 0
    def __init__(self, poids_vide : float, capacite_max : float, niveau_remplissage : float):
        self._poids_vide = poids_vide
        self._capacite_max = capacite_max
        self._niveau_remplissage = niveau_remplissage
        WaterTank.volume_total += niveau_remplissage

    @property
    def poids_vide(self):
        return self._poids_vide

    @poids_vide.setter
    def poids_vide(self, poids_vide):
        if isinstance(poids_vide, float):
            self._poids_vide = poids_vide
        else:
            raise ValueError

    @property
    def capacite_max(self):
        return self._capacite_max

    @capacite_max.setter
    def capacite_max(self, capacite_max):
        if isinstance(capacite_max, float):
            self._capacite_max = capacite_max
        else:
            raise ValueError

    @property
    def niveau_remplissage(self):
        return self._niveau_remplissage

    @niveau_remplissage.setter
    def niveau_remplissage(self, niveau_remplissage):
        if isinstance(niveau_remplissage, float):
            self._niveau_remplissage = niveau_remplissage
        else:
            raise ValueError

    def poids_total(self):
        print(f"Le poids total de la citerne est de {self.poids_vide + self.niveau_remplissage} litres.")

    def remplir_citerne(self, volume):
        if self.niveau_remplissage + volume <= self.capacite_max:
            self.niveau_remplissage += volume
            WaterTank.volume_total += volume
        else:
            WaterTank.volume_total += self.capacite_max - self.niveau_remplissage
            self.niveau_remplissage = self.capacite_max
            print("Le volume à ajouter excède la capacité maximale de la citerne.")
        print(f"La citerne contient désormais {self.niveau_remplissage} litres d'eau.")

    def vider_citerne(self, volume):
        if self._niveau_remplissage - volume >= 0:
            self._niveau_remplissage -= volume
            WaterTank.volume_total -= volume
            print(f"{volume} litres d'eau ont été retirés, la citerne contient désormais {self._niveau_remplissage} litres d'eau.")
        else:
            self.niveau_remplissage = 0.0
            print("La citerne est vide.")
    

    @classmethod
    def afficher_volume_total(cls):
        print(f"L'ensemble des citernes contient {cls.volume_total} litres d'eau.")
    
