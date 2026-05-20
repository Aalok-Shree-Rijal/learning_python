# Syntax
# open("file name", "operation(r(read),w(write),a(append)), r+(read and write)")

data = open("c:/Users/Nitro/Desktop/coding things/learning_python/Day_05/data.txt", "r")

for values in data.readlines():
    print(values)


# Closing data after opening it
data.close()

# we can use function like readline() and readlines()