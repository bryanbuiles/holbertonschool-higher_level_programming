#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import turtle

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(
        90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]
    """ poniendo titulos """
    turtle.penup()
    turtle.setposition(0, 325)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.write('Rectangles!', font=style, align='center')
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.write('Squares!', font=style, align='center')
    turtle.hideturtle()

    """ rectangle section """
    count = -2
    flag = 1
    for i in range(len(list_rectangles)):
        squareb = turtle.Turtle()
        if i == 1:
            count = 0
        if i == 2 or i == 0:
            flag = 0
        else:
            flag = 1
        squareb.pensize(2)
        squareb.penup()
        squareb.setpos((150 * count) + (-75 * flag), 100)
        squareb.pendown()
        squareb.forward(150)
        squareb.write("x")
        squareb.penup()
        squareb.left(180)
        squareb.forward(150)
        squareb.pendown()
        squareb.right(90)
        squareb.forward(150)
        squareb.write("y")
        squareb.penup()
        squareb.left(180)
        squareb.forward(150)
        squareb.pendown()
        squareb.pensize(0)
        # set the position
        squareb.penup()
        squareb.setpos((150 * count) + (-75 * flag) + list_rectangles[i].x,
                       100 + list_rectangles[i].y)
        squareb.pendown()
        # dibujando el cuadro
        squareb.begin_fill()
        if i == 1:
            squareb.color("#4044B7")
        elif i == 0:
            squareb.color("#2C8A87")
        else:
            squareb.color("#F249B4")
        squareb.left(90)
        squareb.forward(list_rectangles[i].width)
        squareb.left(90)
        squareb.forward(list_rectangles[i].height)
        squareb.left(90)
        squareb.forward(list_rectangles[i].width)
        squareb.left(90)
        squareb.forward(list_rectangles[i].height)
        squareb.end_fill()
        count += 1

        """ square section """
    count = -2
    flag = 1
    for j in range(len(list_squares)):
        squareb = turtle.Turtle()
        if j == 1:
            count = 0
        if j == 2 or j == 0:
            flag = 0
        else:
            flag = 1
        squareb.pensize(2)
        squareb.penup()
        squareb.setpos((150 * count) + (-75 * flag), -250)
        squareb.pendown()
        squareb.forward(150)
        squareb.write("x")
        squareb.penup()
        squareb.left(180)
        squareb.forward(150)
        squareb.pendown()
        squareb.right(90)
        squareb.forward(150)
        squareb.write("y")
        squareb.penup()
        squareb.left(180)
        squareb.forward(150)
        squareb.pendown()
        # set the position
        squareb.penup()
        squareb.setpos((150 * count) + (-75 * flag) + list_squares[j].x,
                       -250 + list_squares[j].y)
        squareb.pendown()
        # dibujando el cuadro
        squareb.pensize(0)
        squareb.begin_fill()
        if j == 1:
            squareb.color("#0F7724")
        elif j == 0:
            squareb.color("#F26A49")
        else:
            squareb.color("#DCDC32")
        squareb.left(90)
        squareb.forward(list_squares[j].width)
        squareb.left(90)
        squareb.forward(list_squares[j].height)
        squareb.left(90)
        squareb.forward(list_squares[j].width)
        squareb.left(90)
        squareb.forward(list_squares[j].height)
        squareb.end_fill()
        count += 1
    turtle.done()
