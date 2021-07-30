# Given a temperature in Celsius
# degrees,
# write a method that converts it to Fahrenheit degrees or vice versa.
# Remember that temperature below -271.15C (absolute zero) does not exist!

# convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "That temperature does not exist!"
    # [(Celsius  value) × (9/5)] + 32
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

# Expected Input and Output:
# test function celcius to fahrenheit


def test_celsius_to_fahrenheit():
    print(celsius_to_fahrenheit(-15) == "That temperature does not exist!")

# convert fahrenheit to celsius


def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        return "That temperature does not exist!"
    # formular for celsius from fahrenheit
    # [(Fahrenheit value) - (32)] * (5/9)
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


#  test function fahrenheit to celsius
# get some reliable data later
print(celsius_to_fahrenheit(-15))
