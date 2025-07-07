# main.py

from classes.Gateau import Gateau

tarte_aux_pommes = Gateau(
    "Tarte aux pommes", 
    30, 
    ["pommes", "sucre", "pate"], 
    ["Couper les pommes", "Mettre les pommes dans la pate", "Faire cuire la pate pendant 35min à 180°."], 
    "Joel Robuchon")

def main():
    tarte_aux_pommes.afficher_gateau()

main()