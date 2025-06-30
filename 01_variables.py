### Variable declaration ###

# Snake case
first_var = 10
# Should be 10
print(first_var)

second_var = 5
# Should be 15
print(first_var + second_var)

# switch values
first_var, second_var = second_var, first_var

# should print 5
print(first_var)


### Types ###

# int
int_var : int = 5

# float
float_var : float = 3.4

# string
str_var : str = "Hi"

# bool
bool_var : bool = True

# empty
empty_var = None


### Comments  ###

# This is a comment

# This
# is
# a
# multi
# line
# comment


### Memory optimization ###

del first_var


### Functions & methods ###

var_to_print = "i am a string"

# Print function
print(var_to_print)

# methods (attached to a type)
capitalized_string = var_to_print.capitalize()
print(capitalized_string)

# display type
print(type(var_to_print))


### Input function ###

age = input("Enter your age : ")
print("Your age is ", age)


### string interpolation ###

dog_name = "Pluto"
print(f"My dog's name is {dog_name}")


### raw strings ###

print(r"\n") # Should print /n
print("Line1\nline2") # Should print 2 lines


### variable cast ###

str_to_cast = "100.23"
casted_str = float(str_to_cast)
print(type(casted_str)) # Should print float


