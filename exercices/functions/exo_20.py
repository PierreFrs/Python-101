def verification_adn(chaine):
    is_valid = True
    for letter in chaine:
        if (letter != "a") and (letter != "t") and (letter != "c") and (letter != "g"):
            is_valid = False
            break
    return is_valid

def saisie_adn():
    chaine_saisie = input("Veuillez saisir une chaine adn :")

    if verification_adn(chaine_saisie):
        return chaine_saisie
    else:
        print("la chaine saisie n'est pas valide, veuillez réessayer")
        saisie_adn()

def proportion(chaine, sequence):
    return chaine.count(sequence)

def programme_final():
    