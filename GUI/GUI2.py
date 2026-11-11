from tkinter import *
root=Tk()
root.title("Simple GUI") 
# root.configure(bg="lightblue")

def display():
    print("Registration Successful!")
def display1():
    print("Exitted successfully")

L1=Label(root,text="Enter username:",font=("Cambria",20,"bold"),padx=10,pady=10)
L1.grid(row=0,column=0)
username=Entry(root,font=("Cambria",20,"bold"))
username.grid(row=0,column=1,padx=10,pady=10)

L2=Label(root,text="Enter email:",font=("Cambria",20,"bold"),padx=10,pady=10)
L2.grid(row=1,column=0)
email=Entry(root,font=("Cambria",20,"bold"))
email.grid(row=1,column=1,padx=10,pady=10)

L3=Label(root,text="Enter Mobile_Number: ",font=("Cambria",20,"bold"),padx=10,pady=10)
L3.grid(row=2,column=0)
Mobile_Number=Entry(root,font=("Cambria",20,"bold"))
Mobile_Number.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Password:",font=("Cambria",20,"bold"),padx=10,pady=10)
L4.grid(row=3,column=0)
password=Entry(root,font=("Cambria",20,"bold"),show="*")
password.grid(row=3,column=1,padx=10,pady=10)

L5=Label(root,text="Verify Password:",font=("Cambria",20,"bold"),padx=10,pady=10)
L5.grid(row=4,column=0)
Verify_password=Entry(root,font=("Cambria",20,"bold"),show="*")
Verify_password.grid(row=4,column=1,padx=10,pady=10)

B1=Button(root,text="Submit",font=("Arial",15,"bold"),bg="Green",fg="White",command=display)
B1.grid(row=5,column=0)
B2=Button(root,text="Exit",font=("Arial",15,"bold"),bg="Red",fg="White",command=display1)
B2.grid(row=5,column=1)
root.mainloop()