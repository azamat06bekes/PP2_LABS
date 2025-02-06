# 4th Task

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()
p2.show() 

p1.move(10, 12)
p1.show()

d = p1.dist(p2)
print(f"Distance between points: {d}")
