class Employee():
    def __init__(self,emp_id,emp_name,company):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.company=company

    def display(self):
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.emp_name)
        print("Company:",self.company)

class Sales(Employee):
    def __init__(self, emp_id, emp_name, company,profile,team):
        super().__init__(emp_id, emp_name, company)
        self.profile=profile
        self.team=team

    def display_sales(self):
        self.display()
        print(self.profile,self.team,sep="\n")

class HR(Employee):
    def __init__(self, emp_id, emp_name, company,management_level):
        super().__init__(emp_id, emp_name, company)
        self.management_level=management_level

    def display_HR(self):
        self.display()
        print(self.management_level)

class Development(Employee):
    def __init__(self, emp_id, emp_name, company,skills,project):
        super().__init__(emp_id, emp_name, company)
        self.skills=skills
        self.project=project

    def display_dev(self):
        self.display()
        print(self.skills,self.project,sep="\n")

S1=Sales(101,"Waseem","TCS","Junior Sales Executive","Alpha")
H1=HR(102,"Ahmed","Infosys","HR Manager")
D1=Development(103,"Saadan","ABC Infra",["Python","C","SQL"],"Exam Software")

S1.display_sales()
H1.display_HR()
D1.display_dev()