child_age = 0

while child_age <= 0:
    child_age = int(input("Veuillez renseigner l'age de votre enfant (à partir de 3 ans) : "))

if child_age < 3:
    print("Votre enfant est trop jeune pour être inscrit.")
elif child_age < 7:
    print("Catégorie 'Baby'.")
elif child_age < 9:
    print("Catégorie 'Poussin'.")
elif child_age < 11:
    print("Catégorie: 'Pupille'.")
elif child_age < 13:
    print("Catégorie: 'Minime'.")
elif child_age < 18:
    print("Catégorie: 'Cadet'.")
else:
    print("Veuillez vous renseigner auprès de la division senior.")
