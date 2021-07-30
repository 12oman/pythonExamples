# take distance accepting either km/hr or mph
# and time as input
#
# calculate the speed in both km/hr and mph
# kilometers per hour and miles per hour.

print('This program will calculte traveling speed')
print(f"you'll need to know the distance and time")
print("and the unit of distance that you're using")


def get_unit():
    unit = input(
        'what unit of distance are you using? [K]ilometers or [M]iles: ')
    # change this to a switch case statement?

    if unit == 'K' or unit == 'k' or unit == 'Kilometers':
        unit = 'K'
    elif unit == 'm' or unit == 'M' or unit == 'Miles':
        unit = 'M'
    else:
        print('invalid unit')
        get_unit()
    return unit


unit = get_unit()
print(unit)

if(unit) == 'K':
    dist = float(input('what is the distance? '))
    time = float(input('what is the time? '))
    speed = dist/time
    speedMph = speed * 0.62137
    print(f'you are traveling {speed} km/hr')
    # the funny :.2f just means 2 decimal places
    print(f'Your speed in MPH is: {speedMph:.2f}')
else:
    dist = float(input('what is the distance? '))
    time = float(input('what is the time? '))
    speed = dist/time
    speedKm = speed * 1.60934
    print(f'you are traveling {speed} mph')
    print(f'Your speed in KM is: {speedKm:.2f}')


#     dist = float(input('Enter distance in kilometers: '))
#     time = float(input('Enter time in hours: '))
#     speedKm = dist/time
#     speedMph = speedKm * 0.621371
#     print(f'Your speed in KPM is: {speedKm}')
#     # round to 2 decimal places
#     print(f'Your speed in MPH is: {speedMph:.2f}')

#     dist = float(input('Enter distance in miles: '))
#     time = float(input('Enter time in hours: '))
#     speedM = dist/time
#     speedKm = speedM * 1.60934
#     print(f'Your speed in miles per hour is: {speedM}')
#     # round to 2 decimal places
#     print(f'Your speed in KPH is: {speedKm:.2f}')
