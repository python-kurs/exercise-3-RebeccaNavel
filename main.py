# Exercise 3

from pathlib import Path
import utils as u
import csv

# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

carsdir = Path (data_dir, "cars.txt")

# 2. Read the text file [2P]

with open (carsdir, "r") as file:
    cars = file.readlines ()
    
# 3. Count the occurences of each item in the text file [2P]

car_count = u.countwords (cars)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

Path ('C:\Users\User\Documents\GitHub\exercise-3-RebeccaNavel\solution').mkdir (parents = True, exist_ok = True) 

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

counts = output_dir / "counts.csv"

with open (counts, "w") as f:
    writer = csv.DictWriter (f, fieldnames = ["item", "count"]) 
    writer.writeheader ()
    for key in car_count.keys():
        f.write ("%s,%s\n"%(key,car_count[key]))  