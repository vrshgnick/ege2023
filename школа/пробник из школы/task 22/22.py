f = open('22')
a = [0]
for s in f:
    prcs, time, need = s.split()
    a.append(0)
    for i in need.split(';'):
        a[int(prcs)] = max(a[int(prcs)], a[int(i)])
    a[int(prcs)] += int(time)
print(max(a))

# ответ - 17
