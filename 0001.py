target = 999

def naturalNumber(input): # O(n)
    sum = 0
    for i in range (input):
        if ((i%3 == 0) or (i%5==0)):
            sum += i 
    return sum

def SumDivisibleBy(n): # O(1)
    p = int(target/n)
    return int(n*(p*(p+1)) / 2)

print (SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15))
#print (naturalNumber(1000))