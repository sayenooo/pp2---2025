class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x1 = self.x + 10
        self.y1 = self.y + 5
        self.distance = (abs(self.x1**2-self.x**2) + (self.y1**2-self.y**2))**0.5
    def show(self):
        print(f"(x,y) = ({self.x},{self.y})")
    def move(self):
        print(f"changed: ({self.x1},{self.y1})")
    def dist(self):
        print(self.distance)
    
p1,p2 = map(int,input().split())
point = Point(p1,p2)


point.show()
point.move()
point.dist()