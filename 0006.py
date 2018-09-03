sum = 0
series = range(1,101,1)
for i in series:
    print('i loop : ', i)
    j = i
    while(j < 100):
        sum += i * series[j]
        print('summing  {} * {} '.format(i,series[j]))
        j = j + 1
print(2*sum)