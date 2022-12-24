# import itertools
# a = itertools.product()             #размещение (символы могут повторяться)
# b = itertools.permutations()        #перестановки (без повторений)


    # 1

# 2 4 6 - chetnie
# 1 3 5 7 - nechetnie

# import itertools

# a = list(itertools.product('01234567', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if (word.count('4') == 2) and ('14' not in word)\
#         and ('41' not in word)\
#         and ('34' not in word)\
#         and ('43' not in word)\
#         and ('54' not in word)\
#         and ('45' not in word)\
#         and ('74' not in word)\
#         and ('47' not in word)\
#         and word[0] != '0':
#         count += 1
# print(count)


    # 2

# import itertools
#
# a = list(itertools.product('0123', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if (word.count('3') == 1) and ('03' not in word)\
#         and ('30' not in word)\
#         and word[0] != '0':
#         count += 1
# print(count)

    # 3

# import itertools
#
# a = list(itertools.product('КНОРСЯ', repeat = 6))
#
# wordlist = []
# count = 0
# for i in a:
#         wordlist.append(''.join(i))
# print (wordlist)
#
# for i in wordlist:
#     if (i.count('К') < 4) and (i.count('Я') == 2):
#         print (wordlist.index(i) + 1)
#         break

    # 4

# import itertools
#
# a = list(itertools.product('АЗЛОПЬ', repeat = 6))
#
# wordlist = []
# count = 0
# for i in a:
#         wordlist.append(''.join(i))
# print (wordlist)
#
# for i in wordlist:
#     if (i.count('З') < 3) and (i.count('А') == 1) and (i.count('Ь') < 2):
#         print (wordlist.index(i) + 1)
#         break


    # 5

import itertools

# a = list(itertools.product('АВИКЛ', repeat = 6))
#
# wordlist = []
# count = 0
# for i in a:
#         wordlist.append(''.join(i))
# print (wordlist)
#
# for i in wordlist:
#     if (i.count('А') < 3) and (i.count('В') == 2) and (i.count('И') < 1):
#         print (wordlist.index(i) + 1)
#         break


    # 6

# import itertools
#
# a = list(itertools.product('0123', repeat = 3))
#
# wordlist = []
# for i in a:
#     wordlist.append(''.join(i))
#
# for i in wordlist:
#     if (wordlist.index(0) > wordlist.index(1) and wordlist.index(0) > wordlist.index(2))\
#         and (wordlist.index(1) < wordlist.index(0) and wordlist.index(1) > wordlist.index(2))\
#         and (wordlist.index(2) < wordlist.index(0) and wordlist.index(1))\
#         and word[0] != '0':
# print (wordlist)


import itertools

a = list(itertools.product("0123", repeat = 3))

wordlist = []
count = 0

for i in a:
    wordlist.append("".join(i))

for i in wordlist:
    if int(i[0]) <= int(i[1]) <= int(i[2]) and i[0] != "0":
        count += 1
        print (i)
print(count)

