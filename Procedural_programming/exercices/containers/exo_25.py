def calculate(a, b):
    return a+b, a-b, a/b, a*b

def main():
    first_value = float(input("veuillez saisir une premiere valeur : "))
    second_value = float(input("veuillez saisir une seconde valeur : "))

    add, sub, div, mult = calculate(first_value, second_value)

    print(f"Le résultat de l'addition de vos valeurs est {first_value} + {second_value} = {add}.")
    print(f"Le résultat de la soustraction de vos valeurs est {first_value} - {second_value} = {sub}.")
    print(f"Le résultat de la division de vos valeurs est {first_value} / {second_value} = {round(div, 2)}.")
    print(f"Le résultat de la multiplication de vos valeurs est {first_value} x {second_value} = {mult}.")

main()