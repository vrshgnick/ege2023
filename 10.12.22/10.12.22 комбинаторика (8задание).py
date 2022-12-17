                # как и через что можно

import itertools

# a = itertools.product()             #размещение (символы могут повторяться)

# b = itertools.permutations("год")        #перестановки (без повторений)

# b = list(itertools.permutations("год"))       #вывод в строку
# print (b)

# b = list(itertools.permutations("год"))
# for i in b:
#     print(''.join(i))


# for i in b:
#     print(i)

#PRIMER 1

# import itertools
#
# a = list(itertools.product('god', repeat=6))
#
# print (len(a))


#2

# import itertools
#
# a = list(itertools.product('god', repeat = 6))
#
# count = 0
# for i in a:
#     word = ''.join(i)
#     if word[0] == 'g' or word[0] == 'd':
#         count += 1
# print (len(i))


#3

# import itertools
# a = list(itertools.product('slon', repeat = 5))
#
# count = 0
# for i in a:
#     word = ''.join(i)
#     if word.count('s') == 1:
#         count += 1
# print (count)


#4

# import itertools
# a = list(itertools.product('ychenik', repeat = 5))
#
# count = 0
#
# for i in a:
#     word = ''.join(i)
#     if word[0] == 'y' and word[-1] == 'k':
#         count += 1
# print (count)


#5

# import itertools
# a = list(itertools.permutations('ольга'))
# count = 0
#
# for i in a:
#     word = ''.join(i)
#     if word[0] != 'ь' and ('оь' not in word) and ('аь' not in word):
#         count += 1
#
# print (count)


#6

# import itertools
# a = list(itertools.product('boris', repeat = 6))
#
# count = 0
# for i in a:
#     word = ''.join(i)
#     if (word.count('b') == 1 and word.count('r') == 1 and word.count('s') < 2):
#         count += 1
#
# print (count)


