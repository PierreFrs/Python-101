# main.py
from classes.WaterTank import WaterTank

citerne_1 = WaterTank(1000.0, 2000.0, 200.0)
citerne_2 = WaterTank(1000.0, 2000.0, 1200.0)

citerne_1.poids_total()
citerne_2.poids_total()

WaterTank.afficher_volume_total()

citerne_1.remplir_citerne(1000.0)
citerne_2.vider_citerne(400.0)

WaterTank.afficher_volume_total()

citerne_1.remplir_citerne(4000.0)
citerne_2.vider_citerne(4000.0)