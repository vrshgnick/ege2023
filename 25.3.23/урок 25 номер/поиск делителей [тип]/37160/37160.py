nums = []
n = 500001
while len(nums) < 5:
    for d in range(2, int(n**0.5) + 1):
        if (n%d == 0) and (d != 0) and ((d%10 == 8) or ((n//d)%10 == 8)):
            nums.append(n)
    n += 1
print(nums)

for i in nums:
    print(f'chislo = {i}')
    for d in range(2,int(i**0.5) + 1):
        if (i%d == 0) and (d%10 == 8 or (i//d)%10 == 8):
            print(d)
            print(i//d)
