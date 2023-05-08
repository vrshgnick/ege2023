    #5
# c = 0
# for n in range(1000000):
#     binn = bin(n)[2::]
#     sumn = sum([int(i) for i in str(n)])
#     if sumn %  2 != 0:
#         binn = binn + '1'
#     else:
#         binn = binn + '0'
#     n = int(binn,2)
#     sumn = sum([int(i) for i in str(n)])
#     if sumn % 2 != 0:
#         binn = binn + '1'
#     else:
#         binn = binn + '0'
#     sumn = sum([int(i) for i in str(n)])
#     if sumn %  2 != 0:
#         binn = binn + '1'
#     else:
#         binn = binn + '0'
#     n = int(binn,2)
#     r = int(binn,2)
# if (r >= 123_456_789) and r <= (1_987_654_312)
#     c += 1
# print(r)
# print (c)

# 8
import itertools

a = list(itertools.product('01234567'), repeat=11)
odds = list(itertools.product('1357'), repeat=2)

for i in a:
    word =''.join(i)
    if (word[0] != = 0) and (word.count('1')  + word.count('3') + num.count('5') + num.count('17') == 3) and \
        not '13' in word and not '15' in word and not '17' in word and not '35' in word \
        and not '55' in word and not '75' in word and not '11' in word ...