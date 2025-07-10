class Carte:
    couleurs = ["trèfle", "coeur", "carreau", "pique"]
    
    def __init__(self, valeur : int, couleur : str):
        if valeur < 2 or valeur > 14:
            raise ValueError ("La valeur doit être comprise entre 2 et 14.")
        if couleur.lower() not in Carte.couleurs:
            raise ValueError("La carte doit être de couleure trèfle, coeur, carreau ou pique.")
        self._valeur = valeur
        self._couleur = couleur

    @property
    def valeur(self):
        return self._valeur
    
    @property
    def couleur(self):
        return self._couleur

    def __add__(self, other : "Carte"):
        return self.valeur + other.valeur
    
    def __sub__(self, other : "Carte"):
        return self.valeur - other.valeur
    
    def __gt__(self, other : "Carte"):
        return self.valeur > other.valeur
    
    def __lt__(self, other : "Carte"):
        return self.valeur < other.valeur
    
    def __eq__(self, other : "Carte"):
        return self.valeur == other.valeur
    
    def __contains__(self, couleur : str):
        if couleur in self.couleur:
            print(f"la carte est un {couleur}")
        else:
            print(f"la carte n'est pas un {couleur}")
    
    def __str__(self):
        return f"{self.couleur} {self.valeur}"