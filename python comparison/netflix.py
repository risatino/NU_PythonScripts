import os
import csv

movie = input("What movie are you looking for?")

csvpath = os.path.join('/c/Users/rprezzano/Work Folders/Desktop/NUpython', 'netflix_ratings.csv')

found = False

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
       if statement
       print(row)

