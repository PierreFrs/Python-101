first_name = ""
last_name = ""

while(first_name == "") :
    first_name = input("Veuillez saisir votre prénom : ").strip().capitalize()

while(last_name == "") :
    last_name = input("Veuillez saisir votre nom : ").strip().upper()

print(f"Bonjour M. ou Mme {first_name} {last_name}.")