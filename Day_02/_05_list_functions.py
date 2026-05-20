lucky_numbers = [3,4,1,6]

# append a new number to the list
# will append the value to the end of the list
lucky_numbers.append(8)
print(lucky_numbers)

# insert a new number at a specific index
lucky_numbers.insert(2,5) # indexing starts at 0
print(lucky_numbers)

# we can also remove a value from the list
lucky_numbers.remove(4)
print(lucky_numbers)

# pop will remove the last value from the list
lucky_numbers.pop()
print(lucky_numbers)

# pop can also remove a value at a specific index
lucky_numbers.pop(1) # removes the value at index 1
print(lucky_numbers)

# we can find the index of a value in the list
print(lucky_numbers.index(1))

# we can count how many times a value appears in the list
print(lucky_numbers.count(6))

# we can sort the list in ascending order
lucky_numbers.sort()
print(lucky_numbers)

# we can make a copy of the list
lucky_numbers_copy = lucky_numbers.copy()
print(lucky_numbers_copy)

