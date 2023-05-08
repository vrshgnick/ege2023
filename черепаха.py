# import turtle
# turtle.shape("turtle") #    ПОЯЛЕНИЕ ЧЕРЕПАХИ НА ЭКРАНЕ
#
# import turtle
#
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.backward(100)
#
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.backward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.backward(100)
#######################################################

# import turtle
#
# square = turtle.Turtle()
# square.shape("turtle")
# square.color('red', 'green')
# square.begin_fill()
# for j in range(3):
#     square.left(20)
#     for i in range(4):
#         square.forward(100)
#         square.left(90)
#
# square.end_fill()
# turtle.exitonclick()

    ######################################
# import turtle
# turtle.shape("turtle")
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

    #6 10 егэ



# import turtle
# turtle.speed(1000)
# turtle.shape("turtle")
# for i in range(4):
#     turtle.forward(70)
#     turtle.right(90)
#     turtle.forward(80)
#     turtle.right(90)

#
#
# turtle = 0
#
# for x in range(1, 17):
#     for y in range(1, 8):
#         turtle += 1
#
# print(turtle, 'точки')

#####################################



# import turtle
# turtle.speed(100)

# turtle.title("Turtle Drawing")
# circle = turtle.Turtle()
# circle.shape("turtle")
# circle.pensize(5)
# circle.pencolor("cyan")


# # circle.dot(20)
# circle.penup()
# circle.goto(0, -100)
# circle.pendown()
# for i in range(100):w
#     circle.circle(100)
#     turtle.exitonclick()

###################################################################
# import turtle
# from math import tan, sqrt, pi
#
# def prepare(x, y, color):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.color(color)
#     turtle.begin_fill()
#
# def draw_polygon(num_sides, side_length):
#     angle = 360.0 / num_sides
#     for i in range(num_sides):
#         turtle.forward(side_length)
#         turtle.right(angle)
#     turtle.end_fill()
#
# def calc_s(num_sides, side_length):
#     return num_sides * side_length ** 2 / (4 * tan(pi/num_sides))
#
# def calc_side(square):
#     return sqrt(4 * square * tan(pi/num_sides) / num_sides)
#
# turtle.hideturtle()
# turtle.speed(10)
#
# colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'yellow', 'pink', 'brown']
# xcoords = [0, 150, -150, 150, -150, 270, -270, 270, -270]
# ycoords = [0, 150, -150, -150, 150, 270, -270, -270, 270]
#
# squares = []
# numsides = []
# for i in range(9):
#     num_sides = i + 3
#     square = round(calc_s(num_sides, 100), 2)
#     side_length = round(calc_side(10000), 3)
#     squares.append(square)
#     numsides.append(num_sides)
#     print("Углов:", num_sides, "была площадь:", square, "стала длина грани:", side_length,
#           "изменение в", round(side_length/100, 2), "раз")
#     prepare(xcoords[i], ycoords[i], colors[i])
#     draw_polygon(num_sides, side_length)
#
# turtle.exitonclick()
# print("Список количество углов:", numsides, end="")
# print("Список площади:", squares)


######################################
# import turtle
# turtle.speed(100)
#
# turtle.title("Turtle Circles")
# circ = turtle.Turtle()
# circ.pencolor("purple")
# circ.fillcolor("orange")
# circ.shape("circle")
# circ.pensize(5)
# circ.speed(10)
# circ.fd(150)
# circ.begin_fill()
# circ.circle(90)
# circ.end_fill()
#
# n = 10
# t = turtle.Turtle()
# while n <= 50:
#     t.circle(n)
#     n += 10
#
# turtle.exitonclick()