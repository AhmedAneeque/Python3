import time
import threading
'''
# passing arguments to a function by using threads
def f1(a,b,c):
    print("this is function")
    print(f"{a}  {b}  {c}")

t1=threading.Thread(target=f1,args=("Data","Tables","Columns"))
t1.start()
'''
sq=[]
cb=[]

def Square(s,e,a,Name,Version):
    for i in range(s,e):
        # print(a,time.strftime(" %H:%M:%S --"),":",i*i)
# This Both function is used to print time
        print(a,time.ctime(),":",i*i)
        print(Name,Version,sep="\t")
        sq.append(i*i)
        time.sleep(2)

def Cubes(s,e,b,Name,Version,Year):
    for i in range(s,e):
        print(b,time.strftime(" %H:%M:%S --"),":",i*i*i)
        print(Name,Version,Year,sep="\t")
        cb.append(i*i*i)
        time.sleep(2)

t1=threading.Thread(target=Square,args=(1,5,"Square"),kwargs={"Name":"Thread1","Version":1.15})
t2=threading.Thread(target=Cubes,args=(10,15,"Cubes"),kwargs={"Name":"Thread2","Version":2.25,"Year":2024})

t1.start()
t2.start()
t1.join()
t2.join()

print(sq)
print(cb)