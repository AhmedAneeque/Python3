# Operator Overriding
class Points:
    def __init__(self,x,y):
        self.x=x
        self.y=y

# Dunder Methods
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            print("The points are same")
            return True
        else:
            print("Point are Different")
            return False
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass

P1=Points(4,5)
P2=Points(7,6)
P1==P2