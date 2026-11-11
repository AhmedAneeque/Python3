'''
Write a menu driven application by using python to perform following operations by using functions
1:To create a file with name "xyz.csv"
2:To Display all data from the csv file
3:To backup
4:To Delete the Backup File
5:To check if a record is present in the file or not
6:To exit from the application 
'''
print('''1:To create a file with name "xyz.csv"
2:To Display all data from the csv file
3:To backup
4:To Delete the Backup File
5:To check if a record is present in the file or not
6:To exit from the application''')

import os
import csv
headers=["sid","sname","city","gender","total"]

def Createfile(file_name):
    if os.path.exists(file_name):
        print("File Already Present!")
    else:
        with open(file_name,"w") as file:
            csvWriter=csv.DictWriter(file,fieldnames=headers)
            print("File is created")
            file.close()

def display_records(file_name):
    def display_records():
        with open ("Students.csv","r") as infile:
            csvReader=csv.DictReader(infile)
            records=list(csvReader)
            if len(records)==0:
                print("No Record!")
            else:
                return records

def backupfile():
    with open("Students.csv","r") as fr,open ("Backup.csv","w") as fw:
        FileData=fr.readlines()
        for line in FileData:
            l=list(line.split())
            print(l)
            fw.write(f"{l}")

def delbackup():
    os.remove("Backup.csv")
    print("Backup file Deleted Successfully!")

def check_record():
    found=False
    allrecords=display_records()

    for r in allrecords:
        if id==int(r["id"]):
            print(r)
            found=True
    if found==False:
        print("No Records Found")

def exit():
    print("Menu driven app closed!")

o=int(input("Type an option: "))
if o==1:
    Createfile(input("enter the file name: "))

elif o==2:
    display_records(input("enter File name: "))

elif o==3:
    backupfile()

elif o==4:
    delbackup()

elif o==5:
    check_record()

elif o==6:
    exit()

else:
    print("Invalid Option")



