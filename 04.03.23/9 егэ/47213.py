f = open('47213.txt')
count = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    num = sum(a) - sum(set(a))
    if (len(set(a)) == 5) and ((sum(a)-2*num)/4 <= 2*num):
        count += 1
print(count)
