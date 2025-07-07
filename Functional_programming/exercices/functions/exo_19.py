def compter_lettre_a(chaine : str) -> int :
    a_counter = 0
    for letter in chaine.lower():
        if letter == "a":
            a_counter += 1
    return a_counter

print(compter_lettre_a("Animal"))
print(compter_lettre_a("mixer"))

def compter_lettre_a_sans_boucle(chaine : str) -> int :
    return chaine.count("a")

print(compter_lettre_a_sans_boucle("animal"))