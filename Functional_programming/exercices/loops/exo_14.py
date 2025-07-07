base_pop = int(input("Renseignez la population de base : "))
target_pop = int(input("Renseignez la population visée : "))
growth_rate = float(input("Renseignez le taux d'accroissement : "))

num_year = 0

while base_pop < target_pop:
    num_year += 1
    base_pop *= 1 + growth_rate/100

print("La population a besoin de 1 an pour atteindre le nombre visé") if num_year == 1  else print(f"La population a besoin de {num_year} ans pour atteindre le nombre visé")