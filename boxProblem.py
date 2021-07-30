from math import floor

# get the user to imput a number
items = int(input("Please enter the number of items: "))

# calculate the number of big items
big = floor(items // 5)

# calculate the number of medium items
medium = floor(items % 5 / 3)

# calculate the number of small items
small = (items % 5) % 3

# calculate the total items
total = big + medium + small

# print out the the boxes used
print("total Boxes used: ", total)
# print out the number of big boxes
print("Number of big boxes used: ", big)

# print out the number of medium boxes
print("Number of medium boxes used: ", medium)

# print out the number of small boxes
print("Number of small boxes used: ", small)
