print("Entrez 6 nombres et je vous dirai lequel est le plus grand : ")

num_set = []

for i in range(1, 7):
    if i == 1 :
        num_set.append(int(input("veuillez renseigner le 1er nombre : ")))
    else:
        num_set.append(int(input(f"Veuillez renseigner le {i}ème nombre : ")))

max_num = max(num_set)

print(f"Le plus grand nombre est le {max_num}.")