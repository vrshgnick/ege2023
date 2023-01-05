#                         #1

# from turtle import *
# left(90)
# pensize(10)
# penup()
# forward(100)
# pendown()
# pencolor("red")
# begin_fill()
# circle(70,230)
# pensize(10)
# pencolor("red")
#
# pencolor("red",)
# forward(140)
# seth(40)
# forward(135)
# pencolor("red")
# right(5)
# circle(70,210)
# pencolor("black")
#
# seth(30)
# fillcolor("red")
# end_fill()
# seth(-90)
# pencolor("red")
# pensize(3)
# forward(50)
# pencolor("black")
#
#
# hideturtle()
# done()

                    #2
from turtle import *
bgcolor("black")
color("pink")
speed(11)
left(45)

for i in range(1000):
    circle(30)
    if i < 60:
        right(3)
        forward(5)
    if 60 < i < 100:
        forward(5)
    if i == 100:
        right(90)
    if 100 < i < 140:
        forward(5)
    if 140 < i < 200:
        right(3)
        forward(5)
    if i == 200:
        up()
        left(130)
        forward(200)
    if i == 201:
        write ("любимому Колe", False,
               align="center", font=("arial", 30, "normal"))


# import time
#
# x = 1000
#
# time.sleep(0.4)
# print('У меня нет проблем')
# time.sleep(0.4)
# print('Кроме моей башки')
# time.sleep(0.4)
# print('1000-7 я умер прости')
# time.sleep(0.4)
#
# while x > 7:
#      print(f"{x} - 7 = {x-7}")
#      x -= 7
#      time.sleep(0.09)
#
# print('пидорас')


# print('\n'.join(' '.join(*zip(*row)) for row in ([["*" if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8 else " " for col in range(7)] for row in range(6)])))
# print("\u2764\uFE0F")
