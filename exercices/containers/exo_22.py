note_number = 15
list_to_display = []

for i in range(note_number):
    list_to_display.append(input("Veuillez saisir une note : "))

print("voici vos notes : ")
for el in list_to_display:
    print(el)