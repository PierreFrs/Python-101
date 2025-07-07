### Containers ###

# lists
my_list = ["banana", 1, True]

print(my_list[0] == "banana") # Should display True

my_list.append(0.98) # adds an element at the end of the list

my_second_list = ["Donatello", "Leonardo", "Rafaello", "Michelangelo"]

my_list.extend(my_second_list) # adds multiple elements to a list at the end

print(my_list) 

print(my_list[-1] == "Michelangelo")

my_list.append(my_second_list)

print(my_list[-1][0]) # should display "Donatello"

test = my_list.pop(3)
print(my_list)
print(test)

my_list.remove(1)
print(my_list)

my_third_list = [ 1, 2, 3]
for el in my_third_list:
    print(el) # should print each element of the list

# sorted, filter, map, reduce

# tuples

mon_tuple = "a", 1, True # Immutables
var1, var2, var3 = mon_tuple # Tuple unpacking
print(var1) # "a"
print(var2) # 1
print(var3) # True

def recuperer_nombre_carre(nombre):
    return nombre, nombre**2 # tuple packing

nombre, carre = recuperer_nombre_carre(9) # Unpacking
print(nombre)
print(carre)

mon_autre_tuple = 1, 2, 3, 4, 5

var1, var2, var3, var4, var5 = mon_autre_tuple

# _ variable => jumps the underscore corresponding to the tuple index
var1, var2, _, _, var5 = mon_autre_tuple

# dictionaries

my_dict = {
    "k1": "first value", 
    "k2": "second value"
}

toto = {
    "prenom" : "Toto",
    "age" : 25,
    "email" : "toto@email.fr",
    "isAdmin" : False,
    "tuple" : ("test", 2) # tuples need parenthesis
}

titi = {
    "prenom" : "Titi",
    "age" : 25,
    "email" : "titi@email.fr",
    "isAdmin" : False,
    "tuple" : ("test", 2) # tuples need parenthesis
}

tata = {
    "prenom" : "Tata",
    "age" : 25,
    "email" : "tata@email.fr",
    "isAdmin" : False,
    "tuple" : ("test", 2) # tuples need parenthesis
}

annuaire = [toto, titi, tata]

for personne in annuaire:
    for key, value in personne.items():
        print(f"{key} : {value}")
    print("-"*50)

# print(toto)

# print(toto["prenom"])

# toto["age"] += 1
# print(toto["age"])

# for value in toto.values:
#     print(value)

# for key in toto.keys:
#     print(key)

# for key, value in toto.items:
#     print (f"{key} : {value}")

# CRUD