    # https://inf-ege.sdamgia.ru/problem?id=47313 (Тип 6 № 47313)
# Повтори 10 [Вперёд 9 Направо 90 Вперёд 2 Направо 90]
# Определите количество точек с целочисленными координатами,
# лежащих внутри или на границе области, которую ограничивает заданная алгоритмом линия

    # 1) вдоль какой оси направлена голова чеперахи (ось абцисс - ось Х,
    #                                                ось ординат - ось У)
    # 2) правильно отрисовываем фигуру (чтобы пришла на изначальную точку для закрытия фигуры)
    # 3) написать алгоритм поиска точек (черзе find_overlapping())
    # 4) считаем ли мы точки на границе? изменяем в зависимости от этого наше условие в алгоритме поиска точек

# from turtle import *
# import turtle
#
# color('black','red')
# left(90)
# turtle.speed(0)
# m = 100     #масштаб
#
# begin_fill()
# for i in range(2):
#     forward(9*m)
#     right(90)
#     forward(2*m)
#     right(90)
# end_fill()
#
# canvas = getcanvas()    #создаем холст (рабочую область)
# count = 0
#
# for x in range(-10*m,10*m,m):
#     for y in range(-10*m,10*m,m):
#         #ищем точки
#         point = canvas.find_overlapping(x,y,x,y)
#         if len(point) >= 1:
#             count += 1
# print(count)
#
# done()


    # 2 из книги (есть в дс-е)

# from turtle import *
# import turtle
#
# left (90)
# color ('black','red')
# turtle.speed(0)
# m = 100
#
# begin_fill()
# right(180)
# forward(2*m)
# right(90)
# forward(30*m)
# right(90)
# forward(2*m)
# right(30)
# for i in range(6):
#     forward(5*m)
#     right(120)
#     forward(5*m)
#     right(240)
# end_fill()
#
#
# canvas = getcanvas()
# count = 0
#
# for x in range(-35*m,35*m,m):
#     for y in range(-35*m,35*m,m):
#         point = canvas.find_overlapping(x,y,x,y)
#         # если не учитываем точки на линии, то пишем if len(point) == 1 and point[0] == 5:
#         # иначе пишем if len(point) >= 1:
#         if len(point) == 1 and point[0] == 5:
#             count += 1
# print (count)
#
# done()

    # 3

# from turtle import *
# import turtle
# turtle.shape("turtle")
# left (90)
# color ('black','red')
# turtle.speed(0)
# m = 100
#
# begin_fill()
# for i in range(3):
#     forward(123*m)
#     right(120)
# end_fill()
#
# canvas = getcanvas()
# count = 0
#
# for x in range(-150*m,150*m,m):
#     for y in range(-150*m,150*m,m):
#         point = canvas.find_overlapping(x,y,x,y)
#         if len(point) == 1 and point[0] == 5:
#             count += 1
# print(count)
# done()

    # 4
# from turtle import *
# import turtle
# turtle.shape("turtle")
# left (90)
# color ('black','red')
# turtle.speed(0)
# m = 100
# begin_fill()
#
# right(60)
# for i in range(3):
#     forward(10*m)
#     right(120)
#     forward(5*m)
#     right(240)
# right(120)
# forward(3*m)
# right(90)
# forward((15*(3**0.5))*m)
# right(90)
# forward(3*m)
#
# end_fill()
#
# canvas = getcanvas()
# count = 0
#
# for x in range(-150*m,150*m,m):
#     for y in range(-150*m,150*m,m):
#         point = canvas.find_overlapping(x,y,x,y)
#         if len(point) == 1 and point[0] == 5:
#             count += 1
# print(count)
# done()


    # 5

from turtle import *
import turtle
turtle.shape("turtle")
left (90)
color ('black','red')
turtle.speed(0)
m = 100
# kvadrat = 64
# triug = 30

begin_fill()
for i in range(4):
    forward(9*m)
    right(90)
for i in range(3):
    forward(9*m)
    right(120)
end_fill()

canvas = getcanvas()
count = 0
for x in range(-10*m,10*m,m):
    for y in range(-10*m,10*m,m):
        point = canvas.find_overlapping(x,y,x,y)
        if len(point) == 1 and point[0] == 5:
            count += 1
print (count)
done()
