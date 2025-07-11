# classes/Product.py

class Product:
    def __init__(self, id : int, name : str, price : float, stock : int):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if isinstance(value, int):
            self._stock = value
        else:
            raise ValueError
