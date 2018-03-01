# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print all of the candies to the screen and their index in brackets
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

# Run through a loop which allows the user to choose which candies to take home with them
for x in range(allowance):
    selected = input("Which candy would you like to bring home? ")

    # Add the candy at the index chosen to the candyCart list
    candyCart.append(candyList[int(selected)])

# Loop through the candyCart to say what candies were brought home
print("I brought home with me...")
for candy in candyCart:
    print(candy)

# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
# for x in range(10):
#     print(x)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
# for x in range(20,30):
#     print(x)

# If a list is provided, then the For loop will loop through each element within the list
# for x in ["Peanut","Butter","Jelly","Time","Is","Now"]:
#     print(x)

# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")
