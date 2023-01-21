import math  # 12.14229
# s = '9'*85
# while ('666' in s) or ('999' in s):
#     if ('666' in s):
#         s = s.replace('666','9',1)
#     else:
#         s = s.replace('999','6',1)
# print(s)

        # 12.11243

# s = '1' + '9'*98
#
# while('19' in s) or ('299' in s) or ('399' in s):
#     s = s.replace('19','2',1)
#     s = s.replace('299','3',1)
#     s = s.replace('3999','1',1)
# print(s)


        # 12.18820

# s = '9'*65
# while('999' in s) or ('222' in s):
#     if ('222' in s):
#         s = s.replace('222','9',1)
#     else:
#         s = s.replace('999','2',1)
#
# print(sum([int(i) for i in s]))


        # 12.demo
#простое ли число
# def isSimple(n):
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return False
#             break
#     return True
#
# for n in range(100):
#     s = '>' + '0' * 39 + '1' * n + '2' * 39
#     while('>1' in s) or ('>2' in s) or ('>0' in s):
#         if ('>1' in s):
#             s = s.replace('>1','22>',1)
#         if ('>2' in s):
#             s = s.replace('>2','2>',1)
#         if ('>0' in s):
#             s = s.replace('>0','1>',1)
#     s = s.replace('>','')
#     k = sum([int(i) for i in s])
#     if isSimple(k):
#         print(n)



            # 12.47009

for x in range(30):
    for y in range(30):
        for z in range(30):
            s = '0' + x*'1' + y*'2' + z*'3' + '0'
            while not '00' in s:
                if '01' in s:
                    s = s.replace('01','210',1)
                if '02' in s:
                    s = s.replace('02', '3101', 1)
                if '03' in s:
                    s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(2 + x + y + z)
                exit()
