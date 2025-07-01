### Mathematical Operators ###

# + - * ** // / %

a = 1
b = 2

add = a + b
sub = a - b
mul = a * b
full_div = a // b
float_div = a / b
power = a ** b
mod = a % b

# Unary operators : *= /= (! ++ & -- don't work in python)
a *= 2
a /= 2
print(a) # Should equal 1.0

# String concatenation
str_1 = "hello"
str_2 = "world"
print(str_1 + " " + str_2)

print(str_1 * 5)


### Relational Operators ###

# < > =< => == !=
print(1 < 3)
print(3 > 1)
print(1 <= 3)
print(3 >= 1)
print(2 == 2)
print(3 != 4)


### Logical Operators ###

# or, and, not
print((25 > 1) and (25 != 50))
print((25 > 1) or (25 == 50))
print(not True) # => False


