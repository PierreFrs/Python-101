import random

hero = {
    "nom" : "Enguerrand le pleutre",
    "classe" : "Consultant",
    "niveau" : 1,
    "points_de_vie" : 100,
    "inventaire" : [
        {
        "nom" : "potion de soin", 
        "quantité" : 3
        }
    ]
}

antagoniste = {
    "nom" : "Dylan de l'ESSEC",
    "classe" : "Fils à papa",
    "niveau" : 1,
    "points_de_vie" : 100,
    "inventaire" : [
        {
        "nom" : "potion de soin", 
        "quantité" : 4
        }
    ]
}

def add_items(personnage, items):
    for item in items:
        personnage["inventaire"].append(item)
        print(f"Un nouvel objet a été ajouté à l'inventaire de {personnage['nom']}")

def level_up(personnage):
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20
    print(f"{personnage["nom"]} prend le lead et passe au niveau {personnage['niveau']} !")

def use_healing_potion(personnage):
    healing_power = random.randint(1, 50)
    for el in personnage["inventaire"]:
        if el["nom"] == "potion de soin" and el["quantité"] > 0:
            personnage["points_de_vie"] += healing_power
            el["quantité"] -= 1
            print(f"{personnage["nom"]} prend une potion de soin et gagne {healing_power} points de vie !")
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

def afficher_points_de_vies(personnage):
    print(f"Points de vies de {personnage["nom"]} : {personnage["points_de_vie"]}")

def attaquer(personnage1, personnage2):
    degats = personnage1["niveau"] * 10
    print(f"{personnage1["nom"]} attaque !")
    personnage2["points_de_vie"] -= degats
    if personnage2["points_de_vie"] <= 0:
        for el2 in personnage2["inventaire"]:
            for el1 in personnage1["inventaire"]:
                if el2["nom"] == el1["nom"]:
                    el2["quantité"] += el1["quantité"]
            else:
                el1.update(el2)

def player_combat_action(personnage1, personnage2):
    print("1. Attaquer")
    print("2. Utiliser une potion de vie")
    users_choice = int(input("Votre choix : "))
    match users_choice:
        case 1:
            attaquer(personnage1, personnage2)
        case 2:
            use_healing_potion(personnage1)

def opponent_combat_action(personnage1, personnage2):
    destiny = random.randint(1, 5)
    if 1 <= destiny <= 4:
        attaquer(personnage1, personnage2)
    else:
        for el in personnage1["inventaire"]:           
            if el["nom"] == "potion de soin" and el["quantité"] > 0:
                use_healing_potion(personnage1)
            else:
                attaquer(personnage1, personnage2)

def combat(personnage1, personnage2):
    print(f"Le combat débute entre {personnage1["nom"]} et {personnage2["nom"]} !")

    while personnage1["points_de_vie"] > 0 and personnage2["points_de_vie"] > 0:
        afficher_personnage(personnage1)
        print()
        afficher_points_de_vies(personnage2)
        print()
        if personnage1["points_de_vie"] > 0:
            player_combat_action(personnage1, personnage2)
        if personnage2["points_de_vie"] > 0:
            opponent_combat_action(personnage2, personnage1)
    
    if personnage1["points_de_vie"] <= 0:
        print("Vous avez lamentablement perdu...")
        exit()
    else:
        print("Vous passez senior !!!")

combat(hero, antagoniste)