def root(x):
    r = x**0.5
    nr = int(r)
    if r == nr:
        return True
    else:
        return False
print(root(16))
