import time
import threading
import os

def file_read_write(file1,file2):
    print(os.getcwd())
    os.chdir("D:\\Aneeque Python")
    print(os.getcwd())
    print(time.ctime())

    mydata=""
    with open(file1,"r") as f1:
        mydata=f1.read()
        print(mydata)
        f1.close()

    os.chdir("D:\\Aneeque Python\\MULTITHREADING")
    with open(file2,"w") as f2:
        f2.write(mydata)
        f2.close()

# file_read_write("Employee.txt","new_employee.txt")
t1=threading.Thread(target=file_read_write,args=("Employee.txt","new_employee.txt"))
t1.start()
t1.join()
