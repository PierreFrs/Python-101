base_capital = int(input("Veuillez saisir votre capital initial : "))
doubled_capital = base_capital * 2
improved_capital = base_capital
rate = float(input("Veuillez saisir votre taux : "))/100
year = 0

while (improved_capital < doubled_capital):
    year += 1
    improved_capital = improved_capital * (1 + rate)
    print(improved_capital)

print(f"Il vous faudra {year} ans pour doubler votre capital, passant de {base_capital}€ à {round(improved_capital)}€.")