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


def trib(n):
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1
    return trib(n-1) + trib(n-2) + trib(n-3)

n = list(map(trib,[x for x in range(1,10+1)]))

k = int(input("chislo:"))
n = 1

while True: nb
\\\\\\\\\\\\\\\\     4
    if trib(n) > k:
        break
    else:
        print(trib(n))
        n += 1