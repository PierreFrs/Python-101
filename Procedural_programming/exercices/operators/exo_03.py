import math

pi = math.pi
rayon_base = ""
hauteur = ""

while(rayon_base == ""):
    rayon_base = float(input("Veuillez renseigner le rayon de la base (en cm) : "))

while(hauteur == ""):
    hauteur = float(input("Veuillez renseigner la hauteur du cone (en cm) : "))

surface_base = pi * math.pow(rayon_base, 2)

volume = (surface_base * hauteur)/3

print(f"Le volume du cone est de {math.floor(volume, 2)} cm3")