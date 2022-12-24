    # 1

c = 0
for A in range (1,500):
    flag = True
    for x in range(1,500):
        for y in range (1,500):
            if not(((x<5) <= (x**2 < A)) and ((y**2) <= A) <= (y <= 5)):
                flag = False
                break
    if flag == True:
        c += 1
print(c)