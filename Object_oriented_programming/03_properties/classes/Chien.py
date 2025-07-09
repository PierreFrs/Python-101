class Chien:
    def __init__(self, nom, age, race): # self => this
        self._nom = nom
        self._age = age
        self._race = race
        print(f"Naissance de {self._nom} !")

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if isinstance(nom, str):
            self._nom = nom
        else:
            raise ValueError

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise ValueError

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if isinstance(race, str):
            self._race = race
        else:
            raise ValueError

    def aboyer(self):
        print(f"{self.nom} waf waf")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")