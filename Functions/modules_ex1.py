def greeting():
    print ("Welcome to the Class ")

def read_student_data(n):
    student_data=[]
    for i in range(n):
        student_data.append(input("enter a student name:"))
    return student_data

def calculate_expenses(n):
    expenses=[]
    for i in range(n):
        p,q=map(int,input("Enter price and qty:").split())
        expenses.append(p*q)
    return expenses