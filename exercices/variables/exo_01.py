a = 1
b = 2
print(a, b)

# solution 1 : temp
c = a
a = b
b = c
print(a, b)

# solution 2 : switch
a, b = b, a
print(a, b)

