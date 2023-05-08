f = open('1.txt')
s = f.readline()

curlen = 1
maxlen = 1
cntA = 0
for i in s:
    curlen += 1
    if i == 'A':
        cntA += 1
    if cntA == 4:
        maxlen = max(curlen,maxlen)
        curlen = 0
        break
print(maxlen)


# понедельник : до 3 школа, 5-6 репет
# вторник: до 3 школа, 3.30-6 репет
# среда: до 3 школа,3.30-6 репет
# четверг: до 3 школа, 4-5 репет
# пятница: до 3 школа