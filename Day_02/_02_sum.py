num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# int() function converts string to integer
# Here we use float() to handle decimal numbers as well
result = float(num1) + float(num2)

print("The sum is: " + str(result))