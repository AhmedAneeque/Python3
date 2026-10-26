# This is a Multiple inheritance
class Personal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print("Personal")

class Academics:
    def __init__(self,education,marks):
        self.education=education
        self.grade=""
        self.marks=marks
        self.percent=sum(self.marks)/len(self.marks)
        if self.percent>=90:
            self.grade="A"
        elif self.percent>=80:
            self.grade="B"
        elif self.percent>=70:
            self.grade="C"
        else:
            self.grade="D"
        print("Academics")

class Skills:
    def __init__(self,skillset):
        self.skillset=skillset
        print("Skills")

class Employee(Personal,Academics,Skills):
    def __init__(self,name,gender,education,marks,skillset,emp_id,company,salary):
        Personal.__init__(self,name,gender)
        Academics.__init__(self,education,marks)
        Skills.__init__(self,skillset)
        self.emp_id=emp_id
        self.salary=salary
        self.company=company
        print("Employee")

    def display_data(self):
        print(self.name)
        print(self.gender)
        print(self.education)
        print(self.marks)
        print(f"{self.percent:.2f}%")
        print(self.grade)
        print(self.skillset)
        print(self.emp_id)
        print(self.company)
        print(self.salary)

E1=Employee("Aneeque","Male","B.E",[90,80,79],["C","Python"],101,"Google",45000)
E1.display_data()
