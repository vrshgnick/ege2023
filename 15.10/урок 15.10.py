#     # сколько двоек в массиве (.count)
#
# a = [1,2,3,4,5,2,3,4,6,8,4]
# print (a.count(2))
#
# a = "111234"
# print (a.count(2))

#     # последнее значение
#
# a = "1234"
# print (a[:1])



# c = 60
# for i in range(2, c//2 +1):
#     if c % i == 0:
#         print(i)

# for i in range(10,21):
#     for i in range(2,c//2 +1):
#         if c % i == 0:
#             print(i)


# for num in range(10,100):
#     print(f"num = {num}")
#     sum = 0
#     for delit in range(2, num//2 + 1):
#         if num % delit == 0:
#             sum += 1
#     if sum == 0:
#         print (f"{sum} - prostoe chislo")
#     print (f"кол-во делителей = {sum}")



# min = 999999
#
# for i in range (0, 100):
#     if i < min:
#         min = i
# print(min)


# a = 14
# a2 = (bin(a)[2:])
# a8 = (oct(a)[2:])
# a16= (hex(a)[2:])
# print (a2,a8,a16)
# print()
#
# b = int(a16,16)
# print(b)
# print()
#
# a10 = int(a2, 2)            #перевод из Н в 10ую сс
# print(a10)
# print()
# a10 = int(a8, 8)
# print (a10)