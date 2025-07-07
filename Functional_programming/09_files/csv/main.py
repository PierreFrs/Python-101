import csv

path = "./09_files/csv/personne.csv"

with open(path, "r", encoding="UTF_8") as file:
    personnes = csv.reader(file, delimiter=";")
    next(personnes) # pass 1st line
    for personne in personnes:
        print(personne)

with open(path, "a", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Titi", 25, "titi@email.fr"])