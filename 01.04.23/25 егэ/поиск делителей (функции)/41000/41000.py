def divs(n):
    devis = set()
    for d in range(1,int(n**0.5) + 1):
        if n%d == 0:
            devis.add(d)
            devis.add(n//d)
    return sorted(devis)

def M(N):
    delit = divs(N)                 # делители числа N
    if len(delit) > 2:
        summa = delit[-2] + delit[-3]
        return summa
    else:
        return 0
mnums = []
N = 11_000_001
while len(mnums) < 5:
    if 0<M(N)<10000:
        mnums.append((N,M(N)))
    N+=1
print(mnums)
