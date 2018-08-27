def naturalNumber(input):
    resultList = []
    for i in range (input):
        if ((i%3 == 0) or (i%5==0)):
            resultList.append(i)
    return resultList

print (sum(naturalNumber(1000)))