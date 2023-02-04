# def isSimple(n):
#     for d in range(2, n//2 + 1):
#         if n % d == 0:
#             return False
#             break
#     return True
#
# def transform(s):
#     while '>0' in s or '>1' in s or '>2' in s:
#         if '>0' in s:
#             s = s.replace('>0','22>',1)
#         if '>1' in s:
#             s = s.replace('>1','2>',1)
#         if '>2' in s:
#             s = s.replace('>2','1>',1)
#     return s
#
# for n in range(100):
#     s = '>' + 15*'0' + n*'1' + 15*'2'
#     s = transform(s)
#     summa = sum([int(i) for i in s if i != '>'])
#     if isSimple(summa):
#         print(n)
#         break


    #12.33514

# def transform(s):
#     while '01' in s or '02' in s or '03' in s:
#         s = s.replace('01','30',1)
#         s = s.replace('02', '101', 1)
#         s = s.replace('03', '202', 1)
#     return s
#
# for x in range(50):
#     for y in range(50):
#         for z in range(50):
#             s = '0' + x*'1' + y*'2' + z*'3'
#             s = transform(s)
#             if s.count('1') == 15 and s.count('2') == 10\
#                 and s.count('3') == 60:
#                 print(x)

    #12.27013

# import itertools
#
#
# a = list(itertools.product('12',repeat = 14))
#
# maxsum = 0
# for i in a:
#     word =''.join(i)
#     if word.count('1') == 10 and word.count('2') == 4:
#         s = word
#         while '11' in s:
#             if '112' in s:
#                 s = s.replace('112','6',1)
#             else:
#                 s = s.replace('11','3',1)
#         summa = sum([int(i) for i in s])
#         if summa > maxsum:
#             maxsum = summa
# print(maxsum)


    #12.27383
