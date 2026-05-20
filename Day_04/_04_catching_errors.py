# we can handle errors using try/except 
# now it will run the try block code and if any error occurs, it will run the except block code

try: 
    number = int(input("Please enter a number: "))
    print(number)

# we have multiple options to specify the error type in the except block
except ValueError:
    print("Invalid input !")

# if we just write except it will catch all of the errors