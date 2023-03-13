f = open('17.txt')
a = [int(x) for x in f]
c = 0
m = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if ((a[i] + a[j]) % 80 == 0) and (a[i] % 50 == 0 or a[j] % 50 == 0):
            c += 1
            m = max(a[i] + a[j], m)
print(c,m)
