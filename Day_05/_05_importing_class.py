# here it is like we are importing an new datatype called student made by us
from _04_classes_objects import student

# now the variable student1's datatype is of the defined class student
# it will be able to take the initialized parameters and then store them as attributes
student1 = student("Harry", "psycology", 3.7, False)
print(student1.name) # Output: Harry