# write a function that calculates the area of a circle
# given the radius

# here' is the function
def circleArea(radius):
    area = 3.14 * radius ** 2
    return area

inner_circle = circleArea(5)
outer_circle = circleArea(10)

# here i am calculating the area of the ring
ring_area = outer_circle - inner_circle

print("The area of the inner circle is", inner_circle)
print("the area of the outer circle is", outer_circle)
print("The area of the ring is", ring_area)