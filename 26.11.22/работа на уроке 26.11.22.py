def isSimple(n):
    deliteli = 2
    for delit in range (2, n//2+1):
        if n % delit == 0:
            deliteli += 1
        break
    if deliteli != 2:
        return False
    else:
        return True

def simple(n):
    sum = 0
    num = 0
    i = 0
    while i <= n:
        if isSimple(num):
            sum += num
            i += 1
        num += 1
    return sum

print (simple(10))