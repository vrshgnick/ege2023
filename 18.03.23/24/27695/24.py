f = open('zadanie24_2.txt')
s = f.readline()
maxlen = 1
curlen = 1
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        curlen += 1
    else:
        maxlen = max(maxlen,curlen)
        curlen = 1
print(maxlen)
