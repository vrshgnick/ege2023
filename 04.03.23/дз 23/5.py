def f(x,y,cmd):
    if x == y:
        return 1
    if x > y:
        return 0
    print (f'команд = {cmd}')
    return f(x+1,y,cmd+1) + f(x*2,y,cmd+1)
print(f(1,15,0))
