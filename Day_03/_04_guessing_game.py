secret_word = "python"
max_attempts = 5
attempts = 0
out_of_attempts = False
guess = ""
while (guess != secret_word and not(out_of_attempts)):
    if attempts < max_attempts + 1 :
        guess = input("Guess the secret word: ")
        attempts += 1
    else:
        out_of_attempts = True

if out_of_attempts:
    print("You are out of attempts! The secret word was:", secret_word)
else: 
    print("Congratulations! You've guessed the secret word")
    

# NOTE: this code potrays how you can use variables to control the flow of a guessing game
# and how to use variables to make the program more efficient by avoiding unnecessary checks.