sum = 0

n = int(input())

if n >= 1:
    for i in range(1,n+1):
        sum += i
else:
    for i in range(n,1+1):
        sum += i

print (sum)