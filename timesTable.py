# display the multiplication table of a given integer.
# Input the number (Table to be calculated): 15
# Expected Output: 15 X 1 = 15 ... ... 15 X 10 = 150

def timesTable(number):
    for i in range(1, 11):
        print(number, "X", i, "=", number * i)


# get the number to be multiplied
number = int(input("Enter the number for the (Table to be calculated): "))
timesTable(number)
