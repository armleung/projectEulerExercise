#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math

finalPrimeSeries = [2]
trialNumber = 3

def isPrime(n):
    if n == 1 :
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif (n % 2) == 0 :
        return False
    elif n < 9 : # we have already excluded 4,6 and 8.
        return True
    elif (n % 3) == 0:
        return False
    else:
        r = int(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f<=r : 
            if (n % f) == 0 : return False #(and step out of the function)
            if (n %(f+2)) == 0 : return False #(and step out of the function)
            f=f+6
    return True

while trialNumber < 2000000:
    if isPrime(trialNumber):
        print(trialNumber)
        finalPrimeSeries.append(trialNumber)
    
    trialNumber += 2

print(sum(finalPrimeSeries))
