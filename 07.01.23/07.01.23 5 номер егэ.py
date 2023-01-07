    # bin - в двоичную (из 10ной)
    # oct - в восьмиричную (из 10ной)
    # hex - с шестнадцатиричную (из 10ной)

        # 5.26949

# for n in range(1000):
#     num = bin(n)[2::]       # исходное число в 2сном представлении
#     if n % 2 == 0:
#         new_num = num + '00'
#     else:
#         new_num = num + '11'
#
#     r = int(new_num, 2)     # исходное число в 10чном представлении
#     if r < 94:
#         print(n)


        # 5.47209

# for n in range(1000):
#     binn = bin(n)[2::]
#     s = sum(map(int, binn))
#     if s%2 == 0:
#         temp = binn + '0'
#         new_num = '10' + temp[2::]
#     else:
#         temp = binn + '1'
#         new_num = '11' + temp[2::]
#
#     r = int(new_num, 2)
#     if r > 40:
#         print(n)
#         break


        # 5.47002

for n in range(1000):
    binn = bin(n)[2::]      # двоичная запись числа

    c1 = 0
    c0 = 0
    pos = 1

    for elem in binn:
        if elem ==  '1' and pos%2 == 0:
            c1 += 1
        if elem == '0' and pos%2 != 0:
            c0 += 1
        pos += 1
    r = abs(c0 - c1)
    if r == 4:
        print(n)
        break
