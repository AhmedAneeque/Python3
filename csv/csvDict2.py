import csv

emp = [
    {"empid": "121", "name": "Ali", "Gender": "Male", "City": "Malegaon", "Role": "Web Designer", "Basic_pay": 45000},
    {"empid": "122", "name": "Ahmed", "Gender": "Male", "City": "Malegaon", "Role": "App Developer", "Basic_pay": 55000},
    {"empid": "123", "name": "Kamran", "Gender": "Male", "City": "Pune", "Role": "Graphic Designer", "Basic_pay": 40000},
    {"empid": "124", "name": "Rahul", "Gender": "Male", "City": "Mumbai", "Role": "Software Engineer", "Basic_pay": 34000}
]

with open("newEmp.csv", "w", newline="") as outfile:
    fields = ["empid", "name", "Gender", "City", "Role", "Basic_pay"]
    csvWriter = csv.DictWriter(outfile, fieldnames=fields)
    csvWriter.writeheader()
    csvWriter.writerows(emp)

