'''
Create an Employee class with attributes such as emp_id, name, department, designation,
salary, and city.Create an object of the class and display the complete details of the 
employee. Also, create methods to calculate annual salary and display employee information.
'''
class Employee:
    def __init__(self,emp_id,name,department,designation,salary,city):
            self.name=name
            self.emp_id=emp_id
            self.department=department
            self.designation=designation
            self.salary=salary
            self.city=city
            print("Employee details")

    def display_data(self):
          print("Employee id:",self.emp_id)
          print("Name:",self.name)
          print("Department:",self.department)
          print("Designation:",self.designation)
          print("Salary:",self.salary)
          print("city:",self.city)
          print("Annual Salary:",self.salary*12)

e1=Employee(101,"Ahmed","Finance","Accounts Analyst",35000,"Malegaon")
e1.display_data()
