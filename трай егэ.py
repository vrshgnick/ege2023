# Вариант № 12117752


        # Тип 2 № 15814

# print ("x y z w")
# for x in range(2):
#     for y in range (2):
#         for z in range (2):
#             for w in range(2):
#                 if ((x == (w or y)) or ((w <= z) and (y <= w))) == False:
#                     print (x,y,z,w)
# print ('ответ: yxzw')


            # Тип 8 № 18558

# import itertools
# a = itertools.product()             #размещение (символы могут повторяться)
# b = itertools.permutations()        #перестановки (без повторений)

# Иван составляет 5-буквенные коды из букв И, В, А, Н. Буквы в коде могут повторяться,
# использовать все буквы не обязательно, но букву И нужно использовать хотя бы один раз.
# Сколько различных кодов может составить Иван?

# import itertools
#
# a = list(itertools.product('ИВАН', repeat = 5))
# count = 0
#
# for i in a:
#     word =''.join(i)
#     if (word.count('И') >= 1):
#         count += 1
# print('ответ:', count)



        # Тип 14 № 13362

# x = 125 + 25**3 + 5**9
# s = ''
# while x != 0:
#     s += str(x % 5)
#     x //= 5
# s = s[::-1]
# print(s.count("0"))


        # Тип 15 № 13745

# for a in range(300, 1, -1):
#     k = 0
#     for x in range(0, 500):
#         for y in range(0, 500):
#             if ((x <= 9) <= (x * x <= a)) and ((y*y <= a) <= (y <= 9)):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break


        # Тип 5 № 18785
# for n in range(1, 100):
#     s = bin(n)[2:]  # перевод в двоичную систему
#     s = str(s)
#     if s[-1] == '0':
#         s = '1' + s + '0'
#     else:
#         s = '11' + s + '11'
#     r = int(s, 2)  # перевод в десятичную систему
#     if r > 52:
#         print(n)
#         break


###################################


# Вариант № 12117755

        # Тип 2 № 18578

            #   ((x ∧ ¬y) ∨ (w → z)) ≡ (z ≡ x)

# print ('x y z w')
#
# for x in range (2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and not y) or (w <= z)) == (z == x) == True:
#                     print (x,y,z,w)
# print ('ответ: z y w x')


    # Тип 8 № 18586

# import itertools
#
# a = list(itertools.product('СВЕТА', repeat = 5))
# count = 0
#
# for i in a:
#     word =''.join(i)
#     if (word.count('С') >= 1):
#         count += 1
# print(count)

    # Тип 14 № 16043

# x = 9**17 + 3**21 - 9
# s = ''
# while x != 0:
#     s += str(x % 3)
#     x //= 3
# s = s[::-1]
# print(s.count("2"))





    # Тип 12 № 9365

# print('all цикл')
#
# a = '8'*68
#
# while ('222' in a) or ('888' in a):
#     if '222' in a:
#         a = a.replace('222','8',1)              # вопрос: какого хуя тут единица,
#                                                 # да и после тоже, ведь без нее пара 228
#                                                 # с кайфом получается
#     else:
#         a = a.replace('888','2',1)
#         print(a)
#
# print('ну и какие нахуй',a,'?')



    # Тип 12 № 10415

# a = '8' * 99 + '1'
#
# while ('133' in a) or ('881' in a):
#     if '133' in a:
#         a = a.replace('133', '81',1)
#     else:
#         a = a.replace('881','13',1)
# print (a)


    # Тип 12 № 16443

# a = '1' * 84
#
# while ('11111' in a):
#     if ('222' in a):
#         a = a.replace('222','1',1)
#     else:
#         a = a.replace('111','2',1)
# print (a)


                    # 15 январский вариант

    # Тип 2 № 15787

# print ('x y z w')
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) and (y <= w)) or (z == (x or y))) == False:
#                     print (x,y,z,w)
#
# print ('xwzy')

    # Тип 8 № 13406

# import itertools
#
# a = itertools.product('ABCDXYZ', repeat = 4)
#
# for i in a:
#     word = ''.join(i)
#     if (word('X')[0])\
#         or (word('Y')[0])\
#         or (word('Z')[0]):
#         count += 1
# print (count)
#
# gg


    # Тип 12 № 16817


# a = '1' * 80
#
# while ('11111' in a):
#     if ('111' in a):
#         a = a.replace('111','2',1)
#     else:
#         a = a.replace('222','1',1)
#     print (a)


# for num in range(125256, 125331):
#     d = []
#     for j in range(1, int(num**0.5) + 1):
#         if num % j == 0:
#             if j % 2 == 0:
#                 d.append(j)
#             if num//j % 2 == 0 and num//j != j:
#                 d.append(num//j)
#     if len(d) == 6:
#         d.sort()
#         print(d[0], d[1], d[2], d[3], d[4], d[5])


# a = '1'*84
# while ('11111' in a):
#     if ('222' in a):
#         a = a.replace('222','1',1)
#     else:
#         a = a.replace('111','2',1)
# print (a)


