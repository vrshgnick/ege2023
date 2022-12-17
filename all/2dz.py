#больше памяти памяти
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > 0:
#     a = a
# else:
#     a = 0
# if b > 0:
#     b = b
# else:
#     b = 0
# if c > 0:
#     c = c
# else:
#     c = 0
#
# print(a + b + c)

#меньше памяти

sum = 0

for i in range (3):
    num = int(input())
    if num >= 0:
        sum += num
print(sum)