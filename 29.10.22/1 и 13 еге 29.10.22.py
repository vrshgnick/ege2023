import time

x = 1000

time.sleep(0.2)
print('У меня нет проблем')
time.sleep(0.3)
print('Кроме моей башки')
time.sleep(0.3)
print('1000-7 я умер прости')
time.sleep(0.2)

while x > 7:
     print(f"{x} - 7 = {x-7}")
     x -= 7
     time.sleep(0.01)

print('идиот')