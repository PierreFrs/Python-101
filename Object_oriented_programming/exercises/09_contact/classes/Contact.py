# classes/Contact.py

from classes.Address import Address
from classes.Person import Person

class Contact(Address, Person):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)

    def show(self):
        Person.show(self)
        Address.show(self)