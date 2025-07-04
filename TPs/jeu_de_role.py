import random

def create_character(nom, classe):
    return {
        "nom" : nom,
        "classe" : classe,
        "niveau" : 1,
        "pointsDeVie" : 100,
        "inventaire" : [
            {
            "nom" : "potion_de_soin", 
            "quantité" : 3
            }
        ]
    }

# def ajouter_objet(inventaire, nom, quantite):
#     for item in inventaire:
#         if item["nom"] == nom:
#             item["quantite"] += quantite
#             break
#     else:
#         inventaire.append({"nom" : nom, "quantité" : quantite})

# Avec KwArgs
def ajouter_objet(inventaire, **objets):
    for nom, quantite in objets.items():
        for item in inventaire:
            if item["nom"] == nom:
                item["quantite"] += quantite
                break
    else:
        inventaire.append({"nom" : nom, "quantité" : quantite})

def modifier_statistiques(personnage):
    personnage["niveau"] += 1
    personnage["pointsDeVie"] += 20

def utiliser_potion(personnage):
    for item in personnage["inventaire"]:
        if item["nom"] == "potion_de_soin" and item["quantité"] > 0:
            item["quantité"] -= 1
            points_gagnes = random.randint(1, 50)
            personnage["pointsDeVie"] += points_gagnes
            print(f"{personnage["nom"]} prend une potion_de_soin et gagne {points_gagnes} points de vie !")
            if item["quantite"] == 0:
                personnage["inventaire"].remove(item)
        else:
            print("Vous n'avez plus de potion !!!")

def afficher_personnage(personnage):
    print("Vos stats :")
    for key, value in personnage.items():
        if type(value) == list:
            for el in value:
                for key, value in el.items():
                    print(f"        {key.title()} : {value}")
        else:
            print(f"    {key.title()} : {value}")
    print("-"*50)
    print()

def afficher_pointsDeVies(personnage):
    print(f"Points de vies de {personnage["nom"]} : {personnage["pointsDeVie"]}")

def attaquer(attaquant, adversaire):
    degats = attaquant["niveau"] * 10
    print(f"{attaquant["nom"]} attaque {adversaire["nom"]} et lui inflige {degats} points de dégâts !")
    adversaire["pointsDeVie"] -= degats
    if adversaire["pointsDeVie"] <= 0:
        for item in adversaire["inventaire"]:
            print(f"{item["quantité"]} X {item["nom"]}")
            nom = item["nom"]
            quantite = item["quantité"]
            ajouter_objet(attaquant["inventaire"], nom=quantite)
        
        adversaire["inventaire"] = []

def player_combat_action(personnage1, personnage2):
    print("1. Attaquer")
    print("2. Utiliser une potion de vie")
    users_choice = int(input("Votre choix : "))
    match users_choice:
        case 1:
            attaquer(personnage1, personnage2)
        case 2:
            utiliser_potion(personnage1)

def opponent_combat_action(personnage1, personnage2):
    destiny = random.randint(1, 5)
    if 1 <= destiny <= 4:
        attaquer(personnage1, personnage2)
    else:
        for el in personnage1["inventaire"]:           
            if el["nom"] == "potion_de_soin" and el["quantité"] > 0:
                utiliser_potion(personnage1)
            else:
                attaquer(personnage1, personnage2)

def combat(personnage1, personnage2):
    print(f"Le combat débute entre {personnage1["nom"]} et {personnage2["nom"]} !")

    while personnage1["pointsDeVie"] > 0 and personnage2["pointsDeVie"] > 0:
        afficher_personnage(personnage1)
        print()
        afficher_pointsDeVies(personnage2)
        print()
        if personnage1["pointsDeVie"] > 0:
            player_combat_action(personnage1, personnage2)
        if personnage2["pointsDeVie"] > 0:
            opponent_combat_action(personnage2, personnage1)
    
    if personnage1["pointsDeVie"] <= 0:
        print("Vous avez lamentablement perdu...")
        exit()
    else:
        print("Vous passez senior !!!")

hero = create_character("Enguerrand le pleutre", "Consultant")
antagoniste = create_character("Dylan de l'Essec", "Fils à papa")

combat(hero, antagoniste)