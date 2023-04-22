# -10; уменьшить кол-во камней в 3 раза(кол-во получ при делении округл до меньшего)(10 знак 3 = 3)
# например из кучи 25 можно сделать 15 или 8
# игра завершается когда в куче становиться более 10 каменей, в начале было >=11 камней
#
# в1 после неудачного хода пети(найдите максимальное)
from functools import lru_cache
def moves(h):
    a = []
    if h > 10:
        a.append(h-10)
    if h // 3 > 0:
        a.append((h//3))
    return a
@lru_cache()

def game(h):
    if h <= 10:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'
c = 0
for s in range(11,1000):
    if game(s) == 'B2':
        c += 1
print(c)
        # print(s,game(s))
