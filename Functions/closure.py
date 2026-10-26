def example1():
    a=100
    def inner():
        b=20
        return a*b
    return inner
x=example1()
print(x())


def counter():
    n=0
    def count():
        nonlocal n
        n+=1
        return n
    return count
a=counter()
print(a())
print(a())
print(a())

