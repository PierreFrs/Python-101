annuaire = []

def main():
    print("=== MENU PRINCIPAL ===")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimer une adresse")
    print("0. Quitter le programme")
    
    users_choice = int(input("Votre choix : "))

    match users_choice:
        case 0:
            exit()
        case 1:
            read_addresses()
        case 2:
            add_address()
        case 3:
            update_address()
        case 4:
            delete_address()
            
def add_address():
    print("=== AJOUTER UNE ADRESSE ===")

    new_adresse = {
    "numeroDeVoie" : "",
    "complement" : "",
    "intituleDeVoie" : "",
    "commune" : "",
    "codePostal" : ""
    }

    new_adresse["numeroDeVoie"] = input("Veuillez entrer le numéro de voie SVP : ")
    new_adresse["complement"] = input("Veuillez entrer le complément d'adresse SVP : ")
    new_adresse["intituleDeVoie"] = input("Veuillez entrer l'intitulé' de voie SVP : ")
    new_adresse["commune"] = input("Veuillez entrer le nom de la commune SVP : ")
    new_adresse["codePostal"] = input("Veuillez entrer le code postal SVP : ")

    annuaire.append(new_adresse)

    print("L'adresse a bien été ajoutée à l'annuaire")
    main()

def update_address():
    print("=== MODIFIER UNE ADRESSE ===")
    display_addresses()

    address_index = int(input("Veuillez entrer le numéro de l'adresse à modifier : ")) - 1
    address_to_update = annuaire[address_index]
    address_string = display_address(address_to_update)

    print(f"L'adresse à modifier est la suivante : {address_string}")

    print("Quel élément de l'adresse voulez vous mettre à jour ?")
    print(f"1. Le numéro de voie : {address_to_update["numeroDeVoie"]}")
    print(f"2. Le complément d'adresse : {address_to_update["complement"]}")
    print(f"3. L'intitulé de voie : {address_to_update["intituleDeVoie"]}")
    print(f"4. La commune : {address_to_update["commune"]}")
    print(f"5. Le code postal : {address_to_update["codePostal"]}")
    print(f"0. Sortir du menu de mise à jour")

    users_choice = int(input("Que choisissez-vous ? "))

    match users_choice:
        case 0:
            main()
        case 1:
            address_to_update["numeroDeVoie"] = input("Veuillez renseigner le nouveau numéro de voie : ")
        case 2:
            address_to_update["complement"] = input("Veuillez renseigner le nouveau complément d'adresse : ")
        case 3:
            address_to_update["intituleDeVoie"] = input("Veuillez renseigner le nouvel intitulé de voie : ")
        case 4:
            address_to_update["commune"] = input("Veuillez renseigner la nouvelle commune : ")
        case 5:
            address_to_update["codePostal"] = input("Veuillez renseigner le nouveau code postal : ")

    annuaire.pop(address_index)
    annuaire.insert(address_index, address_to_update)

    print("l'adresse a été mise à jour !")
    main()

def read_addresses():
    print("=== VOIR LES ADRESSES ===")

    if len(annuaire) == 0:
        print("Il n'y a aucune adresse à afficher.")
    else:
        display_addresses()

    input("Appuyer sur n'importe quelle touche pour revenir au menu précédent : ")

    main()

def delete_address():
    print("=== SUPPRIMER UNE ADRESSE ===")

    display_addresses()

    address_index = int(input("Veuillez entrer le numéro de l'adresse à supprimer : ")) - 1
    address_to_delete = annuaire[address_index]
    address_string = display_address(address_to_delete)

    print(f"L'adresse à supprimer est la suivante : {address_string}")
    confirm = input("Êtes vous sur de vouloir supprimer cette adresse ? (y / n) ")
    if confirm == "y":
        annuaire.pop(address_index)
        print("l'adresse a été supprimée de l'annuaire.")
        main()
    else:
        print("L'action est annulée, retour au menu de suppression.")
        delete_address()

def display_address(address):
    return f"{address["numeroDeVoie"]} {address["complement"]} {address["intituleDeVoie"]}, {address["codePostal"]} {address["commune"]}"

def display_addresses():
    print("Voici les différentes adresses enregistrées : ")
    print("-" * 50)
    for adresse in annuaire:
        print(f"Adresse n°{annuaire.index(adresse) + 1} :")
        print(display_address(adresse))
        print("-" * 50)

main()