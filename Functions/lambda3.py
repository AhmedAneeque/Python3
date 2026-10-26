import functools

find_ods=lambda a:a%2==0
print(list(filter(find_ods,[45,20,33,45,85,40,66,80])))

names=["Ali","Sahil","Abdullah","Abdul Rahman Khan","Abdul Salam"]
find_small_names=lambda n:len(n)<=6
# print(find_small_names("Ali"))
print(list(filter(find_small_names,names)))

marks=[25,74,85,65,65]
largest_number=lambda a,b:a if a<b else b
print(functools.reduce(largest_number,marks))

marks=[2,7,8,5,5]

# total_marks=lambda a,b:a+b
# print(total_marks(25,10))

print(functools.reduce(lambda a,b:a+b,marks)/len(marks))


