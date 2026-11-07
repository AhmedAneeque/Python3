class invalidException(Exception):
    def __init__(self,age,message):
        self.message=message
        self.age=age

    def __str__(self):
        return f"age is {self.age} and error{self.message}"

class invalidmarks(Exception):
    def __init__(self,marks,message):
        self.marks=marks
        self.message=message

    def __str__(self):
            return f"marks is {self.marks} and error{self.message}"

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    age=int(input("Enter age of staff: "))
    marks=int(input("Enter your Marks: "))
    c=a+b
    d=a*b
    e=a/b
    f=a-b
    if age<20 or age>60:
        raise invalidException(age,"age must be between 20 to 60")

    if marks<250 or marks>600:
        raise invalidException(marks,"Marks must be between 250 to 600")

except ValueError:
    print("Invalid Value error")
except ZeroDivisionError:
    print("You can not divide a number by zero")
except invalidException as e:
    print(e)
except Exception as e:
    print("Some exception has occured",e)
except Exception as e:
    print("are not elligible")
else:
    print("no exception occured")
    print(c,d,e,f,sep="\t")
finally:
    print("the program execution is finished")

