f = open('1(27524)')
maxims = []
maximum = 39.0
count = 0
for s in f:
    a = sorted([float(x) for x in s.split()])
    for degree in a:
        if degree < (maximum/2):
            count += 1
    # maxims.append(max(a))
# print(max(maxims))
print(count)
