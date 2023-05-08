#программа для удаления элементов кратных числу 3
# task 1

# array = [1,2,5,17,9,13,15,19]
# for i in array:
#     if i%3 == 0:
#         array.remove(i)
# print(array)

# даны 2 массива, добавить в первый элемент второго и отсортировать по убыванию
# task 2


array1 = [1,2,5,7,9,13,15,19]
array2 = [3,4,6]
for i in array2:
    array1.append(i)
# print (array1)
array1.sort(reverse=True)
print (array1)
