# these are used to check conditions

# SYNTAX:
# if <condition>:
#     <Block of code>
# elif <condition>:
#     <Block of code>
# else:
#     <Block of code>

# we can keep on using the elif statement to check multiple conditions

hungry = input("Are you hungry? (yes/no): ")
money = input("Do you have money? (yes/no): ")
hungry = hungry.lower()
money = money.lower()

# .lower() is used to convert the input to lowercase
# so that the comparison is case-insensitive

if(hungry == "yes" and money == "yes"):
    print("Go get some food")
elif(hungry == "yes" and money == "no"): 
    print("You are hungry but broke, sybau and work")
elif(hungry == "no" and money == "yes"):
    print("don't you dare waste your money")
else: 
    print("You are not hungry, so chill")