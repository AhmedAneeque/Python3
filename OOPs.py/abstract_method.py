from abc import ABC,abstractmethod
class Data(ABC):
    def __init__(self,a):
        print("This is Constructor in abstract class method")
        self.a=a**2

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def show(self):
        pass

    def mymethod(self):
        print("This is Concrete Method")

class NewData(Data):
    def __init__(self, a,b):
        super().__init__(a)
        self.b=b**3

    def display(self):
        print("This is display method in derived class")

    def show(self):
        print("This is show method in derived class")
        print(self.a)
        print(self.b)

N1=NewData(3,4)
N1.display()
N1.show()
N1.mymethod()