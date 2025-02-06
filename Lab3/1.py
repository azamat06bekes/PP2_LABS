# Python Functions


# 1st question: What is the correct keyword for defining functions in Python?
#Answer: def

# 2nd question: Create a function named my_function.
def my_function():
    print("Hello from a function")
#Answer: def my_function():

# 3rd question: Execute a function named my_function.
def my_function():
    print("Hello from a function")
my_function()
#Answer: my_function()

# 4th question: Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
#Answer: print(fname)

# 5th question: Let the function return the x parameter + 5.
# def my_function(x):
    return x + 5
#Answer: return x + 5

# 6th question: If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])
#Answer: *

# 7th question: If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
  print("His last name is " + kid["lname"])
#Answer: **
