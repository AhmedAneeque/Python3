import time
import threading
def display():
    l1=[4,5,6,8,9,3,4]
    for i in l1:
        print("Display",i)
        time.sleep(1)

def sum():
    l1=[4,6,8,4,9,8,7,6,4,3]
    s=0
    for i in l1:
        s+=i
        print("sum",s)
        time.sleep(1)

def string():
    s1="python"
    l1=[]
    for i in s1:
        l1.append(i)
        print(l1)
        time.sleep(1)

t1=threading.Thread(target=display)
t2=threading.Thread(target=sum)
t3=threading.Thread(target=string)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()