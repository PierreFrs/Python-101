### Containers ###

# lists
my_list = ["banana", 1, True]

print(my_list[0] == "banana") # Should display True

my_list.append(0.98) # adds an element at the end of the list

my_second_list = ["Donatello", "Leonardo", "Rafaello", "Michelangelo"]

my_list.extend(my_second_list) # adds multiple elements to a list at the end

print(my_list) 

print(my_list[-1] == "Michelangelo")

my_list.append(my_second_list)

print(my_list[-1][0]) # should display "Donatello"

test = my_list.pop(3)
print(my_list)
print(test)

my_list.remove(1)
print(my_list)

my_third_list = [ 1, 2, 3]
for el in my_third_list:
    print(el) # should print each element of the list

# dictionaries


# tuples

