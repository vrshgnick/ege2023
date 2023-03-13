def kon(num):
    return abs(num)%10
f = open('117.txt')
a = [int(x) for x in f]
c = 0
m3 = 0
m = 0
for i in a:
    if kon(i) == 3 and i > m3:
        m3 = i
for i in range(len(a) - 1):
    if ((kon(a[i]) == 3 and kon(a[i + 1]) != 3) or (kon(a[i]) != 3 and kon(a[i+1]) == 3)) \
        and (a[i]**2 + a[i+1]**2 >= m3**2):
        c += 1
        m = max(a[i]**2 + a[i+1]**2,m)
print(c,m)
