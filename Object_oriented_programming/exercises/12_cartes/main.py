# main.py

from classes.Carte import Carte

c1 = Carte(3, "trèfle")
c2 = Carte(7, "coeur")
result = c1 + c2
print(result)
result = c1 - c2
print(result)
print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
"trèfle" in c1
"trèfle" in c2