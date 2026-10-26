class Company:
    def __init__(self,emp_id,emp_name):
        # Instance Variable
        self.emp_id=emp_id
        self.emp_name=emp_name
    # Instance class
    Company_name="Google"

    # Instance Method
    @classmethod
    def display_info(cls,salary):
        print("This is basic info")
        cls.salary=salary
        print(cls.salary)

    def display(self):
        print(self.emp_name)
        print(self.emp_id)
        print(self.Company_name)

c1=Company(101,"Ahmed")
c1.display()
Company.Company_name="Microsoft"
c1.display()
# print(Company.Company_name)
c1.display_info(50000)