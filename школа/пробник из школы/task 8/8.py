import itertools

a = itertools.product('ivan', repeat = 5)

c = 0

for i in a:
    word =''.join(i)
    if word.count('i') >= 1:
        c += 1
print(c)