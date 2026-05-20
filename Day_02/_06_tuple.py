# similar to lists, but they can't be changed or modified (immutable)

# declaring a tuple
lucky_numbers = (3, 7, 13, 21)
print(lucky_numbers)

# accessing elements in a tuple
print(lucky_numbers[0])  # prints 3

# trying to change an element of tuple
lucky_numbers[0] = 5  # This will raise a TypeError 

# tuples could be useful when you don't want the data to be changed