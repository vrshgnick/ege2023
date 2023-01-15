    # 5.10468

# 512 -> [5,1,2] -> sum = 8
# '10011' -> ['1','0','0','1','1'] -> применяем int к каждому элементу списка -> [1,0,0,1,1] -> сумма =

# for n in range(1000):
#     n2 = bin(n)[2::]   # двоичная запись числа n
#     s = sum(list(map(int,list(n2))))    # нашли сумму
#     n2 += str(s%2)
#     s = sum(list(map(int,list(n2))))    # нашли сумму
#     n2 += str(s%2)
#     r = int(n2,2)
#     if r > 77:
#         print(n)
#         break


    # 5.16882

# for n in range(0,256):
#     n2 = bin(n)[2::]
#     while len(n2) < 8:  # дополнение нулями
#         n2 = '0' + n2
#     n2 = n2.replace('1','*')
#     n2 = n2.replace('0','1')
#     n2 = n2.replace('*','0')
#     print(n2)
#     r = int(n2,2)
#     if r-n == 111:
#         print(n)

# for n in range(255, -1,-1):
#     n2 = bin(n)[2::]
#     while len (n2) < 8:
#         n2 = '0' + n2
#     r = int(n2,2)
#     realn = 255 - n
#     if r - realn == 111:
#         print (realn)

    # 5.13617

for n in range(100,1000):
    n = str(n)
    mult1 = int(n[0]) * int(n[1])
    mult2 = int(n[1]) * int(n[2])
    r = str(max(mult1,mult2)) + str(min(mult1,mult2))
    if r == '123':
        print(n)
        break

    # 5.14767

for n in range(1000,10000):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])

1 способ записи

    a = []
    a.append(s1)
    a.append(s2)
    a.append(s3)
    a = sorted(a)
    r = str(a[1])+ str(a[2])

2 способ записи (лучше)

    r = str(s1 + s2 + s3 - max(s1,s2,s3) - min(s1,s2,s3)) + str(max(s1,s2,s3))

    if r == '613':
        print(n)
        break
