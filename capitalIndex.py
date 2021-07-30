# Write a function named capital_indexes.
#
# The function takes a single parameter,
# which is a string.
#
# Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(str):
    return [i for i, letter in enumerate(str) if letter.isupper()]


print(capital_indexes("HeLlo"))  # => [0, 1, 2]
