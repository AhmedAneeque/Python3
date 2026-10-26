# Duck Object Polymorphism
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=math.pi*self.radius
    def display_area(self):
        print(self.area)

class Square:
    def __init__(self,side):
        self.side=side
        self.area=self.side**2
    def display_area(self):
        print(self.area)

c1=Circle(10)
c1.display_area()

s1=Square(20)
s1.display_area()

# Polymorphism by using built in fuction overloading
l1=[25,97,56,59]
s1="Hello"
d1={"username":"ali","email":"ali@gmail.com"}

print(len(l1),type(l1))
print(len(s1),type(s1))
print(len(d1),type(d1))