f = open('4')
count = 0
for s in f:
    a = [float(x) for x in s.split()]
    for i in range(len(a) - 1):
        if a[i+1] - a[i] >= 2:
            count += 1
print(count)
