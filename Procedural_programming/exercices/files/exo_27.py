import os

def get_secret(path):
    with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    

def save_secret(path, secret):
    with open(path, "w") as file:
        file.write(secret)
    with open(path, "r") as file:
        if os.path.exists(path):
            data = file.read()
            if data == secret:
                print("Votre secret a bien été enregistré")
            else:
                print("Quelque chose empêche votre secret d'être sauvé, veuillez contacter le service technique (pensez à faire un ticket)")

def exit_to_main():
    input("Lorsque vous souhaitez revenir au menu principal, tapez 'Entrée'")
    main()

def main():
    file_path = r"exercices/files/mock_files/secret_file.txt"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="UTF-8") as file:
            secret = file.read()
    else:
        secret = input("Veuillez entrer votre secret : ")

    print("Bienvenue dans votre gestionnaire de secrets, que souhaitez-vous faire ?")
    print("1. Consulter mon secret")
    print("2. Modifier mon secret")
    print("0. Enregistrer et sortir de l'application")
    users_choice = int(input("Veuillez saisir votre choix : "))

    match users_choice:
        case 0:
            save_secret(file_path, secret)
            exit()
        case 1:
            print(f"Votre secret : {secret}")
            exit_to_main()
        case 2:
            secret = input("Veuillez entrer votre nouveau secret : ")
            exit_to_main()

main()