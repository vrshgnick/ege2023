from functools import lru_cache

def moves(h):           # перебор ходов
    return h+1, h+2, h*2

@lru_cache(None)

def game(h):
    if h >= 103:
        return 'W'
    if any(game(m) == 'W' for m in moves(h) if (m%3 != 0)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)if (m%3 != 0)):
        return "B1"

for s in range(1,102):
    if game(s) == 'B1':
        print(s,game(s))
