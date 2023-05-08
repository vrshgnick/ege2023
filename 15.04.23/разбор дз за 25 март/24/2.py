f = open('2.txt')
n = f.readline()
c = 0
for i in range(len(n) - 1):
    if n[i] == n[i+1] and