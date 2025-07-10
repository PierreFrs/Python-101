# classes/VolDirect.py

class VolDirect:
    def __init__(self, dep : str, arr : str, jour : str, heure : int):
        self._dep = dep
        self._arr = arr
        self._jour = jour
        self._heure = heure

    @property
    def dep(self):
        return self._dep

    @property
    def arr(self):
        return self._arr

    @property
    def jour(self):
        return self._jour

    @property
    def heure(self):
        return self._heure

    def affiche(self):
        print(f"Ce vol part de {self.dep} vers {self.arr} le {self.jour} à {self.heure} heure.")