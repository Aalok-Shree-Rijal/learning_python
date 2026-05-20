# we can use '**' to denote exponentiation in Python
# for example, 2 raised to the power of 3 is written as 2 ** 3
print(2**3) # Output: 8

# we can also use functions and for loops to calculate powers
def raise_power(base, power):
    result = 1
    for index in range(power):
        result *= base
    return result

base = float(input("Enter the base: "))
power = float(input("Enter the power: "))

print("{base} raised to the power of {power} is {raise_power(base, power)}")
# we can only display numeric values so we can use the '{}'
