            # 2 раздел 15 задания (отрезки)
            # длина отрезка всегда правая скобка минус левая


                 ## ДЛЯ ПОИСКА НАИМЕНЬШЕГО ##

    # 1

    # шаблонная часть

# p1,p2,q1,q2 = 4, 15, 12, 20
#
# P = [i/10 for i in range(p1*10,p2*10 + 1)]
# Q = [i/10 for i in range(q1*10,q2*10 + 1)]
#
#      # конец шаблонной части
#
# A = set()
#
# def sol(x,A):
#     return ((x in P) and (x in Q)) <= (x in A)
#
# for x in [i/10 for i in range(p1*10,q2*10 + 1)]:
#     if not sol(x,A):
#         A.add(x)
# print(sorted(A))
#
# #[12,15] == 15 - 12 = 3

    # 2

# p1,p2,q1,q2,r1,r2 = 10, 40, 5, 15, 35, 50
#
# P = [i/10 for i in range(p1*10,p2*10 + 1)]
# Q = [i/10 for i in range(q1*10,q2*10 + 1)]
# R = [i/10 for i in range(r1*10,r2*10 + 1)]
#
# A = set()
#
# def sol(x,A):
#     return ((x in A) or (x in P)) or ((x in Q) <= (x in R))
#
# for x in [i/10 for i in range((5-1)*10, (50-1)*10 +1)]:
#     if not sol (x,A):
#         A.add(x)
# print(sorted(A))
#
# # [5,10] 10-5=5(answer)

    # 3

# p1,p2,q1,q2 = 69, 91, 77, 114
#
# P = [i/10 for i in range(p1*10, p2*10 + 1)]
# Q = [i/10 for i in range(q1*10, q2*10 + 1)]
# A = set()
#
# def sol(x,A):
#     return (x in Q) <= (((x in P) == (x in Q))\
#         or ((not (x in P)) <= (x in A)))
#
# for x in [i/10 for i in range(68*10, 116*10 + 1)]:
#     if not sol(x,A):
#         A.add(x)
# print(sorted(A))
#
# print('сам итог, который нужен в ответе:', 114-91)
# print('114 - 91 = !23! ### для общего понимания(идет разрыв между порядками чисел)')


                    ## ДЛЯ ПОИСКА НАИБОЛЬШЕГО ##

    # 1

# p1,p2,q1,q2 = 5, 30, 14, 23
#
# P = [i/10 for i in range (p1*10, p2*10 + 1)]
# Q = [i/10 for i in range (q1*10, q2*10 + 1)]
#
# A = [i/10 for i in range(p1*10, p2*10 + 1)]
#
# def sol(x,A):
#     return ((x in P) == (x in Q)) <= (not (x in A))
#
# for x in [i/10 for i in range(4*10, 31* 10 + 1)]:
#     if not sol(x,A):
#         A.remove(x)
# print(sorted(A))

#[5,14) U (23, 30] - 2 скобки т.к есть разрыв
# 14 - 5 = 9
# 30 - 23 = 7
# тк просят большее,значит в ответ идет 9