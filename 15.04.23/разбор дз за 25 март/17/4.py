f = open('4.txt')
a = [int(x) for x in f]
c = 0
m = 0
for i in range(len(a) - 1):
    if (a[i] % 3 == 0) and (a[i+1] % 3 == 0):
        c += 1
        m = max(a[i] + a[i+1],m)
print(c,m)
