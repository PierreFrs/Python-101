min_age = 30
max_salary = 40000
min_xp = 5

candidate_age = ""
candidate_expected_salary = ""
candidate_xp = ""

# Inputs section
while (candidate_age == ""):
    candidate_age = input("Veuillez renseigner votre age : ").strip()
    if (candidate_age != ""):
        candidate_age = int(candidate_age)

while (candidate_expected_salary == ""):
    candidate_expected_salary = input("Veuillez renseigner le salaire souhaité : ").strip()
    if (candidate_age != ""):
        candidate_expected_salary = int(candidate_expected_salary)

while (candidate_xp == ""):
    candidate_xp = input("Veuillez renseigner votre nombre d'années d'experience professionnelle : ").strip()
    if (candidate_xp != ""):
        candidate_xp = int(candidate_xp)

# Candidate info verification
if (candidate_age < min_age):
    print(f"L'age minimum requis pour le poste est de {min_age} ans")
    exit()

if (candidate_expected_salary > max_salary):
    print(f"Le salaire maximum proposé pour le poste est de {max_salary}€")
    exit()
if (candidate_xp < min_xp):
    print(f"Le nombre minimal d'années est de {min_xp} ans.")
    exit()

# HR response
print("Merci pour votre candidature, nous reviendrons vers vous lorsque notre équipe de recrutement l'aura examinée.")
