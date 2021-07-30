# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.

def format_number(number):
    return "{:,}".format(number)


print(format_number(1234))
print(format_number(1234567890))
