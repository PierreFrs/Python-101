### functions ###

# No parameters
def hello_world():
    print("Hello world !")

hello_world() # Should print Hello world !

# With parameters
first_name = "Luis" # Global scope variable

def print_hi(name): # Local scope variable
    print(f"Hi {name}")

print_hi("José") # Should print "Hi José"
print_hi(first_name) # Should print "Hi Luis"

# Default parameters
def print_bye(name = "Coco"):
    print(f"Bye {name}")

print_bye() # Should print "Bye Coco"

# return value (with type specification)
def addition(num_a : int, num_b : int) -> int:
    return num_a + num_b

print(addition(1, 2)) # Should return 3