f = open('2.txt')
a = [int(x) for x in f]
maks = max(a)
s = 0
c = 0
for i in range(len(a) - 2):
    if ((a[i] % 10 == 0 and a[i+1]%10 != 0 and a[i+2]%10 != 0) or \
            (a[i] % 10 != 0 and a[i + 1] % 10 == 0 and a[i + 2] % 10 != 0) or \
            (a[i] % 10 != 0 and a[i + 1] % 10 != 0 and a[i + 2] % 10 == 0)) and (a[i] + a[i+1] + a[i+2] < maks):
        c += 1
        s = max(s,a[i] + a[i+1]+a[i+2])
print(c,s)
