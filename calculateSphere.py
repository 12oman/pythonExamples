# take the radius of a sphere as input
# calculate and display:
# the surface area
# and volume of the sphere

# import math
import math


def main():
    print("This program calculates the surface area and volume of a sphere")
    r = eval(input("Please enter the radius of the sphere: "))
    s = 4 * math.pi * r ** 2
    v = 4 / 3 * math.pi * r ** 3
    # 2 decimal places
    print("The surface area of the sphere is:", round(s, 2))
    print("The volume of the sphere is:", round(v, 2))


main()
