#function definition 
def create_dictionary(pnames,prices):
    products=dict()
    if len(pnames)!=len(prices):
        print("pnames and prices are does not match ")
    else:
        for i in range (len(pnames)):
            products[pnames[i]]=prices[i]
    return products 

#function call
a=create_dictionary(["keyboard","Monitor","Printer","Mouse"],[600,4000,15000,400])
print(a)    

a=create_dictionary(["orange","Mango","apple","banana"],[100,250,150,30])
print(a) 

