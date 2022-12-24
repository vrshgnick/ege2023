import itertools
# a = itertools.product()             #размещение (символы могут повторяться)
# b = itertools.permutations("год")        #перестановки (без повторений)


#1

# import itertools
#
# a = list(itertools.product('aoy', repeat =5))
#
# print (a)


# #2

# import itertools
#
# a = list(itertools.product('aoy', repeat=5))
#
# wordlist = []
# for i in a:
#     word =''.join(i)
#     wordlist.append(word)
#
# print(wordlist.index('yayay') + 1)

#3

# import itertools
#
# a = list(itertools.product('akry', repeat = 5))
#
# wordlist = []
# for i in a:
#     wordlist.append(''.join(i))
#
# print (wordlist)
#
# for i in wordlist:
#     if i[0] == 'y':
#         print(wordlist.index(i) + 1)
#         break


#4

# import itertools
#
# a = list(itertools.product('bnrt', repeat = 6))
#
# print (a[249])


#5

# import itertools
#
# a = list(itertools.product('01234567', repeat = 5))
#
# count = 0
# for i in a:
#     num = ''.join(i)
#     if (num.count('6') == 1) and ('16'not in num)\
#             and ('61' not in num)\
#             and ('36' not in num)\
#             and ('63' not in num)\
#             and ('56' not in num)\
#             and ('65' not in num)\
#             and ('76' not in num)\
#             and ('67' not in num)\
#             and num[0] != '0':
#         print (num)
#         count += 1
#
# print (count)


