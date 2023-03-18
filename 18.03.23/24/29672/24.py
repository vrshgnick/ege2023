f = open('inf_22_10_20_24.txt')
n = f.readlines()
count = 0
for s in n:
    if s.count('E') > s.count('A'):
        count += 1
print(count)