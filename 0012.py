import math

def getTriangleNumber(n):
    return int((1+n)*n / 2)

def getListofDivisor(n):
    divisors = []
    root = int(math.sqrt(n))
    for x in range(1,root,1):
        if (n % x == 0):
            divisors.append(x)
            divisors.append(int(n/x))
    if (n % root == 0):
        divisors.append(root)
    return divisors


trial       = 0
maxNumofDiv = 0

while maxNumofDiv < 500:
    trial = trial + 1
    divisors = getListofDivisor(getTriangleNumber(trial))
    maxNumofDiv = len(divisors)

#print (getListofDivisor(getTriangleNumber(trial)))
print (trial)
print (getTriangleNumber(trial))
#print (getListofDivisor(getTriangleNumber(trial)))


# Set Lower Bound and upper Bound 
# if number of divisors < 150 , 
#   then lower = upper,  upper x 2
# if number of divisor > 150 
#   then lower unchange , upper = upper + delta / 2
