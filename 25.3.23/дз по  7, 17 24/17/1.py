f = open('1.txt')
n = [int(x) for x in f]
c = 0
m = 0      #99991
for i in range(len(n) - 1):
    if (n[i] + n[i+1]) == max(n):
        c += 1
        m = max(n[i]**2 + n[i+1]**2,m)
print(c,m)
