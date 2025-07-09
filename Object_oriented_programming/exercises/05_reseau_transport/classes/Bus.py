# classes/Bus.py
class Bus:
    total_bus = 0
    tarif_ticket = 1.50
    capacite_max_global = 50
    id_counter = 0

    def __init__(self):
        Bus.total_bus += 1
        Bus.id_counter += 1
        self._id_bus = Bus.id_counter
        self._passagers = 0

    @property
    def id_bus(self):
        return self._id_bus

    @property
    def passagers(self):
        return self._passagers

    @passagers.setter
    def passagers(self, passagers):
        if isinstance(passagers, int):
            self._passagers = passagers
        else:
            raise ValueError

    def ajouter_passagers(self, nb):
        if (nb > 0) and (self.passagers + nb <= Bus.capacite_max_global):
            self.passagers += nb
            print(f"Le bus avec l'id {self.id_bus} contient désormais {self.passagers} passagers.")
        elif (nb > 0) and (self.passagers + nb > Bus.capacite_max_global):
            passagers_restant = self.passagers + nb - Bus.capacite_max_global
            self.passagers = Bus.capacite_max_global
            print(f"Le bus avec l'id {self.id_bus} a atteint la capacité maximale de {Bus.capacite_max_global} passagers. {passagers_restant} passagers devront attendre le prochain.")
        else:
            print("Le nombre de passagers à ajouter ne peux pas être inférieur ou égal à 0.")
    
    def retirer_passagers(self, nb):
        if (nb > 0) and (self.passagers - nb > 0):
            self.passagers -= nb
            print(f"Le bus avec l'id {self.id_bus} contient désormais {self.passagers} passagers.")
        elif (nb > 0) and (self.passagers - nb <= 0):
            self.passagers -= nb
            print(f"Le bus avec l'id {self.id_bus} est désormais vide.")
        else:
            print("Le nombre de passagers à retirer ne peux pas être inférieur ou égal à 0.")

    @classmethod
    def modifier_tarif(cls, nouveau_tarif):
        if isinstance(nouveau_tarif, float) and nouveau_tarif > 0:
            cls.tarif_ticket = nouveau_tarif
            print(f"Le prix du ticket est passé à {cls.tarif_ticket} €.")
        else:
            raise ValueError
    
    @classmethod
    def modifier_capacite_max_global(cls, nouvelle_capacite):
        if isinstance(nouvelle_capacite, int) and (nouvelle_capacite > 0):
            cls.capacite_max_global = nouvelle_capacite
            print(f"La capacité maximale globale est passée à {cls.capacite_max_global} passagers par bus.")
        else:
            raise ValueError
    
    @classmethod
    def afficher_statistiques(cls):
        print("Statistiques de la compagnie de bus :")
        print(f"    - Nombre total de bus : {cls.total_bus}")
        print(f"    - Tarif actuel du ticket : {cls.tarif_ticket}")
        print(f"    - Capacité individuelle des bus : {cls.capacite_max_global}")