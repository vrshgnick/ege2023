# БЕЗ ДОП УСЛОВИЙ
    #1
# def f(start,finish):
#     if start == finish:
#         return 1
#     if start > finish:
#         return 0
#     if start < finish:
#         return f(start + 1, finish) + f(start * 2, finish)
# print(f(2,22))

    #2
# def f(z,x):
#     if z == x:
#         return 1
#     if z < x:
#         return 0
#     if z > x:
#         return f(z - 2,x) + f(z - 5,x)
# print(f(23,2))

    #3
# def f(start,finish):
#     if start == finish:
#         return 1
#     if start > finish:
#         return 0
#     if start < finish:
#         return f(start + 1, finish) + f(start * 2,finish)+ f(start * 2 + 1,finish) + f(start * 10, finish)
# print(f(1,15))

    #4 7933
# def f(x,y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     if x < y:
#         return f(x+1,y) + f(x+2,y) + f(x+(x-1),y)
# print(f(2,9))

#C ОБЯЗАТЕЛЬНЫМИ УСЛОВИЯМИ
    #1 11358
# def f(x,y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     return f(x+1,y) + f(x+2,y) + f(x*2,y)
# print(f(3,10)*f(10,12))

    #2 18801
# def f(x,y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     return f(x+1,y) + f(x*3,y) + f(x+2,y)
# print(f(2,9)*f(9,11)*f(11,12))

    #3 47227
def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1,y) + f(x*2,y)
print(f(1,10)*f(10,16)*f(18,35))

