        # №16
    # 1

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n%2 == 0:
#         return f(n / 2)
#     if n%2 != 0:
#         return 1 + f(n - 1)
# k = 0
# for i in range(1,1001):
#     if f(i) == 3:
#         k += 1
# print (k)

    # 2

# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return f(n - 1) * (n - 2) * f(n - 2)
# print(f(6))


    # 3

# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + (2 ** n - 1)
# print (f(10))

    # 4

# def f(n):
#     if n == 1:
#         return 0
#     if n > 1:
#         return f(n - 1) + n
#
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return g(n - 1) * n
#
# print(f(5) + g(5))

    # 5

# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) * f(n - 1) - f(n - 1) * n + 2 * n
# print (f(4))

    # 6

# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return (n * (n - 1) * f(n - 1))
# print(f(123)/f(120))
