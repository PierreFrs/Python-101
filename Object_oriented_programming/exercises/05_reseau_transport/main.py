# main.py
from classes.Bus import Bus

bus_1 = Bus()
bus_2 = Bus()

bus_1.ajouter_passagers(20)
bus_1.retirer_passagers(15)
bus_1.ajouter_passagers(50)
bus_1.retirer_passagers(50)

bus_2.ajouter_passagers(50)

Bus.modifier_tarif(1.60)
Bus.modifier_capacite_max_global(60)
Bus.afficher_statistiques()