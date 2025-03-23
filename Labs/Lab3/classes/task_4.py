from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, end = " ")
        print(self.y)
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(self.x, end = " ")
        print(self.y)
    
    def dist(self, sec_point):
        print(sqrt((self.x - sec_point.x)**2 + (self.y - sec_point.y)**2))


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def move(self, x1, y1, z1):
        super().move(x1, y1)
        self.z += z1
        print(self.x, self.y, self.z, end = " ")


        

p1 = Point(6, 8)
p2 = Point(5, 5)
p1.show()
p1.move(1, 1)
p1.dist(p2)

