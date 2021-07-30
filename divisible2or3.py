# Given two integers
# write a method that returns their multiplication
# if they are both divisible by 2 or 3
# otherwise returns their sum.


def divisible2or3(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a * b
    elif a % 3 == 0 and b % 3 == 0:
        return a * b
    else:
        return a + b

# test cases:
# Expected input and output


# Enter two integers: 15, 30
# Divisible By 2 Or 3(15, 30) → 450
print(divisible2or3(15, 30) == 450)

# Enter two integers: 2, 90
# Divisible By 2 Or 3(2, 90) → 180
print(divisible2or3(2, 90) == 180)

# Enter two integers: 7, 12
# Divisible By 2 Or 3(7, 12) → 19
print(divisible2or3(7, 12) == 19)
