class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other : "Point"):
        return  Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return f"x : {self.x}, y : {self.y}"
    
p1 = Point(10, 5)
p2 = Point(20, 18)
p3 = p1 + p2
print(p3) # => error
p4 = -p2
print(p4)