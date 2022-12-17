#pervya

# print("x,y,z,w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and not y) or (y == z) or not w) == False:
#                     print(x,y,z,w)

                    #ответ wzyx


#vtoraya

# print("x,y,z,w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) and (y <= w)) or (z == (x or y))) == False:
#                     print(x,y,z,w)

                    #ответ xwzy

#tretya

# print("x,y,z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if ((x == y) or ((y or z) <= x)) == False:
#                 print(x,y,z)


                    #ответ xzy

#chetvertya

print("x,y,z,w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not x or y or z)==(not y and z and w)) == True:
                    print(x,y,z,w)

                    #ответ1 yxzw
                    #ответ2 ywzx

#pyatya

# print("x,y,z,w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x <= z) or (not x and w)) == (w == z) == True:
#                     print (x,y,z,w)


# 1: wzyx
# 2: xwzy
# 3: xzy
# 4: yxzw or ywzx