
'''1: create a user defined function to perform following task
   electricity units of 5 consumers are given to the function      (argument) in the form of a dictionary
   calculate the bill amount of each consumer and return it 
   in the form of a list
  {"abdullah":120,"Ali":250.................}
   follow the below criteria to calculate the bill amounts
   a: all consumers must pay a fixed amount of 100
   b: for each unit between 1 to 200, the electricity rate will be rs 3 per unit
   c: for each unit between 201 to 300, the rate should be rs 4 per unit
   d: for each unit between 301 to 400, rate should be rs 5 per unit
   e: d: for each unit between 401 to 500, rate should be rs 6 per unit
   f: for all units above 500, rate should be rs 7 per unit
'''

def electricity_bill (consumers):
    bill_list=[]

    for units in consumers.values():
        if units<=200:
            amount=100+units*3
        elif units>200 and units<=300:
            amount=700+(units-200)*4
        elif units>300 and units<=400:
            amount=1100+(units-300)*5
        elif units>400 and units<=500:
            amount=1600+(units-400)*6
        else:
            amount=2200+(units-500)*7
        bill_list.append(amount)
    return bill_list


list_of_consumers={"abdullah":120,"Ali":250,"rahul":370,"raju":500,"ahmed":540}
bill_amount=electricity_bill(list_of_consumers)
print("calculated bill list",bill_amount)