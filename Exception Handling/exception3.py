# raed from a file and store specific data elsewhere
import os
'''
os.chdir("D:\\Aneeque Python") 
print(os.getcwd())
with open("Employee.txt","r") as fr,open ("Salary.txt","w") as fw:
    FileData=fr.readlines()
    for line in FileData:
        l=list(line.split())
        print(l)
        fw.write(f"{l[0]} {l[-1]}\n")
'''
class FileOperations:
    def __init__(self,source,dest):
        os.chdir("D:\\Aneeque Python")
        print(os.getcwd())
        self.source=source
        self.dest=dest

    def Copydata(self):
        # os.chdir("D:\\Aneeque Python") 
        with open(self.source,"r") as fr,open (self.dest,"w") as fw:
            FileData=fr.readlines()
        for line in FileData:
            l=list(line.split())
            print(l)
            fw.write(f"{l[0]} ")
            # fr.close()
            # it automatically close the files,not needed to add close() in these
            # fw.close()

F1=FileOperations("Employee.txt","Salary.txt")
F1.Copydata()