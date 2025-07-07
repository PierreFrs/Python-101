from classes.AddressesBook import AddressBook

address_book = AddressBook()

def main():
    while True:
        print("==== MENU ====")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Modifier une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter")

        choice = int(input("Veuillez faire votre choix : "))

        match choice:
            case 1:
                address_book.display_addresses()
            case 2:
                address_book.add_address()
            case 3:
                address_book.update_address()
            case 4 :
                address_book.delete_address()
            case 0 :
                exit()
            case _:
                print("Erreur dans le choix !")

main()