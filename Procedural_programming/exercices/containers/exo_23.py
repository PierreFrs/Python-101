from statistics import mean

grades = []

def main():
    user_choice = ""
    while (user_choice != "y") and (user_choice != "n"):
        user_choice = input("Souhaitez vous choisir un nombre prédéterminé de notes à remplir ? (y / n) ").lower()

    if user_choice == "y":
        limited_grades_loop()
    else:
        free_grades_loop()

    print(f"La note maximale est de {float(max(grades))} / 20")
    print(f"La note minimale est de {float(min(grades))} / 20")
    print(f"La moyenne est de {round(mean(grades), 2)} / 20")

def free_grades_loop():
    while True:
        grade = float(input("Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : "))
        if 0 <= grade <= 20:
            grades.append(grade)
        elif grade > 20:
            print("Erreur : la note ne peut être supérieure à 20. Réessayez.")
        else:
            break

def limited_grades_loop():
    max_num_of_grades = int(input("Combien de notes souhaitez-vous entrer dans le programme ? "))
    for _ in range(max_num_of_grades):
        grade = 0
        while True:
            grade = float(input("Veuillez entrer une note entre 0 et 20 compris : "))
            if 0 <= grade <= 20:
                grades.append(grade)
                break
            else:
                print("Erreur : la note doit être entre 0 et 20. Réessayez.")

main()