class shape():
    def area():
        return 0
    
class Square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
len = int(input())
wid = int(input())
square = Square(len)
rectangle = Rectangle(len, wid)
print(square.area(), rectangle.area())
