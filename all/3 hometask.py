# n = 0
# int(input(""))
# for i in range(1,n + 1):
#     n = n + i
# print(n)
#
#
#
# sum = 0
# n = int(input(""))
# for n in range(1,n + 1):
#     sum = sum + n
# print (sum)

sum = 0
n = int(input("vvedite chislo n "))
if n < 1:
    for i in range(1,n):
        sum = sum + i
    print (sum)

or:

if n > 1:
    for i in range(n,1):
        sum = sum + i
    print (sum)