# a = '8' * 99 + '1'
# while ('133' in a) or ('881' in a):
#     if ('133' in a):
#         a = a.replace('133','81',1)
#     else:
#         a = a.replace('881','13',1)
# print(a)

# a = '8' * 1000
#
# while ('999' in a ) or ('888' in a):
#     if ('888' in a):
#         a = a.replace('888','9',1)
#     else:
#         a = a.replace('999','8',1)
# print (a)

# a = '121'
#
# if a = reversed:
#     print('true')
# else:
#     print ('false')



# a = input('vvod: ')
# a1 = a[::-1]
# if (a1 in a):
#     a = a1
#     print('true')
# else:
#     print('false')


# import turtle
#
# polygon = turtle.Turtle()
# num_sides = 6
# side_length = 100
# angle = 360.0 / num_sides
#
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
#
# turtle.exitonclick()

# import turtle
#
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.backward(100)
#
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.backward(100)



    # new var   (https://inf-ege.sdamgia.ru/test?id=12328356)

    # 2
# print ('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x <= y) == (z <= w)) or (x and w) == False:
#                     print(x, y, z, w)

    # 6

# from turtle import *
# import turtle
# turtle.shape("turtle")
# left (90)
# color ('black','red')
# turtle.speed(0)
# m = 100
#
# begin_fill()
# for i in range(2):
#     forward(17*m)
#     right(90)
#     forward(4*m)
#     right(90)
# end_fill()
#
# canvas = getcanvas()
# count = 0
#
# for x in range(-10*m,10*m,m):
#     for y in range(-10*m,10*m,m):
#         point = canvas.find_overlapping(x,y,x,y)
#         if len(point) == 1:
#             count += 1
# print (count)
#
# done()


    # 8

# import itertools
#
# a = list(itertools.permutations('матвей'))
#
# count = 0
# for i in a:
#     word =''.join(i)
#     if (word[0] != 'й') and ('ае' not in word):
#         count += 1
# print(count)

    # 12

# a = 1000*'9'
#
# while ('999' in a) or ('888' in a):
#     if '888' in a:
#         a = a.replace('888','9',1)
#     else:
#         a = a.replace('999','8',1)
# print (a)


#Тип 2 № 15097
# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (x == z) or (x <= (y and z)) == False:
#                 print(x,y,z)

#Тип 5 № 17370
# a = []
# for x in range(100, 3001):
#     i = int(bin(x)[3:], 2)
#     if x - i not in a:
#         a.append(x-i)
# print(len(a))

#Тип 6 № 47306
# from turtle import *
# import turtle
# speed(0)
# color('black','red')
# left(90)
# m = 100
# begin_fill()
# for i in range(4):
#     forward(8*m)
#     right(90)
#     forward(8*m)
#     right(90)
# end_fill()
# canvas = getcanvas()
# count = 0
# for x in range(-100*m, 100*m, m):
#     for y in range(-100*m, 100*m, m):
#         point = canvas.find_overlapping(x,y,x,y)
#         if len(point) == 1 and point[0] == 5:
#             count += 1
# print(count)
# done()

#Тип 8 № 16385
# import itertools
#
# a = list(itertools.product('абвгд', repeat = 5))
# count = 0
# for i in a:
#     word =''.join(i)
#     if word[0] != 'а' and 'aa' not in word\
#         and 'бб' not in word\
#         and 'вв' not in word\
#         and 'гг' not in word\
#         and 'дд' not in word:
#         count += 1
# print(count)

#Тип 12 № 10290
# a = '1' + 80*'8'
# while '18' in a or '288' in a or '3888' in a:
#     if '18' in a:
#         a = a.replace('18','2',1)
#     else:
#         if '288' in a:
#             a = a.replace('288','3',1)
#         else:
#             a = a.replace('3888','1',1)
# print(a)


#Тип 23 № 15117
# def f(x,y):
#     if x == y:
#         return 1
#     if x > y or x==15:
#         return 0
#     if x < y:
#         return f(x + 1,y) + f(x + 2,y)
# print(f(3,9)*f(9,20))


# f = open(r'C:\Users\n-ver\Documents\17.txt')
# a = [int(i) for i in f]
# s = 0
# mx = 0
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] % 160 != a[j] % 160) and ((a[i] % 17 == 0) or (a[j] % 17 == 0)):
#             s += 1
#             mx = max(mx, a[i] + a[j])
# print(s, mx)

# x = 8**2020 + 4**2017 + 26 - 1
# s = ''
# while x != 0:
#     s += str(x % 2)
#     x //= 2
# s = s[::-1]
# print(s.count("1"))


# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     if n > 2:
#         return F(n-1) * n + F(n-2) * (n-1)
# print(F(5))











import turtle
from turtle import *

from turtle import *
speed(0)
left(90)
k = 50
for i in range(5):
    left(36)
    forward(4*k)
    left(36)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4, 'red')
done()
