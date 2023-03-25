def isSimple(n):
    for d in range(2,int(n**0.5) + 1):
        if n%d == 0:
            return False
            break
    return True
print(isSimple(52281337))