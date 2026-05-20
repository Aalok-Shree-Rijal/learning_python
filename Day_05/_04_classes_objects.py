# they help to make code more organized
# when dealing with data
# it is like creating our very own data type

# creating a class called 'student'
class student:

    # here we assign the values that we want to pass
    def __init__(self, name, major, gpa, is_on_scholarship):
        
        # here we are asigning the actual values of the attributes that was passed
        # NOTE : just because you passes the value doesn't means that value is automatically
        # understood, you need to assign the values yourself        
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_sholarship = is_on_scholarship

def scholarship_test(value):
    if(value == "y"):
        return "on scholarship."
    else:
        return "not on scholarship"

name = input("Enter your name: ")
major = input("what is your major: ")
gpa = input("What gpa did you get: ")
is_on_scholarship = input("Are you on scholarship(y/n): ")

student1 = student(name, major, gpa, is_on_scholarship)

print(student1.name + " is a student of ABC collage.\n"
      "He is taking " + student1.major + " as his major.\n "
      "He got " + student1.gpa + " gpa and his is " + scholarship_test(student1.is_on_sholarship))

