import os
class InvalidGenderException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Please Enter M for Male and F for Female!"

class InvalidMarksException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "There should be only 3 subjects"

class FileOperations:
    def __init__(self,n,file_name):
        os.chdir("D\\..\\..\\..")
        print(os.getcwd())
        self.n=n
        self.file_name=file_name

    def WriteData(self):
        try:
            Allstudents=[]
            for i in range(self.n):
                r=int(input("Enter roll Number: "))
                name=input("Enter name: ")
                gender=input("Enter M for Male and F for Female: ")
                if gender not in("M","F"):
                    raise InvalidGenderException
                
                marks=list(map(int,input("Enter Marks in 3 subjects: ").split()))
                if len(marks)!=3:
                    raise InvalidMarksException
                
                total=sum(marks)
                percent=round(total/len(marks),2)
                student=[r,name,gender,marks,total,percent]
                Allstudents.append(student)

            f1=open(self.file_name,"w")
            for l in Allstudents:
                for data in l:
                    if isinstance(data,list):
                        for x in data:
                            f1.write(str(x)+" ")
                    else:
                        f1.write(str(data)+" ")
                f1.write("\n")
            f1.close()
            print("All data added to the file!")

        except ValueError:
            print("Please Enter Roll Number or marks in Integer format!")
                
        except InvalidGenderException as e:
            print(e)
        
        except InvalidMarksException as e:
            print(e)
        
        except FileNotFoundError:
            print("The File may not be present or you are in Readonly Mode")
        
        except Exception as e:
            print(e)

    def backUpData(self):
        os.chdir("D\\..")
        print(os.getcwd())
        f1=open(self.file_name,"r")
        f2=open("backup.txt","w")
        f2.write(f1.read())
        print("File Backup Created!")
        f1.close()
        f2.close()
        
    def addNewstudent(self):
        try:
            f3=open(self.file_name,"a")
            print("\n Enter new data! ")
            roll=int(input("Enter Roll Number: "))
            name=input("Enter name: ")
            gender=input("Enter M for Male and F for Female: ")
            marks=list(map(int,input("Enter marks in 3 subjects:").split()))
            total=sum(marks)
            percent=round(total/len(marks),2)
            f3.write(f"{roll} {name} {gender} {marks[0]} {marks[1]} {marks[2]} {total} {percent}\n")
            print("Data Addded to the file!")
            f3.close()
            
        except ValueError:
            print("Please Enter Roll Number or marks in Integer format!")
                
        except InvalidGenderException as e:
            print(e)
        
        except InvalidMarksException as e:
            print(e)
        
        except FileNotFoundError:
            print("The File may not be present or you are in Readonly Mode")
        
        except Exception as e:
            print(e)

F1=FileOperations(2,"Students.txt")
F1.WriteData()
# F1.backUpData()
# F1.addNewstudent()