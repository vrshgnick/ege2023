f = open('24')
s = f.readline()
c, m = 1, 0
for i in range(1, len(s)):
    if s[i-1:i+1] not in ['da', 'ad']:
        c += 1
    else:
        c = 1
    m = max(m, c)
print(m)

# ответ - 2252