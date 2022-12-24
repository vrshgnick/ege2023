    # 1

p1,p2,q1,q2 = 17,46,22,57


P = [i/10 for i in range(p1*10, p2*10 + 1)]
Q = [i/10 for i in range(q1*10, q2*10 + 1)]

# print(P)
# print(Q)

A = set()
def sol(x,A):
    return (not (x in A)) <= (((x in P) and (x in Q)) <= (x in A))

for x in [i/10 for i in range(10*10,100*10 + 1)]:
    if not sol(x,A):
        A.add(x)
print(sorted(A))
