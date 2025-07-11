# services/services.py
from classes.Product import Product
from classes.Order import Order

def create_product():
    while True :
        id = int(input("Veuillez renseigner l'id produit : "))
        if isinstance(id, int):
            break
    while True :
        name = input("Veuillez renseigner le nom de votre produit : ")
        if name != "":
            break
    while True:
        price = float(input("Veuillez renseigner le prix du produit : "))
        if isinstance(price, float):
            break
    while True:
        stock = int(input("Veuillez renseigner la quantité de produit à ajouter : "))
        if isinstance(stock, int):
            break
    
    return Product(id, name, price, stock)

def select_product_id():
    while True:
        id = int(input("Veuillez sélectionner l'ID du produit dont les stocks doivent être modifiées : "))
        if isinstance(id, int):
            break
    return id

def select_amount():
    while True:
        amount = int(input("Veuillez renseigner la quantité de stocks à ajouter : "))
        if isinstance(amount, int):
            break
    return amount

def create_order():
    while True :
        id_order = int(input("Veuillez renseigner l'id de commande : "))
        if isinstance(id_order, int):
            break
    while True :
        id_produit = int(input("Veuillez renseigner l'id produit : "))
        if isinstance(id_produit, int):
            break
    while True:
        quantity = int(input("Veuillez renseigner la quantité commandée : "))
        if isinstance(quantity, int):
            break
    while True:
        customer = input("Veuillez renseigner le nom du client : ")
        if customer != "":
            break
    
    return Order(id_order, id_produit, quantity, customer)