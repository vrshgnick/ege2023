    # 1

# def d(n,m):
#     return n % m == 0
#
# for A in range(1, 500):
#     flag = True
#     for x in range(1, 500):
#         if not (not d(x,A)) <= (d(x,6) <= (not d(x,9))):
#             flag = False
#             break
#     if flag == True:
#         print(A)

    # 2

# def d(n,m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if not (d(A,45) and ((d(750,x) <= ((not d(A,x)) <= (not d(120,x)))))):
#             flag = False
#             break
#     if flag == True:
#         print(A)

    # 3

# def d(n,m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if not ((d(x,2)) <= (not d(x,3)) or ((x + A) >= 100)):
#             flag = False
#             break
#     if flag == True:
#         print(A)


    # 4

for A in range(1,500):
    flag = True
    for x in range (1,500):
        if not ((x&41 != 0) <= ((x&33 == 0) <= (x&A != 0))):
            flag = False
            break
    if flag == True:
        print(A)
        break

