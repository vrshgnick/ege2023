array = [1,2,3,4,5,3,5,2,8,9,12,3,4,3,3,3]
for i in array:
    if i%2 == 0:
        array.remove(i)
    if i%3 == 0:
        array.remove(i)

print(array)



array = [1,2,3,4,5,3,5,2,8,9,12,3,4,3,3,3]
print(array)

while array.count(3) > 3:
    array.remove(3)

for i in array:
    if i%2 == 0:
        array.remove(i)
print (array)



