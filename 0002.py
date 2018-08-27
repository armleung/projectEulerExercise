a = 0 
b = 1 
fib = 0
totalnumber = 0

while fib < 4000000:
    print ('fib value is ',fib)
    if (fib %2 == 0):
        totalnumber += fib
    fib = a + b
    a = b 
    b = fib 

print ('Final Sum is ',totalnumber)