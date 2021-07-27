# a*(b%c)
# a*b%c

a = 10
b = 20
c = 30

print(a*(b%c))
print(a*b%c)

def quadraticOne(a, b, c):
    return a*(b%c)

def quadraticTwo(a, b, c):
    return a*b%c

# test if the return value of quardraticOne is the same as the return value of quadraticTwo
print(quadraticOne(a, b, c) == quadraticTwo(a, b, c))

