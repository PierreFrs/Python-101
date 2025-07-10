# classes/Vols

from classes.VolDirect import VolDirect

class Vols:
    def __init__(self, liste_vols : list[VolDirect] = []):
        self._liste_vols = liste_vols

    @property
    def liste_vols(self):
        return self._liste_vols

    @liste_vols.setter
    def liste_vols(self, value):
        if isinstance(value, list[VolDirect]):
            self._liste_vols = value
        else:
            raise ValueError

    def liste_successeurs(self, ville_depart):
        return [vol.arr for vol in self.liste_vols if vol.dep == ville_depart]
    
    def appartient(self, ville):
        for vol in self.liste_vols:
            if vol.dep == ville or vol.arr == ville:
                True
        return False
    
    def affiche(self):
        for vol in self.liste_vols:
            vol.affiche()