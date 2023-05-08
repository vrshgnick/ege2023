f = open('9.txt')

c = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    for i in range(len(a) - 1):
        if (a) / (max(a) % 2) < max(a):
            c += 1
print(c)

#ответ - 601