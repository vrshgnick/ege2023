import datetime

now = datetime.datetime.now()

x = 300000000
divs = set()
for d in range(1,int(x**0.5) + 1):
    if x%d == 0:
        divs.add(d)
        divs.add(x//d)
print(sorted(divs))



end = datetime.datetime.now()
print(end - now)
