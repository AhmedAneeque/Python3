'''
2: create a billing system of a restaurant if the dictioanry of
    receipes are passed to the function
    {"Biryani":450,"chicken 65":300.......}
   the function should display the bill in detail like
   1: Briyani   450
   2: Chicken65 300

   Total Bill Amount    750
   GST 0.06	        45
   Bill amount with GST 795	
'''
def restaurant_bill(recipes):
    total = 0

    print("------ RESTAURANT BILL ------")

    for i, (item, price) in enumerate(recipes.items(), start=1):
        print(f"{i}: {item}    {price}")
        total +=price

    gst_rate = 0.06
    gst = total * gst_rate
    final_amount = total + gst

    print("-----------------------------")
    print(f"Total Bill Amount    {total}")
    print(f"GST {gst_rate}          {gst:.2f}")
    print(f"Bill Amount with GST  {final_amount:.2f}")

recipes = {"Biryani": 450,"Chicken 65": 300}
restaurant_bill(recipes)