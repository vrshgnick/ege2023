f = open('2.txt')
n = f.readline()
c = 0
for i in n:
    if n.count('AB') == 21:
        c += 1
print(c)