# 1 куча
# +1  *2 *3
# условие победы - 36 <= s <= 60
# игра завершается в тот момент, когда кол-во камней в куче
# становится не менее 36, если при этом в куче оказалось более 60 камней,
# то победителем считается игрок, сделавший последний ход, в противном случае
# победителем становится противник
# найдите минимальное s при любом в1 при любой игре пети

from functools import lru_cache
def moves(h):
    return h+1,h*2,h*3
@lru_cache(None)
def game(h):
    if 36<=h<=60:
        return 'W'
    if h > 60:
        return 'P1'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'

for s in range(1,100):
    if game(s) == 'B1':
        print(s,game(s))
