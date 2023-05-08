f = open('6.txt')
a = [int(x) for x in f]
s = 0
c = 0
for i in range(len(a) - 1):
    if (abs(a[i])%10 == abs(a[i+1])%10 and (abs(a[i])%10)%2 != 0):
        c += 1
        s = max(s, abs(a[i])*abs(a[i+1]))
print(c,s)
