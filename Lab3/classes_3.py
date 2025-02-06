# 3rd Task

class Shape:
    def __init__(self):
        pass 

    def area(self):
        return 0  
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width  

shape = Shape()
print("Shape area:", shape.area()) 

square = Rectangle(5, 4)
print("Square area:", square.area()) 
