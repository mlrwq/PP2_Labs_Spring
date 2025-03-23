class shape():
    def area():
        return 0
    
class Square():
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    
n = int(input())
square = Square(n)
print(square.area())
