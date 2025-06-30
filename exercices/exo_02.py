first_name = ""
last_name = ""

while(first_name == "") :
    first_name = input("Veuillez saisir votre prénom : ").capitalize()

while(last_name == "") :
    last_name = input("Veuillez saisir votre nom : ").capitalize()

print(f"Bonjour M. ou Mme {first_name} {last_name}.")