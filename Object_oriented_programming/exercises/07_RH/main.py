# main.py
from classes.Employe import Employe
from classes.Manager import Manager
from classes.Technicien import Technicien

def filtrer_par_role(liste_employe : list):
    employes = []
    managers = []
    techniciens = []

    for employe in liste_employe:
        match employe:
            case Manager():
                managers.append(employe)
            case Technicien():
                techniciens.append(employe)
            case Employe():
                employes.append(employe)
            case _:
                raise ValueError
    
    return employes, managers, techniciens

def afficher_roles(employes, managers, techniciens):

    print("Liste des employés simples : ")
    for employe in employes:
        print(f"    - {employe.nom}")

    print("Liste des techniciens : ")
    for technicien in techniciens:
        print(f"    - {technicien.nom}")

    print("Liste des managers : ")
    for manager in managers:
        print(f"    - {manager.nom}")

# Tests classe Employe
employe1 = Employe("Michel", 25000.0)
employe2 = Employe("Joséphine", 26000.0)
employe3 = Employe("Morgan", 23000.0)

print(employe1.presentation())
print(employe2.presentation())

employe1.augmenter_salaire(5.4)

Employe.total_salaire([employe1, employe2])

# Tests classe Technicien
technicien1 = Technicien("Paul", 32000.0, "Systèmes et réseaux")
technicien2 = Technicien("Rachel", 32000.0, "Infrastructure Cloud")

print(technicien1.presentation())
print(technicien2.presentation())

technicien1.changer_specialite("Data Management")

# Tests classe Manager
manager1 = Manager("Bernadette", 35000.0, [employe1, technicien1])
manager2 = Manager("Kevin", 36000.0, [employe2, technicien2])

manager1.ajouter_employe(employe3)

print(manager1.presentation())
print(manager2.presentation())


# Test listes
employes_list, managers_list, techniciens_list = filtrer_par_role([employe1, employe2, employe3, technicien1, technicien2, manager1, manager2])
afficher_roles(employes_list, managers_list, techniciens_list)



