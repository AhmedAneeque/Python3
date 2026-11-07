import os
os.chdir("D:\\Aneeque Python")
'''
with open("Salary.txt","r+") as f1:
    # it read + write data in the file
    print(f1.read())
    f1.seek(0) #it takes the pointer to the any lines
    f1.truncate() #it deletes the data from the file
    f1.write("Hello")
    f1.seek(0)
    print(f1.read())
'''
with open ("Salary.txt","a+") as f2:
    # it append + read data
    f2.seek(0)
    print(f2.read())
    f2.write("Product name-CPU QTY-3 Amount-5000 \n")
    f2.seek(0)
    print(f2.read())
    f2.write("Product name-Monitor QTY-3 Amount-5000\n")
    f2.seek(0)
    print(f2.read())
    f2.write("Product name-Keybord QTY-4 Amount-1000\n")
    f2.seek(0)
    print(f2.read())
    
    

