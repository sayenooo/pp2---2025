

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2

Area1=Square(int(input()))
print(Area1.area())
length,width=map(int,input().split())
Area2=Rectangle(length,width)
print(Area2.area())

