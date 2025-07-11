# classes/Order.py
from classes.Product import Product

class Order:
    def __init__(self, order_id : int, product_id : int, quantity : int, customer : str):
        self._order_id = order_id
        self._product_id = product_id
        self._quantity = quantity
        self._customer = customer

    @property
    def order_id(self):
        return self._order_id

    @property
    def product_id(self):
        return self._product_id
    
    @property
    def quantity(self):
        return self._quantity

    @property
    def customer(self):
        return self._customer