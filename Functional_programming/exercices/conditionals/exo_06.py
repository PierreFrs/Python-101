copy_number = 0
total_price = 0

while copy_number <= 0:
    copy_number = int(input("Veuillez entrer le nombre d'exemplaires à photocopier : "))

def calculate_price(input_value):
    if input_value < 10:
        return 0.5
    elif input_value <= 20:
        return 0.4
    else:
        return 0.3

total_price = copy_number * calculate_price(copy_number)

print(f"Le montant total s'élève à {total_price}€")