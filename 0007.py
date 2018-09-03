finalPrimeSeries = [2]
totalPrimeNumber = 1
trialNumber = finalPrimeSeries[-1] + 1

def isPrime(targetNum):
    for i in finalPrimeSeries :
        if (targetNum % i == 0):
            return False
    return True

while (totalPrimeNumber < 10001):
    if (isPrime(trialNumber)):
        finalPrimeSeries.append(trialNumber)
        totalPrimeNumber += 1
        print ("The {}th primeNumber is {}".format(totalPrimeNumber,trialNumber))
    
    trialNumber += 2

print ("The {}th primeNumber is {}".format(totalPrimeNumber,trialNumber-1))
    