def admission(func):
    def wrappers(*args,**kwargs):
        print("This is a Pune university")
        print(f"This has '{len(args)}' arguments")
        print(f"This has '{len(kwargs)}' keywords argument ")
        func(*args,**kwargs)
        print("Thankyou!")
    return wrappers
'''
@admission
def FE_admission(sname,marks):
    print(f"The student name={sname}")
    print(f"This is a total CET marks={sum(marks)}")
FE_admission("Aneeque",[90,65,82])

@admission
def BSC_admission(a_id,a_name,a_marks,a_category):
    print(f"Applicant ID:{a_id}")
    print(f"Applicant name:{a_name}")
    print(f"Applicant Category:{a_category}")
    print(f"Applicant marks:{a_marks}")
    print(f"Applicant Total Marks:{sum(a_marks)}")
BSC_admission(134,"Ali",a_marks=[76,98,56],a_category="General")

def restaurant(a):
    def wrappers(*args,**kwargs):
        print ("Welcome to the restaurant")
        print(f"This has '{len(args)}' arguments")
        print(f"This has '{len(kwargs)}' keywords argument ")
        a(*args,**kwargs)
        print("Thankyou For Visiting")
    return wrappers

@restaurant
def customer(name,items,price):
    print(f"customer name:{name}")
    print(f"customer items:{items}")
    print(f"customer iems price:{price}")
    print(f"Total amount:{sum(price)}")
customer("ahmed")
'''
# decorators on conditions(if,else)

def even_odd(a):
    def wrapper(num):
            # num=input("Enter a number:")
            # print(f"This has '{len(args)}' arguments")
            # print(f"This has '{len(kwargs)}' keywords argument ")
            if num%2==0:
                 print("your number is even")
                 a(num)
            else:
                print("your number is odd")
                a(num)
    return wrapper

@even_odd
def display(num):
    print("the number is",num)
display(20)
display(13)

def positive_negative(a):
    def wrapper(num):
            if num>0:
                 print("your number is Positive")
                 a(num)
            else:
                print("your number is Negative")
                a(num)
    return wrapper

@positive_negative
def display(num):
    print("the number is",num)
display(20)
display(-13)



