for n in range(10000, 1000, -1):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])
    r = str(s1 + s2 + s3 - max(s1,s2,s3) - min(s1,s2,s3)) + str(max(s1,s2,s3))
    if r == '1315':
        print(n)
        break

#ответ - 9676