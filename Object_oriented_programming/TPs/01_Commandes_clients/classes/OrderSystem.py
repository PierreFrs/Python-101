# classes/OrderSystem.py
import csv
from classes.Product import Product
from classes.Order import Order

class OrderSystem:
    def __init__(self, products : list[Product], orders : list[Order]):
        self._products = products
        self._orders = orders

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list[Product]):
            self._products = value
        else:
            raise ValueError

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, list[Order]):
            self._orders = value
        else:
            raise ValueError

    def add_product(self, new_product : Product):
        if not isinstance(new_product, Product):
            raise ValueError
        
        for product in self.products:
            if new_product.id == product.id:
                print("Le produit existe déjà")
                return self.products
            
        self.products.append(new_product)
        print("Le produit a été ajouté : ")
        self.print_product(new_product)
        return self.products

    def add_stock(self, product_id, amount):
        if not isinstance(product_id, int) or not isinstance(amount, int):
            raise ValueError
        
        for product in self.products:
            if product_id == product.id:
                product.stock += amount
                print("Le produit a été ajouté :")
                self.print_product(product)
                return self.products
            else:
                print("L'id du produit n'a pas pu être trouvé")

    def add_order(self, new_order : Order):
        if not isinstance(new_order, Order):
            raise ValueError
        for product in self.products:
            if new_order.product_id == product.id and new_order.quantity <= product.stock:
                product.stock -= new_order.quantity
                self.orders.append(new_order)
                print("La nouvelle commande a été enregistrée :")
                self.print_order(new_order)
            elif new_order.product_id == product.id and product.stock < product.stock:
                print(f"La quantité de {product.name} n'est pas suffisante pour passer cette commande.")
                break
            else:
                print(f"Le produit avec l'ID {new_order.product_id} n'existe pas.")
                break
        return self.products, self.orders
    
    def print_products(self):
        print("| ID | Nom du produit | Prix | Stocks |")
        for product in self.products:
            print(f"| {product.id} | {product.name} | {product.price} | {product.stock} |")
    
    def print_orders(self):
        print("| ID | ID du produit | Quantité | Client |")
        for order in self.orders:
            print(f"| {order.order_id} | {order.product_id} | {order.quantity} | {order.customer} |")
    
    def print_product(self, product : Product):
        print(f"| {product.id} | {product.name} | {product.price} | {product.stock} |")

    def print_order(self, order : Order):
        print(f"| {order.order_id} | {order.product_id} | {order.quantity} | {order.customer} |")