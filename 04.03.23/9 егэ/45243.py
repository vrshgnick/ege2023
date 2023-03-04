f = open(r'107_9.txt')
print(f)
count = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[4])**2 > (a[1]**2+ a[2]**2 + a[3]**2):
        count += 1
print(count)
