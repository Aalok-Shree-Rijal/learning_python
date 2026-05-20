phrase = "greater the mass greater the force"
author = "Issac Newton"

# will print exactly the same as above
print(phrase + " was said by " + author) 

# using .upper() to convert the phrase to uppercase
print(phrase.upper() + " was said by " + author.upper()) 

# using .lower() to convert the phrase to lowercase
print(phrase.lower() + " was said by " + author.lower())

# the len() function returns the length of the string
print("Length of phrase: " + str(len(phrase)))

# NOTE: str() is used to convert a datatype of a variable to a string

# The numbering of the characters in a string starts from 0
# so the first character is at index 0, the second at index 1, and so on.
# To access a character at a specific index, we can use square brackets.
print(phrase[5])

variable = "t"
# we can also use an useful .index function to find the index of a character
print("position of " + variable + " : " + str(phrase.index(variable)))

# we can use .replace() to replace a substring with another substring
print(phrase.replace("greater", "thicker"))