# classes/Gateau.py
class Gateau:
    def __init__(
            self, 
            nom : str, 
            temps_cuisson : int, 
            liste_ingredients : list[str], 
            etapes_recette : list[str], 
            nom_createur : str):
        self.nom = nom
        self.temps_cuisson = temps_cuisson
        self.liste_ingredients = liste_ingredients
        self.etapes_recette = etapes_recette
        self.nom_createur = nom_createur
    
    def afficher_ingredients(self):
        print(f"Ingrédients :")
        for ingredient in self.liste_ingredients:
            print(f"- {ingredient.title()}")
    
    def afficher_etapes(self):
        print(f"Etapes :")
        for etape in self.etapes_recette:
            print(f"- {etape}")

    def afficher_gateau(self):
        print(f"Recette pour : {self.nom} par {self.nom_createur}")
        self.afficher_ingredients()
        self.afficher_etapes()