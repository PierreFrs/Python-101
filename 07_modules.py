### modules ###

from exercices.functions.exo_20 import saisie_adn, proportion # Import of module functions

chaine_adn = saisie_adn("Veuillez saisir la chaine d'adn : ")
sequence_adn = saisie_adn("Veuillez saisir la séquence d'adn : ")

occurrence = proportion(chaine_adn, sequence_adn)

print(f"Il y a {occurrence} {sequence_adn} dans la chaine : {chaine_adn}.")