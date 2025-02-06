# Python Inheritance


# 1st question: What is the correct keyword to use inside an empty class, to avoid getting an error?
#Answer: pass

# 2nd question: hat is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
#Answer: class Student(Person):

# 3rd question: We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)
    
class Student(Person):
  pass
x = Student("Mike")
#Answer: x.printname()

# 4th question: 

#Answer: 

# 5th question: 

#Answer: 

# 6th question: 

#Answer: 

# 7th question: 

#Answer: 