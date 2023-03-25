f = open('1.txt')
n = f.readline()
c = 0
for i in n:
    if n.count('A') <= 3:
        c += 1
print(c)