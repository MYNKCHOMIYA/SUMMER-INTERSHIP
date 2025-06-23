#csv files (COMMA seperate VALUES)

import csv

data = [
    ["name", "age", "country_names"],
    ["abc", "25" ,"india"],
    ["raju","34","japan"],
    ["ram","23","arab"],
    ["me","19","goa"]

]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for x in data:
        writer.writerow(x)


with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)








