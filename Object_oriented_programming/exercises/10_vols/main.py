# main.py
from classes.VolDirect import VolDirect
from classes.Vols import Vols



def main():
    def saisie_jour():
        jours_valides = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

        while True:
            jour = input("Veuillez saisir un jour : ")
            if jour in jours:
                return jour
            else:
                print("Jour invalide !")

    def saisie_heure():
        while True:
            heure = int(input("Veuillez saisir l'heure de départ : "))
            if 0 <= heure < 24:
                return heure
            else:
                print("Heure invalide !")

    def saisie_ville():
        while True:
            ville = input("Veuillez saisir la ville : ")
            if ville != "":
                return ville
            else:
                print("Ville invalide !")

    lv : list[VolDirect]= []

    for i in range(3):
        print("Ajouter un vol :")
        dep = saisie_ville()
        arr = saisie_ville()
        jour = saisie_jour()
        heure = saisie_heure()

        lv.append(VolDirect(dep, arr, jour, heure))

    vols = Vols(lv)
    

    print("=== Liste des vols ===")
    vols.affiche()
    print()
    print(vols.appartient("Paris"))
    print(vols.appartient("Bruxelles"))
    print(vols.appartient("Bordeaux"))
    print()
    print(f"La liste des destinataires à partir de Paris est : {set(vols.liste_successeurs("Paris"))}")

main()