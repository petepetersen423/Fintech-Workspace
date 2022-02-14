import csv
from pathlib import Path
from turtle import clear

csvpath = Path("quarterly_data.csv")

print(csvpath.absolute())
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
