### Loops ###

# for in
for i in range(1, 101):
    print(i) # Prints 1 to 100

for i in range(1, 101, 2):
    print(i) # prints only odd numbers from 1 to 99 (step = 2)

# while
i = 1
while i < 10:
    print(i) # Prints 1 to 9
    i += 1

# continue, break, pass
while True:
    valeur = input("Saisir STOP pour arrêter le programme :")
    if valeur == "STOP":
        break # Breaks out of the loop
    elif valeur.upper() == "Stop":
        print("EN UPPERCASE")
        continue # Go to the next iteration without executing the next actions
    else:
        pass # Does nothing