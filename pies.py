# Part 1: single quotes usually means one character rather than a string

cart = 'y'

purchased = []

# pie_list

#Create an order form that will display a list of pies to the user in the following way:
print("Welcome to the House of Pies! Here are our pies: (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak)"

# while

# Then prompt the user to select which pie they'd like to order via number.
pie = {}
pie['Pecan'] = 1
pie['Apple Crisp'] = 2
pie['Bean'] = 3
pie['Banoffee'] = 4
pie['Black Bunn'] = 5
pie['Blueberry'] = 6
pie['Buko'] = 7
pie['Burek'] = 8
pie['Tamale'] = 9
pie['Steak'] = 10

# Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you.` and then ask if they would like to make another order. If so, repeat the process.

for x in pie.keys():
    print pie[x]

# print("Great! We'll have that" + pie_list[int(piechoice) - 1] "right out for you.")

# Once the user is done purchasing pies, print the total number of pies ordered. Add a counter to the input amount.

### solved

# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List 
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", 
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

  # Show pie selection prompt 
  print("---------------------------------------------------------------------")
  print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
                     " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
                     " (9) Tamale, (10) Steak ")

  pie_choice = input("Which would you like? ")

  # Add pie to the pie list
  pie_purchases.append(pie_choice)

  print("------------------------------------------------------------------------")

  # Inform the customer of the pie purchase
  print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

  # Provide exit option
  shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete 
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + "." )