            # еге решаем

print("x,y,z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x or y) <= (z == x)) == False:
                print(x,y,z)