# RULES FOR TRANSLATION
# vowels are replaced with 'g'

def translate(phrase):
    translation = ""
    for letter in phrase:

        # the below condition checks if the letter is a vowel
        # it is like saying does letter.lower() has ony value from the string "aeiou" ?
        if letter.lower() in "aeiou":
            # it checks if the letter is uppercase
            if letter.isupper():
                translation += "G"
            translation += "g"
        else:
            translation += letter
    return translation 

phrase = input("Enter a phrase to translate: ")
print(translate(phrase))