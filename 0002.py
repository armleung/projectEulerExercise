# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Even : F(2), F(5), F(8)
# F(2) : 2
# F(5) : 8
# F(8) : 34
# F(11): 89+55 = 144
# F(n) = 4*F(n-3)+F(n-6) 

a = 2 #F(0)
b = 8 #F(1)
fib = 0
totalnumber = 10

while fib < 4000000: # O(n)
    print ('fib value is ',fib)
    totalnumber += fib
    fib = 4 * b + a
    a = b 
    b = fib 

print ('Final Sum is ',totalnumber)