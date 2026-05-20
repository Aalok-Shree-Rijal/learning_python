# list is a structure to store multiple values
# making easier management of data

# it is declared like a normal variable
# but with square brackets to store multiple values
realFriends = ['chintu','intu','mintu']
fakeFriends = ['rinki','pinki','chinki']

# indexing starts from 0
print(fakeFriends[0])

# Note: '-1' means the last element in the list and '-2' means the second last element 
# and so on
print(realFriends[-1])

# we can have more versatility of fetching values from the list
# we can use something like: 

print(realFriends[0:2])  # this will print the first two 
                         # elements from the index 0

# we can also update list values
realFriends[0] = 'bantu'
print(realFriends)