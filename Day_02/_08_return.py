def validation(username, password):
    if username == "admin" and password == "1234":
        return True
    else: 
        return False

username = input("Enter username: ")
password = input("Enter password: ")
if(validation(username, password)):
    print("Access granted")
else: 
    print("Access denied")

# we still haven't learned about the if-else statements
# so don't worry about it
# just understand that a function is returning a value
# and that value is being used in the if statement

# the function is terminated after a return statement
# the code below the return statement won't be executed