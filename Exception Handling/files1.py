'''
read mode:shows error when file is not present or missing
write mode:this will create file if file is not created,or if created delete the data and write new data
append mode: this will create file if file is not created,or if created append the data into the file
'''
import os
os.chdir("D:\\Aneeque Python")
print(os.getcwd())
try:
    with open ("Employee.txt","a") as fa:
        fa.write("New line is added")
        fa.write(input("Enter text you want to add in the document:"))
        fa.close()

    with open ("Employee.txt","r") as fr:
        print(fr.readlines())
        fr.close()
except FileNotFoundError:
    print("Unable to create a file")
