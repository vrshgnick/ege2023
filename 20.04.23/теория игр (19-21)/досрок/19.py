from functools import lru_cache

def moves(h):           # перебор ходов
    return h+1, h+4, h*4

@lru_cache(None)

def game(h):
    if h >= 78:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return "B1"
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or  game(m) == 'P2' for m in moves(h)):
        return "B2"

for s in range(1,38):
    if game(s) == 'B1':
        print(s,game(s))
