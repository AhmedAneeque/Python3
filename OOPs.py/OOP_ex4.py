'''
Write a Python program to demonstrate the concept of classes and objects by creating a Student class.
The class should contain three attributes: name, roll_no, and marks, representing the student's name, 
roll number, and marks respectively. Define a method to accept or initialize the student details. 
Create an object of the Student class and assign appropriate values to its attributes. Finally, 
display the complete student details in a well-formatted manner.
'''
class student:
    def __init__(self,roll,name,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        print("This is a constructor")

    # def read_data(self):
    #     self.name=input("Enter Name:")
    #     self.roll=input("Enter roll number:")
    #     self.marks=list(int(input("Enter Marks:")))

    def display_data(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
        print(sum(self.marks))
        print(sum(self.marks)/len(self.marks))

s1=student(1,"Dummy",[91,76,78])
# s1.read_data()
s1.display_data()
        

