input_value = ""

while(input_value == ""):
    input_value = input("Veuillez entrer un nombre entier : ").strip()
    if (input_value.isnumeric() == False):
        input_value = ""

def divide_by_3(input_value):
    return int(input_value) % 3 == 0

if input_value == 0:
    print("On ne peut pas diviser par 0")
elif divide_by_3(input_value):
    print("Le nombre est divisible par 3")
else:
    print("Le nombre n'est pas divisible par 3")