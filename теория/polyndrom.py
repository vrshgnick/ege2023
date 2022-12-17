# # a = 123
# # print((a//10)%10)
#
# num = input()
#
# mas1 = []
#
# for i in num:
#     mas1.append(i)
# print (mas1)
# mas2 = mas1
# mas2.reverse()
# print (mas2)
#
#
# for i in range(len(mas1)):
#     if mas1[i] == mas2[i]:
#         continue
#     else:
#         flag = false
#         break
# print(flag)




# flag = (True) только состояние, если цифры неверны, то флаг ставим в False

num = input()
flag = True
for i in range(len(num)//2):
    if num[i] == num[-(1+i)]:
        continue
    else:
        flag = False
        break
print(flag)


                        # #primer tcikla
#     num[0] == num[-1]
#     num[1] == num[-2]
#     num[2] == num[-3]
#     num[3] == num[-4]