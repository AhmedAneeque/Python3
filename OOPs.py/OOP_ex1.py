class student:
    def __init__(self,roll,name,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        print("This is a constructor")

    def display_data(self):
        print(self.name)
        print(self.roll)
        print(sum(self.marks))
        print(round(sum(self.marks)/len(self.marks)))

# polymorphism: same name but different functions.
class teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("")

    def display_data(self):
        print(self.name)
        print(self.id)
        
user=input("Enter 'student' or 'teacher' ")
if user==student:
    s1=student(1,"Aneeque",[87,95,79])
    s2=student(2,"Ali",[67,75,87])
    s1.display_data()
    s2.display_data()
elif user==teacher:
    s1=teacher("Ahmed",201)
    s2=teacher("sameen",202)
    s1.display_data()
    s2.display_data()
else:
    print("Invalid user")    
