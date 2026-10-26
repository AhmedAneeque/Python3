def amount_discount(price,qty):
    amount=price*qty
    if amount>=10000:
        discount=0.1
    elif amount>=5000:
        discount=0.05
    else:
        discount=0
    return amount-(amount*discount)

a=amount_discount(10000,6)
print(a)

a=amount_discount(2500,5)
print(a)

a=amount_discount(500,3)
print(a)