x=lambda a:a*2
print(x(20))

lambda a,b:a+b
print((lambda a,b:a+b)(10,20))

print((lambda a,b:a if a>b else b)(25,80))

import math
print((lambda a:math.sqrt(a)+a**12)(8))

print((lambda a,b,c:a if a>b and a>c else(b if b>a and b>c else c))(20,30,45))

print((lambda v:v.upper())("hello"))
# v="python"
# print(v.upper())

n=[24,45,76,95,34]
x=lambda n:0 if n%2==0 else 1
print(list(map(x,n)))

print(list(map((lambda n:0 if n%2==0 else 1),[32,75,34,86,46])))
