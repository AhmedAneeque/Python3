import csv
fields=["empid","empname","Gender","department","role","Age","Basic_salary"]

#Create a csv file 1
def Create_file():
    with open("Employee1.csv","w",newline="") as files:
        csvWriter=csv.DictWriter(files,fieldnames=fields)
        csvWriter.writeheader()
        files.close()

#Write Data to a csv File 2
def Write_record():
    with open("Employee1.csv","a",newline="") as files:
        csvWriter=csv.DictWriter(files,fieldnames=fields)
        emp={}
        empid=int(input("Enter Employee ID :"))
        empname=(input("Enter Employee name:"))
        emp.update({"empid":empid,"empname":empname})
        Gender=input("Enter Employee Gender:")
        if Gender in ("Male","Female"):
            emp.update({"Gender":Gender})
        else:
            print("Invalid Gender,Enter Male or Female")
        department=input("Enter Employee department:")
        if department in ("Support","Sales","Logistic","Marketing","IT"):
            emp.update({"department":department})
        else:
            print("Invalid Department")
        role=input("Enter Employee role :")
        if role in ("Software Engineer","Frontend Developer","Backend Developer","Data Analyst","HR Manager","Sales Manager"):
            emp.update({"role":role})
        else:
            print("Invalid Role")
        Age=int(input("Enter Employee age :"))
        if Age>=20 and Age<55:
            emp.update({"Age":Age})
        else:
            print("Invalid Age")
        Basic_salary=float(input("Enter Basic Salary :"))
        if Basic_salary>=25000 and Basic_salary<100000:
            emp.update({"Basic_salary":Basic_salary})
        else:
            print("Invalid Salary")
        print(emp)
        csvWriter.writerow(emp)
        files.close()

#Read all data in csv file 3
def display_records():
    with open ("Employee1.csv","r") as infile:
        csvReader=csv.DictReader(infile)
        records=list(csvReader)
        if len(records)==0:
            print("No Record!")
        else:
            return records

#Search for specific information in csv file 5
def checkEmpId(id):
    found=False
    allrecords=display_records()

    for r in allrecords:
        if id==int(r["empid"]):
            print(r)
            found=True
    if found==False:
        print("No Records Found")

#Display all records if condition is satisfied 6
def male_salary(g,s):
    records=display_records()
    for r in records:
        if r["Gender"]==g and float(r["Basic_salary"])>s:
            print(r)

#Dispaly all records in ascending order of employee names 7
def display_ascending():
    records=display_records()
    temp=dict()
    for i in range(len(records)):              
        for j in range(i+1,len(records)):       
            if records[i]["empname"]>records[j]["empname"]:
                temp=records[i]
                records[i]=records[j]
                records[j]=temp

    for r in records:
        print(r)

#Display all records in descending order of salary 8
def display_descending():
    records=display_records()
    temp=dict()
    for i in range(len(records)):              
        for j in range(i+1,len(records)):       
            if records[i]["Basic_salary"]<records[j]["Basic_salary"]:
                temp=records[i]
                records[i]=records[j]
                records[j]=temp

    for r in records:
        print(r)

#Display all Male Employee Records 9
def Male_employee():
    records=display_records()
    for r in records:
        if r["Gender"]=="Male":
            print(r)
            

#Dispaly all employee from specific department 10
def specific_department(a):
    records=display_records()
    for i in records:
        if i["department"]==a:
            print (i)

#Update Records of all Development department by incrementing their salary with 20% 11
def increment():
    records=display_records()
    for r in records:
        if r["department"]=="Support":
            r["Basic_salary"]=float(r["Basic_salary"])+float(r["Basic_salary"])*0.2

    for r in records:
        print(r)
        

# Create_file()
# Write_record()
# print(display_records())
# checkEmpId(101)
# male_salary("Male",40000)
# display_ascending()
# display_descending()
# Male_employee()
specific_department("Support")
# increment()
