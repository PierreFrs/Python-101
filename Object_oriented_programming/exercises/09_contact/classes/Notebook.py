# classes/Notebook.py

from classes.Contact import Contact

class Notebook:
    def __init__(self):
        self._contacts = {}
    
    @property
    def contacts(self):
        return self._contacts
    
    @contacts.setter
    def contacts(self, contacts : dict):
        if isinstance(contacts, dict):
            self.contacts = contacts
        else:
            raise ValueError
    
    def add(self, name, email, street, city):
        self.contacts[name] = Contact(name, email, street, city)
    
    def show(self):
        for key, value in self.contacts.items():
            print(f"=== {key} ===")
            print(f"{value.name} - {value.email}")
            print(value.street)
            print(value.city)
    
