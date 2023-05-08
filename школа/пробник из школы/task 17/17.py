count = m = 0
f = open('17')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] % 14 != 0:
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)

# ответ - 40436496 19999