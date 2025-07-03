personnage = {
    "nom" : "",
    "classe" : "",
    "niveau" : 1,
    "points_de_vie" : 100,
    "inventaire" : [
        {
        "nom" : "", 
        "quantité" : 0
        }
        ]
}

def add_items(items):
    for item in items:
        personnage["inventaire"].append(item)

def modify_stats():
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20

def use_healing_potion():
    for el in personnage["inventaire"]:
        if el["nom"] == "potion de soin" and el["quantité"] > 0:



    potion_exists = any(value in ele for ele in personnage["inventaire"])