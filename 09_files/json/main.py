import json

path = "09_files\json\personne.json"

# .dump() => write to file
with open(path, "w", encoding="UTF-8") as file:
    mon_dict = [
        {
        "prenom" : "Toto",
        "age" : 25,
        "email" : "toto@email.fr"
        }
    ]
    json.dump(mon_dict, file, indent=4)

with open(path, "r", encoding="UTF-8") as file:
    personnes = json.load(file)
    print(personnes)