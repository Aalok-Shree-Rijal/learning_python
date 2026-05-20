# creating the class to store the values with ease
class question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    

# array of questions
Questions = ["\nWho is the father of computer?\na. Mahatma Gandhi \nb. Albert Einstein \nc. Charles Babbage",
             "Which year did the covid-19 virus started to spread?\na. 2020 \nb. 1965 \nc. 2019",
             "What do you call your sister's daugher? \na. daughter \nb. niece \nc. little sister"]

# creating a array of the question classes
answerKey = [question(Questions[0], "c"),
             question(Questions[1], "c"),
             question(Questions[2], "b")]

# initializing the score
score = 0 

# looping through each class in the array answerKey
for question in answerKey:
    userAnswer = input(question.question + "\nyour answer: ")

    # checking if the input is correct to the pre-set answer
    if userAnswer == question.answer:
        score += 1

# printing out the input
print("You got " + str(score) + "/" + str(len(answerKey)) + " qustions right.")