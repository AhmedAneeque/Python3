# fibonacci using recursion
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f=fibonacci(n-1)+fibonacci(n-2)
    return f

for i in range(10):
    print(fibonacci(i))

#factorial using recursion
def fact(n):
    if n==1:
        return 1
    else:
        f=n*fact(n-1)
    return f

print(fact(5))