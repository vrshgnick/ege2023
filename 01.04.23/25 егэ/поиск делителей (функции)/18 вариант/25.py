def divs(n):
    devis = set()
    for d in range(1,int(n**0.5) + 1):
        if n%d == 0:
            devis.add(d)
            devis.add(n//d)
    return sorted(devis)

def M(N):
    delit = divs(N)
    if len(delit) > 2:
        summa = delit[1] + delit[-2]
        return summa
    else:
        return 0

def IsSimple(n):
    for d in range(2,int(n**0.5) + 1):
        if n%d == 0:
            return False
            break
    return True

mnums = []
N = 650001
while len(mnums) < 6:
    delit = divs(N)
    if (not IsSimple(delit[-2])):
        mnums.append((N,delit[-2]))
    N += 1
print(mnums)
