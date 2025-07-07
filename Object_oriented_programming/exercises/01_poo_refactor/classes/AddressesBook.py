from classes.Address import Address

class AddressBook:
    def __init__(self):
        self.addresses : list[Address] = []

    def input_address(self, address : Address=None):
        if address is None:
            print("==== Ajouter une adresse ====")
        else:
            print("==== Modifier une adresse ====")
            print("Entrée pour conserver l'ancienne valeure.")

        numero_voie = input("Veuillez saisir le numéro de voie : ") or address.numero_voie
        complement = input("Veuillez saisir le complément : ") or address.complement
        intitule = input("Veuillez saisir l'intitulé : ") or address.intitule
        commune = input("Veuillez saisir la commune : ") or address.commune
        code_postal = input("Veuillez saisir le code postal : ") or address.code_postal

        return Address(numero_voie, complement, intitule, commune, code_postal)

    def display_addresses(self):
        print("==== Liste des adresses ====")
        for address in self.addresses:
            print(self.addresses.index(address) + 1, end=": ")
            print(address.to_string())
    
    def add_address(self):
        self.addresses.append( self.input_address())
    
    def update_address(self):
        self.display_addresses()
        nb = int(input("Numéro de l'adresse à afficher : ")) - 1
        address = self.addresses[nb]
        self.addresses.pop(nb)
        self.addresses.insert(nb, self.input_address(address))

    def delete_address(self):
        self.display_addresses()
        nb = int(input("Numéro de l'adresse à supprimer : ")) - 1
        self.addresses.pop(nb)