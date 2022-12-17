
        #первая

n = int(input("число для проверки: "))
# n = 0
def symma(n):
# for i in range(1,n):
    d = 2                         #проверка является ли простым или нет
    if n % d != 0:
        d += 1
    return d == n

print(symma(n))



# def isSimple(n):
#     for delit in range(2, n//2+1):
#         if n % delit == 0:
#             flag = True
#
#     if flag == False:
#         return True
#
#     if flag == True:
#         return False
#
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if isSimple(n):
#         print(i)
#         sum += i
#
# print (sum)

        #вторая

# for i in range (69451,173459+1):
#     del_count = 0
#     for delit in range(2, i//2+i):
#         if i % delit == 0:
#             del_count += 1
#         if del_count == 0:
#             print(i)