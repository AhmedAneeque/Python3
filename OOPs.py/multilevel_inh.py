# Multilevel Inheritance
class Products():
    def __init__(self,pid):
        self.pid=pid
        print("Products")

class category(Products):
    def __init__(self, pid,pcategory, pname,price):
        super().__init__(pid)
        self.pname=pname
        self.pcategory=pcategory
        self.price=price
        print("Category")

class Order(category):
    def __init__(self, pid, pcategory, pname, price,qty,payment_method):
        super().__init__(pid, pcategory, pname, price)
        self.qty=qty
        self.payment_method=payment_method
        print("Order")

    def amount(self):
        print("Order Details:")
        print(self.pid,self.pcategory, self.pname, self.price,self.qty,self.payment_method,sep="  ")
        return self.qty*self.price
    
O1=Order(101,"Electronic","Airpod",20000,4,"COD")
O2=Order(102,"Electronic","Laptop",90000,1,"UPI")
O3=Order(103,"Home Appliances","Mixture",2800,2,"Cash")
Orders=[O1,O2,O3]
total_amount=0
print("Total Bill Amount")
for o in Orders:
    total_amount+=o.amount()
print("Total Bill Amount=",total_amount)

