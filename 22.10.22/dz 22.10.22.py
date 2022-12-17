            #первая задача

# mas = [10,20,30,40,9,8,3,6,5]
# print ("дан массив:", mas)
#
# b1 = (mas[0])
# b2 = (mas[1])
# b3 = (mas[2])
# b4 = (mas[3])
# b5 = (mas[4])
# b6 = (mas[5])
# b7 = (mas[6])
# b8 = (mas[7])
# b9 = (mas[8])
# print ("числа:", b1,b2,b3,b4,b5,b6,b7,b8,b9)
#
# a1 = len(mas[:0])
# a2 = len(mas[:1])
# a3 = len(mas[:2])
# a4 = len(mas[:3])
# a5 = len(mas[:4])
# a6 = len(mas[:5])
# a7 = len(mas[:6])
# a8 = len(mas[:7])
# a9 = len(mas[:8])
# print ("номер индексa:", a1,a2,a3,a4,a5,a6,a7,a8,a9)
#
# minimal = min(mas)
# print ("минимальное число массива:", minimal)
#
# print ("кароче вон там все видно если сопоставить как бы тройка это шестой элемент, все шесть да либо минус третий.")

            #нормальное решение

# array = [1,2,3,4,5,1]
# print (array)
# min = max(array)
# index = 0
# for i in range(len(array)):
#     if array[i] <= min:
#         min = array[i]
#         index = i
# print ("min = ", min)
# print ("index = ", index)



        #вторая задача

# array = [1,2,3,5,1,6,7,8,5,3,3,3,3,3,3,6,2]
# max_index = array.index(max(array))
# max_index = 0
#
# min = max(array)
# sum = 0
#
# for i in range(len(array)):
#     if array[i] <= min:
#         min = array[i]
#         min_index = i
# for i in range(max_index+1, min_index):
#     sum += array[i]
#
# print (sum)

            #пятая задача

# array = [1,2,3,4,5,2,3,2,2,2,2,3,2,2,2,2,2,2,2,2,1]
#
# count = 1
# maxCount = 0
# for i in range(len(array)-1):
#     if array[i] == array[i+1]:
#         count += 1
#         if count > maxCount:
#             maxCount = count
#     else:
#         count = 1
# print (maxCount)

            #третья задача

# array = [2,3,5,2,6,8,10,10,2,4]
#
# addIndex = 0
# evenIndex = 0
#
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#         evenIndex = i
#     else:
#         addIndex = i
#
# sum = 0
#
# for i in range(addIndex + 1, evenIndex):
#     sum += array[i]
#
# print(sum)

            #четвертая задача

# array = [2,3,5,2,2,6,8,10,12,4]
#
# maxCount = 0
# count = 0
#
# for elem in array:
#     count = array.count(elem)
#     if count > maxCount:
#         maxCount = count
# print(maxCount)
