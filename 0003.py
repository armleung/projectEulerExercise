import math

n = 600851475143 
maxPrime = 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

print(maxPrime)