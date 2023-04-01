def divs(n):
    devis = set()
    for d in range(1,int(n**0.5) + 1):
        if n&d == 0:
            devis.add(d)
            devis.add(n//d)
    return sorted(devis)

delit = divs(51)
print(delit)
