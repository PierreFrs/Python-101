### Conditional structures ###

# if, elif, else
mon_age = int(input("Veuillez donner votre âge : "))
if mon_age >= 21 :
    print("Vous êtes majeur aux USA")
elif mon_age >= 18 :
    print("Vous êtes majeur en France")
else:
    print("Vous êtes mineur")

# pass
if mon_age >= 21 :
    pass # Temporary instruction, do nothing but prevents error
elif mon_age >= 18 :
    print("Vous êtes majeur en France")
else:
    print("Vous êtes mineur")

# match case (switch case)
var = int(print("Veuillez entrer un nombre entier."))
match var:
    case 1:
        print("une")
    case 2:
        print("deux")
    case _:
        print("ni une, ni deux")

# Ternaries
temp = int(input("Saisir la température de l'eau : "))
state = "solide" if temp < 0 else ("liquide" if temp <= 100 else "gazeux")
