c = 0
n = 460000001
while c < 5:
    poln = n // 2
    cd = 0
    for j in range(2, poln + 1):
        if n % j == 0:
            cd += 1
            if cd == 5:
                print(n // j)
                c += 1
                break
    n += 1

# ответ - 41818182 261959 5 271 57500001