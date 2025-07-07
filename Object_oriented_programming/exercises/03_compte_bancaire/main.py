# main.py
from classes.CompteBancaire import CompteBancaire

compte_de_francis = CompteBancaire(1234567890, "Francis", 100)

def main():
    compte_de_francis.afficher()
    compte_de_francis.versement(5)
    compte_de_francis.afficher()
    compte_de_francis.retrait(205)
    compte_de_francis.afficher()
    compte_de_francis.agios()
    compte_de_francis.afficher()

main()