f = open('zadanie24_1.txt')
# s = [x for x in f]  # для битых файлов (преобразование в 1 строку)
s = f.readline()

maxlen = 1
curlen = 1

for i in range(len(s) - 1):
    if s[i] == s[i+1] == 'C':
        curlen += 1
    else:
        maxlen = max(curlen,maxlen)
print(maxlen)

