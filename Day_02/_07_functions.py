# functions are reusable pieces of code that is used for a specific task

# 'def' is used to define a function
# code of function is indented after ':'
# parameters are passed in the parentheses '()'
# parameters are like the variables that we pass to the function
def greet(name, post):
    print("hello " + name +"!" + " You are a " + post)

# calling a function
user = input("Enter you name: ")
post = input("Enter your post: ")
greet(user, post) # the parameter 'name' will take the value of 'user'
                  # the parameter 'post' will take the value of 'post'

# SOME GOOD PRACTICES: 
# 1. Use simple and descriptive names for functions
# 2. Use lowercase letters and underscores for function names
# 3. Keep functions small and focused on a single task