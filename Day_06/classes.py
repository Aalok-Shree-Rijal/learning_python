class chef: 
    def make_momo(self):
        print("Chef is making a momo")
    def make_chowmein(self):
        print("chef is making a chowmein")
    def make_chia(self):
        print("Chef is making tea.")

# now the attributes of the class chef is inherited by
# the class masterChef
class masterChef(chef):
    def make_special_dish(self):
        print("Chef is making ratatoulie")

class student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

        # creating a function to check weather the student is 
        # nominated as the student of the year
    def soy_nominee(self):
        if self.gpa >= 3.5:
            return True
        else: 
            return False