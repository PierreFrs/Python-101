def verification_adn(chaine : str) -> bool :
    for letter in chaine:
        # if (letter != "a") and (letter != "t") and (letter != "c") and (letter != "g"):
        if letter not in "actg":
            return False
    return True

def saisie_adn(question : str) -> str :
    chaine_saisie : str = input(question)

    while not verification_adn(chaine_saisie) :
        print("la valeur saisie n'est pas valide, veuillez réessayer.")
        chaine_saisie : str = input(question)
        
    return chaine_saisie

def proportion(chaine : str, sequence : str) -> int :
    return chaine.count(sequence)

if __name__ == "__main__":
    chaine_adn : str = saisie_adn("Veuillez saisir la chaine d'adn : ")
    sequence_adn : str = saisie_adn("Veuillez saisir la séquence d'adn : ")

    occurrence : int = proportion(chaine_adn, sequence_adn)

    print(f"Il y a {occurrence} {sequence_adn} dans la chaine : {chaine_adn}")