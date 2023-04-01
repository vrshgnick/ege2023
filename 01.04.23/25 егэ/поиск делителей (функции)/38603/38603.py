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

mnums = []
N = 700_001
while len(mnums) < 5:
    if M(N)%10 == 8:
        mnums.append((N, M(N)))
    N += 1
print(mnums)
