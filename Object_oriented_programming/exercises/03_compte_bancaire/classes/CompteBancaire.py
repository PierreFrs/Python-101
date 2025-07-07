# classes/CompteBancaire.py

class CompteBancaire:
    def __init__(self, numero_compte : int, nom : str, solde : int):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        if montant > 0:
            self.solde += montant
        else:
            print("Le montant doit être supérieur à 0")

    def retrait(self, montant):
        if self.solde >= montant and montant > 0:
            self.solde -= montant
        else:
            print("Le retrait n'est pas possible")
        

    def agios(self):
        if self.solde < 0:
            self.solde -= abs(self.solde) * 0.05
        else:
            print("Des agios ne peuvent être prélevés si le compte est provisionné")

    def afficher(self):
        print("Vos informations de compte :")
        print(f"Numéro de compte : {self.numero_compte}")
        print(f"Nom : {self.nom}")
        print(f"Solde : {self.solde}")