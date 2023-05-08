# import itertools
# product = itertools.product()         #размещение (символы могут повторяться) алфавит, кол-во повторений(длинна шифра)
# permutations = itertools.permutations("год")        #перестановки (без повторений) алфавит
import itertools

# 1

# import itertools
#
# a = list(itertools.product('БЕЛКА', repeat = 4))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if word.count('Б') == 1:
#         count += 1
# print (count)


# 2

# import itertools
#
# a = list(itertools.product('12345', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if word.count('1') == 3:
#         count += 1
# print(count)

# 3

# import itertools
#
# a = list(itertools.product('ГЕПАРД', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if word.count('Г') == 1 and word [0] != 'А' and word [-1] != 'Е':
#         count += 1
# print (count)


# 4

# import itertools
#
# a = list(itertools.product('ГОД', repeat = 6))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if word[0] == 'Г' and word [0] == 'Д':
#         count += 1
# print (count)


# 5

# import itertools
#
# a = list(itertools.product('ЗИМА', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if (word[0] == 'З' or word[0] == 'М') and (word[-1] == 'И' or word[-1] == 'А'):
#         count += 1
# print (count)

# 6

# import itertools
#
# a = list(itertools.product('ИОУ', repeat = 5))
#
# print (a[239])


# 17

# import itertools
#
# a = list(itertools.product('АОУ', repeat = 5))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     count += 1
#     if word [0] == 'У':
#         print(count)
#         break

# 8

# import itertools
#
# a = list(itertools.product('АГИЛМОРТ', repeat = 4))
#
# wordlist = []
# for i in a:
#     word =''.join(i)
#     wordlist.append(word)
# print(wordlist)
#
# for i in wordlist:
#     if i[0] == 'Г' and i[1] == 'О':
#         print(wordlist.index(i) + 1)
#         break

# 9

# import itertools
#
# a = list(itertools.permutations('ПОЛИНА'))
#
# soglsn = list(itertools.product('ПЛН', repeat = 2))
# glasn = list(itertools.product('ОИА', repeat = 2))
#
# soglsnlist = []
# glasnlist = []
#
# for i in soglsn:
#     word =''.join(i)
# for i in glasn:
#     glasnlist'',join(i)



# 10        найти кол-во 6 значных чисел, в которых встречаются лядом нечетные и четные числа

# import itertools
#
# nums = list(itertools.product('0123456789', repeat = 6))
#
# odds = list(itertools.product('13579', repeat = 2))
# evens = list(itertools.product('02468', repeat = 2))
#
# # print(nums)
# # print(odds)
# # print(evens)
#
# oddslist = []
# evenslist = []
#
# for i in odds:
#     oddslist.append(''.join(i))
# for i in evens:
#     evenslist.append(''.join(i))
#
# count = 0
# for i in nums:
#     num = ''.join(i)
#     if not (any([pair in num for pair in evenslist])) and not (any([pair in num for pair in oddslist])) and num[0] != '0':
#         count += 1
#         print(num)
# print(count)
