    # https://inf-ege.sdamgia.ru/problem?id=47313

import turtle
from turtle import *
turtle.speed(0)
color('black')
m = 100
left(90)
begin_fill()
#   чтобы найти число повторений цикла, нужно:
# 1) найти сумму поворотов (в градусах) за один проход цикла
# 2) разделить НОК числа 460 и найденной суммы на найденную сумму
#   полученное число - кол-во повторений

for i in range(10):
    forward(9*m)
    right(90)
    forward(2*m)
    right(90)
end_fill()

canvas = getcanvas()
count = 0
for x in range(-10*m, 10*m, m):
    for y in range(-10*m, 10*m, m):
        point = canvas.find_overlapping(x,y,x,y)    # точка лежащая на нашей фигуре
        if len(point) == 1:
            count += 1
print(count)
done()
exit()


    # 2 (из книги)

#   направо 300 постори 8(вперед 10 направо 120 вперед 10 направо 330)
#   границы не учитываем
import turtle
from turtle import *

turtle.speed(30)
color('black','red')
left(90)
right(300)
m = 100
count = 0

begin_fill()
for i in range(4):
    forward(10*m)
    right(120)
    forward(10*m)
    right(330)
end_fill()

canvas = getcanvas()

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        point = canvas.find_overlapping(x,y,x,y)
        if len(point) == 1 and point[0] == 5:
            count += 1
print(count)

done()
