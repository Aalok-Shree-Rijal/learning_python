def translator(string):
    translation = ""
    for letter in string:
        if letter.lower() in "aeiou":
            translation += "g"
        else:
            translation += letter.lower()
    print(translation)


    
