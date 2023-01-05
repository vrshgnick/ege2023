        # ПРИМЕР

# import sys
#
#
# def f(n):
#     sys.setrecursionlimit(2500)
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1)
#
# print(f(2023)/f(2020))

            # 1

# def mod(a,b):
#     return a%b
# def(n):
#     if n == 0:
#         return 0
#     if n > 0  and mod(n,3) == 0:
#         return f(n/3)
#     if mod (n,3) > 0:
#         return mod (n,3) + f(n = mod(n,3))
#     for n in range(0,1000):
#         if f(n) == 11:
#             print(n)
#             break


            # 2


# def f(n):
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return n + f(n-1)
#     if n > 1 and n%2 != 0:
#         return 2*f(n-2)
#
# print(f(26))


           # 3

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n%2 == 0:
#         return f(n/2)
#     if n%2 != 0:
#         return 1 + f(n-1)
#
# c = 0
#
# for n in range(1, 1000 + 1):
#     if f(n) == 3:
#         c += 1
# print(c)


            # 4

# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n-1) + 2**(n-1)
#
# print(f(18))


            # 5

# 1 1 2 3 5 8 13 21 34
 # answer 21