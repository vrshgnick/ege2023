from functools import lru_cache

def moves(h):
    a,b = h
    return (a+1,b), (a*4,b), (a,b+1), (a,b*4)

@lru_cache(None)

def game(h):
    a, b = h
    if a + b >= 61:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B2'

for s in range(1,58):
    h = 3,s
    if game(h) == 'P2':
        print('otevet:',s,'ne otvet:',h,game(h))

# ответ - 1214