    # 12 егэ

    # 1

# a = '2'*2 + '1'*2023 + '2'*2
#
# while ('211' in a) or ('112' in a):
#     a = a.replace('11','1',1)
#     if '21' in a:
#         a = a.replace('21','12',1)
#     else:
#         a = a.replace('12','1',1)
# print(a)

    # 2

# a = '1'*2022
#
# while ('11' in a) or ('555' in a):
#     if '111' in a:
#         a = a.replace('11','555',1)
#     else:
#         a = a.replace('555','5',1)
# print(a)


    #3

# a = '1' + '5'*25
# while('15' in a) or ('1' in a):
#     if '15' in a:
#         a = a.replace('15','5551',1)
#     else:
#         if '1' in a:
#             a = a.replace('1','5',1)
# print(a.count('5'))

    #4

# a = '1'+ '57'*30
# while('157' in a) or ('1' in a):
#     if '157' in a:
#         a = a.replace('157','5757571',1)
#     else:
#         if '1' in a:
#             a = a.replace('1','57',1)
# print(a.count('7'))

    #5

# a = '0' + 12*'1' + 15*'2' + 17*'3'
# while ('01' in a) or ('02' in a) or ('03' in a):
#     a = a.replace('01','20',1)
#     a = a.replace('02','120',1)
#     a = a.replace('03','302',1)
# print(a.count('1'))

    #6

# a = '0' + 12*'1' + 15*'2' + 17*'3'
#
# while('01' in a) or ('02' in a) or ('03' in a):
#     a = a.replace('01','103',1)
#     a = a.replace('02','10',1)
#     a = a.replace('03','210',1)
# print(a.count('2'))

    #7

# a = 40*'7' + 40*'9' + 50*'4'
# while('49' in a) or ('97' in a) or ('47' in a):
#     if '47' in a:
#         a = a.replace('47','74',1)
#     if '97' in a:
#         a = a.replace('97','79',1)
#     if '49' in a:
#         a = a.replace('49','94',1)
# print(a[24], a[70], a[104])

    #8

# a = '>' + 26*'1' + 10*'2' + 14*'3'
#
# while ('>1' in a) or ('>2' in a) or ('>3' in a):
#     if '>1' in a:
#         a = a.replace('>1','22>',1)
#     if '>2' in a:
#         a = a.replace('>2','2>',1)
#     if '>3' in a:
#         a = a.replace('>3','1>',1)
# a = a.replace('>','')
# print(a)
# print(sum([int(i) for i in a]))

    # 8 егэ

# import itertools
#
# a = itertools.product('01234567', repeat = 5)
# count = 0
# for i in a:
#     word=''.join(i)
#     if (word.count('6') == 1) and ('16' not in word)\
#         and ('61' not in word)\
#         and ('36' not in word)\
#         and ('63' not in word)\
#         and ('56' not in word)\
#         and ('65' not in word)\
#         and ('76' not in word)\
#         and ('67' not in word)\
#         and word[0] != '0':
#         count += 1
# print(count)


