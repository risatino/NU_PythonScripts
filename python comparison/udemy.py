import os
import csv

csvpath = os.path.join('/c/Users/rprezzano/Work Folders/Desktop/NUCHI201801DATA4-Class-Repository-DATA', "..", "Resources", 'WebDevelopment.csv')

# lists
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
       if statement
       print(row)