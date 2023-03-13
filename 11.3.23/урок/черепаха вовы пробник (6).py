from turtle import *
import turtle
speed(10)
left(90)
color('black','red')
m = 15
begin_fill()

for i in range(4):
    forward(10*m)
    right(270)
end_fill()
penup()

forward(3*m)
right(270)
forward(5*m)
right(90)

pendown()

for i in range(2):
    forward(10*m)
    right(270)
    forward(12*m)
    right(270)

end_fill()
penup()
speed(0)
for x in range(-12, 12):
    for y in range(-12, 12):
        setpos(x*m, y*m)
        dot(4, 'grey')
done()
#48 точек
