temp_path.pyimport os
import csv

os.chdir("\c\users\rprezzano\Work Folders\Desktop\NUCHI201801DATA4-Class-Repository-DATA\MWS\Activities\03-Python\3\Activities\10-Stu_UdemyZip\Resources")

# lists
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

csvpath = "webDevelopment.csv"

with open(csvpath, newline='', encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
       print(row)