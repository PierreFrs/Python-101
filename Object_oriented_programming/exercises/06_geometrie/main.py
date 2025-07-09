# main.py
from classes.Rectangle import Rectangle
from classes.Parallelepipede import Parallelepipede

rectangle = Rectangle(10, 5)
print(rectangle.perimetre())
print(rectangle.surface())

parallelepipede = Parallelepipede(10, 5, 4)

print(parallelepipede.perimetre())
print(parallelepipede.surface())
print(parallelepipede.volume())