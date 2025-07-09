# classes/Parallelepipede.py

from classes.Rectangle import Rectangle

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
    
    @property
    def hauteur(self):
        return self._hauteur
    
    def perimetre(self):
        return (super().perimetre() + self.hauteur * 2) * 2
    
    def surface(self):
        return (super().surface() + self.largeur * self.hauteur + self.longueur * self.hauteur) * 2
    
    def volume(self):
        return super().surface() * self.hauteur