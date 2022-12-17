        #5 дз

array = [1,2,3,4,5,2,3,2,2,2,2,3,2,2,2,2,2,2,2,2,1]

count = 1
maxCount = 0
for i in range(len(array)-1):
    if array[i] == array[i*1]:
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1
print (count)


