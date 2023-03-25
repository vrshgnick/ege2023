from fnmatch import fnmatch
for i in range(4173,10**10,4173):
    if fnmatch(str(i),'1?7246*1'):
        print(i)
