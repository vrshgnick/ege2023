x = 52281337
divs = set()
for d in range(1,int(x**0.5) + 1):
    if x%d == 0:
        divs.add(d)
        divs.add(x//d)
print(sorted(divs))
