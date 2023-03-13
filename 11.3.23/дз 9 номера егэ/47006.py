f = open('47006.txt')
count = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    s1 = a[0]
    s2 = a[1]
    s3 = a[2]
    s4 = a[3]
    if s1 + s2 > s3 and s1 + s2 > s4 \
        and s1 + s3 > s2 and s1 + s3 > s4 \
        and s1 + s4 > s2 and s1 + s4 > s3 \
        and s2 + s3 > s1 and s2 + s3 > s4 \
        and s2 + s4 > s1 and s2 + s4 > s2:
        count += 1
print(count)
