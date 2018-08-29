def isPalindrome(number):
    result = True
    compare = str(number)
    n = (int)(len(compare) / 2)
    i = 0
    while i < n:
        result &= (compare[i] == compare[-(i +1) ])
        i = i+1
    return result

largestPalindrome = 0
a = 999
while a >= 100:
    if (a % 11 == 0):
        b = 999
        db = 1
    else:
        b = 990 #The largest number less than or equal 999
        #and divisible by 11 
        db = 11
    while b >= a:
        if a*b <= largestPalindrome:
            break
        if isPalindrome(a*b):
            largestPalindrome = a*b
        b = b-db
    a = a-1
print(largestPalindrome)