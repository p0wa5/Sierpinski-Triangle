from turtle import *

#Sierpinski Triangle in Python

right(30)
penup()
ht()
shape("triangle")
speed(90)


def sierpinski(size, order):
    if order == 0:
        stamp()
    else:
        for i in range(0,3):
            forward(size)
            sierpinski(size/2, order-1)
            backward(size)
            left(120)


sierpinski(140,5)
