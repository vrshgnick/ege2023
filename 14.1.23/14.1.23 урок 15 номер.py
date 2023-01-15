        # из домашки 15

    # B4

# def treug(n,m,k):
#     if (n < m + k) and (m < n + k) and (k < m + n):
#         return True
#     else:
#         return False

def treug(n,m,k):
    return (n < m + k) and (m < n + k) and (k < m + n)

for a in range(0,1000):
    flag = True
    for x in range(0,1000):
        if not(not(((treug(x,12,20) == (not (max(x,5) > 28)))) and treug(x,a,3))):
            flag = False
            break
    if flag == True:
        print(a)
