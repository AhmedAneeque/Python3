import csv
import os
os.chdir("D:\\Aneeque Python")
print(os.getcwd())
'''
with open ("Products.csv","r") as file:
    csvReader=csv.reader(file)
    next(csvReader)   #this function is used to skip 1 line
    total_amount=0
    for l in csvReader:
        print(l)
        total_amount+=int(l[-1])
    file.close()
print("Total bill amount=",total_amount)
'''
with open("employee.csv","w",newline="") as outfile:
    csvWriter=csv.writer(outfile)
    csvWriter.writerow(["empid","empname","basic"])
    csvWriter.writerow([123,"Ali",52000])

    for i in range(3):
        empid=int(input("Enter Employee id:"))
        empname=input("Enter Employee Name:")
        basic=float(input("Enter Basic Salary:"))

        csvWriter.writerow([empid,empname,basic])
    outfile.close()