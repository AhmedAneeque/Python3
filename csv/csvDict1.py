# reading csv files in Dictionary
import csv

with open("employee.csv","r") as infile:
    csvReader=csv.DictReader(infile)  #This read files in a dictinary
    total=0
    for r in csvReader:
        if r["City"]=="Malegaon":
            r["basic_salary"]=(float(r["basic_salary"])*1.1)
            print(type(r["basic_salary"]))
            total+=int(r["basic_salary"])
        print(r)
    infile.close()
    print(f"Total Salary:{total}")

    # for row in csvReader:
    #     print(row)
    #     total+=int(row["basic_salary"])
    