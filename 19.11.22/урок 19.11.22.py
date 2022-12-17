        Разбор задачи из учебника (прошлый урок)

import random

small = bool(random.randint(0,1))
green = bool(random.randint(0,1))
print(f"small = {small}, green = {green}")

if not small:
    if green:
        print("Goroh")
    else:
        print("Vishnya")
else:
        if green:
            print("Arbyz")
        else:
            print("Tikwa")



