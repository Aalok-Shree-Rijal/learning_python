from classes import student

# this checks the value returned by the function of the class 'soy_nominee()'
def check(value):
    if value == True:
        return "nominated as the student of the year."
    else: 
        return "not nominated as the student of the year"

# creating a array of students using the imported class
student_records =[
    student("Aalok", 3.6, "AI/ML"),
    student("Sandesh", 3.49, "Psycology"),
    student("rijan", 3.5, "Cyber Security")
]

# checking wether the students are nominee
# of the student of the year
for student in student_records:
    print(student.name + " is " + (check(student.soy_nominee())))