f = open('24')
s = f.readline()
s = s.replace('CFE','x')
s = s.replace('FCE','X')
maxlen = 1
curlen = 1
for i in range(len(s) - 1):
    if s[i] == s[i+1]
