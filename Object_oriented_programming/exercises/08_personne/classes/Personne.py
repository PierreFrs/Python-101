# classes/Personne.py

class Personne:
    def __init__(self, prenom : str, telephone : str, email : str):
        self._prenom = prenom
        self._telephone = telephone
        self._email = email
    
    @property
    def prenom(self):
        return self._prenom
    
    @property
    def telephone(self):
        return self._telephone
    
    @property
    def email(self):
        return self._email
    

    def __str__(self):
        return f"Prénom : {self.prenom}, Téléphone : {self.telephone}, Email : {self.email}"