import csv, os

def main():
    path = r"./exercices/files/exo_28/data/produits.csv"

    if os.path.exists(path):
        pass
    else:
        with open(path, "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["titre", "prix", "stock"])
    
    print("=== MENU PRINCIPAL ===")
    print()
    print("1. Voir les stocks")
    print("2. Ajouter un produit")
    print("0. Quitter l'application")

    users_choice = int(input("Veuillez faire votre choix : "))

    match users_choice:
        case 0:
            exit()
        case 1:
            read_stock(path)
            print()
            exit_to_main()
        case 2:
            new_product = ask_for_new_stock()
            add_stock(path, new_product)
            print()
            exit_to_main()

def read_stock(path):
    with open(path, "r", encoding="UTF_8") as file:
        produits = csv.reader(file, delimiter=";")
        for item in produits:
            print(item)

def ask_for_new_stock():
    titre = input("Veuillez renseigner le titre de votre produit : ")
    prix = input("Veuillez renseigner le prix de votre produit : ")
    stock = input("Veuillez renseigner le nombre de produits : ")
    return [titre, prix, stock]

def add_stock(path, new_product):
    with open(path, "a", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(new_product)

def exit_to_main():
    input("Lorsque vous souhaitez revenir au menu principal, tapez 'Entrée'")
    main()

main()