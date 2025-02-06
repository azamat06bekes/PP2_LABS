# Python Classes and Objects


# 1st question: When the class object is represented as a string, there is a function that controls what should be returned, which one?
#Answer: __str__()

# 2nd question: What is a correct syntax for deleting an object named person in Python?
#Answer: del person

# 3rd question: Create a class named MyClass:
class MyClass:
    x = 5
#Answer: class

# 4th question: Create an object of MyClass called p1:
class MyClass:
  x = 5
#Answer: p1 = MyClass()

# 5th question: Use the p1 object to print the value of x:
class MyClass:
  x = 5

p1 = MyClass()
#Answer: print(p1.x)

# 6th question: What is the correct syntax to assign a "init" function to a class?
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Answer: __init__()

# 7th question: Insert the missing parts to make the code return: John(36):
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def __str__(self):
    return f'{self.name}({self.age})'
p1 = Person('John', 36)
print(p1)
#Answer: 
