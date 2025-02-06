# Python - Global Variables

# 1st question: Consider the following code:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# What will be the printed result?
#Answer: Python is awesome

# 2nd question: Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
  global x
  x = "fantastic"

#Answer: global

# 3rd question: Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# What will be the printed result?
#Answer: Python is fantastic