for k1 in range(61):
    for k2 in range(61):
        for k3 in range(61):
            s='0' + k1*'1' + k2*'2' + k3*'3' + '0'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print (k1 + k2 + k3 + 2)

# ответ - 38