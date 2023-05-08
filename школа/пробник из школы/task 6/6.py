import turtle
from turtle import *
left(90)
color('black','red')
speed(0)
m = 100

begin_fill()

for i in range(3):
    forward(6*m)
    right(120)

end_fill()

canvas = getcanvas()
c = 0

for x in range(-15*m,15*m,m):
    for y in range(-15*m,15*m,m):
        point = canvas.find_overlapping(x,y,x,y)
        if len(point) == 1 and point[0] == 5:
            c += 1
print(c)

done()

# ответ - 13