def compter_lettre_a(chaine):
    a_counter = 0
    for letter in chaine:
        if letter == "a":
            a_counter += 1
    return a_counter

print(compter_lettre_a("animal"))

def compter_lettre_a_sans_boucle(chaine):
    return chaine.count("a")

print(compter_lettre_a_sans_boucle("animal"))