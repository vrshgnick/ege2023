# def f(n):
#     if n == 0:
#         return 1
#     return n = f(n-1)
# print (f(5))

####################################################

# n = int(input("chislo: "))
# c = 1
# for i in range  (1,n+1):
#     c *= i
#     print (c)

#################################################

# a = [1123,243,333222,4444,565,1123,222,23,4,5111111]
# for i in a:
#     num = str(i)
#     print(len(num))

#####################################################


# num_lengths = map(len,["peter","ann"])
# print(list(num_lengths))


# def fact(n):
#     if n == 0:
#         return 1
#     return n = fact(n-1)
#
# nums = [x for x in range (10)]
#
# nums_fact = list(map(float,nums))
#
# print(nums_fact)


#####################################################


# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# def square(n):
#     return n**2
#
# nums = [x for x in range(1,10+1)]
# print(nums)
#
# # map(func, elem) - применяет функцию к аргументам, которые мы передаем
#
# nums_fact = list(map(fact,nums)) # перевод элементов списка в различные типы данных
# nums_square = list(map(square,nums))
#
#
# print(nums_square)
# print(nums_fact)
#
#
# # анонимные функции
#
# nums2 = list(map(lambda x,y: x + y, [1,3,5,17,9],[2,4,6,8,0]))
#
# nums_tosquare = list(zip(nums, nums_square)) # packing
# print(nums_tosquare)
#
# n2, ns2 = zip(*nums_tosquare) # распаковка
#
# print(n2)
# print(ns2)

#####################################################################################

#
# num1 = 1
# num2 = 1
#
# for i in range(50):
#     num1, num2 = num2, num1 + num2
#
#     print(num2)

        # Фибаначи

# def fib(n):
#     if n == 1:
#         return 1
#     if n ==2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# n = list(map(fib,[x for x in range (1,10+1)]))
#
# print(n)

           # Трибаначи

# 0, 0, 1, 1, 2, 4, 17, 13, 24, 44, 81, 149

# def trib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 0
#     if n == 3:
#         return 1
#     return trib(n-1) + trib(n-2) + trib(n-3)
#
# n = list(map(trib,[x for x in range(1,12+1)]))
#
# print(n)

#################

#все числа трибаначи которые < или = k


# def trib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 0
#     if n == 3:
#         return 1
#     return trib(n-1) + trib(n-2) + trib(n-3)
#
# n = list(map(trib,[x for x in range(1,10+1)]))
#
# k = int(input("chislo:"))
# n = 1
#
# while True:
#     if trib(n) > k:
#         break
#     else:
#         print(trib(n))
#         n += 1


