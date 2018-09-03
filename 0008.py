import math
def isPythagoreanElement(a,b,c):
    return c**2 == (a**2 + b**2)

def abcombination(sum):
    b = sum - 1
    a = 1
    returnlist = []
    while (b>a):
        returnlist.append([a,b])
        b -= 1
        a += 1
    return returnlist

c = 997
while (c > 0):
    for i in abcombination(1000-c):
        if isPythagoreanElement(i[0],i[1],c):
            print('Solution found: a ={}, b = {} , c = {}'.format(i[0],i[1],c))
            print('the product of abc = {}'.format(a*b*c))
            break
        else:
            print('Solution not found: a ={}, b = {} , c = {}'.format(i[0],i[1],c))
    c -= 1