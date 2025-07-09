# classes/CompteBancaire.py

class CompteBancaire:
    def __init__(self, numero_compte : int, nom : str, solde : int):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Votre nouveau solde est de {self.solde}€")
        else:
            print("Le montant doit être supérieur à 0")

    def retrait(self, montant):
            self.solde -= montant
            print(f"Votre nouveau solde est de {self.solde}€")

    def agios(self):
        if self.solde < 0:
            self.solde -= abs(self.solde) * 0.05
            print(f"Votre nouveau solde est de {self.solde}€")
        else:
            print("Des agios ne peuvent être prélevés si le compte est provisionné")

    def afficher(self):
        print("Vos informations de compte :")
        print(f"Numéro de compte : {self.numero_compte}")
        print(f"Nom : {self.nom}")
        print(f"Solde : {self.solde}")