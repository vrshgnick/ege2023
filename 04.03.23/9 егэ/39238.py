f = open('39238.txt')
count = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[2]**2 == a[0]**2 + a[1]**2:
        count += 1
print(count)
