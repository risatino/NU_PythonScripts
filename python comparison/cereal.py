# Dependencies
import os
import csv

cereal_csv = os.path.join("c:\users\rprezzano\Work Folders\Desktop\NUpython\cereal.csv", "cereal.csv")

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Iterate through each row
    for row in csvreader:
        if statement
        print(row)

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >=5:
            print(row)