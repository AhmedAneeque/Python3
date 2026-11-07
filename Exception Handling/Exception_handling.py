# Exception Handling:This is used to handle any exceptions(value error, divide by zero error,
# no file file error,index not found error etc)
for i in range(5):
    try:
        n1=int(input("enter a number:"))
        n2=int(input("enter another number:"))
        print(f"Division {n1/n2}")
    except Exception as e:
        print(e)

try:
    l=[25,67,54,78,34]
    print(l[0])
    print(l[3])
    print(l[45])
except Exception as e:
    print(e)

try:
    with open ("data.txt","r") as f1:
        print(f1.read())
        f1.close()
except Exception as e:
    print(e)
    