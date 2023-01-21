        # 5.2

# for n in range(150):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = n2 + '0'
#     else:
#         n2 = n2 + '1'
#     if n2.count('1') % 3 == 0:
#         n2 = '11' + n2[2:]
#     else:
#         n2 = '10' + n2[2:]
#     r = int(n2,2)
#     if r <= 37:
#         print(n)
# = 25

        # 5.3

# for n in range(1000):
#     n2 = bin(n)[2:]
#     if len(n2) % 2 == 0:
#         n2 = n2[:(len(n2)//2)] + '1' + n2[(len(n2)//2):]
#     r = int(n2,2)
#     if r >= 26:
#         print(n)
#         break
# = 12
###################
# s = '1010'
# s1 = len(s)
# print (list(s))
# s = s[2:]
# s_new = s + '1' + s
# print (s_new)
###################

        # 5.12

# for n in range(100,1000):
#     n = str(n)
#     n1 = int(n[0]) ** 2 + int(n[1]) ** 2
#     n2 = int(n[1]) ** 2 + int(n[2]) ** 2
#     r = int(str(max(n1,n2)) + str(min(n1,n2)))
#     if r == 9752:
#         print(n)