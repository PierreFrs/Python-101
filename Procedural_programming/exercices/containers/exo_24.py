racer_position = ["Anakin Skywalker", "Aldar Beedo", "Ratts Tyerell", "Sebulba", "Mawhonic", "Dud Bolt", "Clegg Holdfast", "Ebe E. Endocott", "Gasgano", "Boles Roor", "Teemto Pagalies", "Elan Mak", "Mars Guo", "Ark 'Bumpy' Roose", "Neva Kee", "Wan Sandage", "Ody Mandrell", "Ben Quadinaros", "Xelbree"]

print("Liste originale : ", racer_position)

def panne_moteur(racers_list):
    first_racer = racers_list.pop(0)
    racers_list.append(first_racer)
    return racers_list

print("Anakin tombe en panne ! : ", panne_moteur(racer_position))

def passe_en_tete(racers_list):
    first_racer = racers_list.pop(0)
    racers_list.insert(1, first_racer)
    return racers_list

print("Mais quelle remontada de la part de Ratts Tyerell qui passe en tête ! : ", passe_en_tete(racer_position))

def sauve_honneur(racers_list):
    last_racer = racers_list.pop()
    racers_list.insert(-1, last_racer)
    return racers_list

print("Ca se bataille en queue de peloton, Anakin sauve l'honneur et double Xelbree ! : ", sauve_honneur(racer_position))

def tir_blaster(racers_list):
    racers_list.pop(0)
    return racers_list

print("Comment ? je ne suis pas sur que cela soit réglementaire, Aldar Beedo passe en tête !", tir_blaster(racer_position))

def retour_inattendu(racers_list):
    racers_list.append("Ratts Tyerell")
    return racers_list

print("Ratts Tyerell est de retour dans la course !", retour_inattendu(racer_position))