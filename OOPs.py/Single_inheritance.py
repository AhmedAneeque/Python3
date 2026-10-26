# This is a single inheritance type
# This is a parent class,Super class or base class
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.gender=gender
        self.age=age
        print("This is Parent Class")

'''
    def display(self):
        print("name:",self.name)
        print("gender:",self.gender)
        print("Age:",self.age)
'''
# This is a Child class
class Students(Person):
    def __init__(self, name, age, gender,roll,school,marks):
        super().__init__(name, age, gender)
        self.roll=roll
        self.marks=marks
        self.school=school
        print("This is a child class")

    def display_data(self):
        print("name:",self.name)
        print("gender:",self.gender)
        print("Age:",self.age)
        print("roll:",self.roll)
        print("Marks:",self.marks)
        print("School:",self.school)

s1=Students("Ahmed",19,"Male",10,"ATT",540)
# s1.display()
s1.display_data()