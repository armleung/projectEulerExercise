def CollatzProblem(input):
    count = 1
    while input != 1 : 
        if (input % 2 == 0): # even 
            input = input // 2 
        else :
            input = 3 * input + 1 
        count = count + 1 
    return count 

maxChainNum = 0
maxNum      = 0
for i in range(2,1000000):
    chainNum = CollatzProblem(i)
    if chainNum > maxChainNum:
        maxChainNum = chainNum
        maxNum = i

print ("Number {} have longest chain : {}".format(maxNum,maxChainNum))
    