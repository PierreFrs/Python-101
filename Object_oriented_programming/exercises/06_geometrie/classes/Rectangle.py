# classes/Rectangle.py

class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    
    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur

    def perimetre(self):
        return (self.longueur + self.largeur) * 2
    
    def surface(self):
        return self.longueur * self.largeur