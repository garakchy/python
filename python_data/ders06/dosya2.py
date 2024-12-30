import turtle
from random import randint as renk

turtle.screensize(800, 600)

R, G, B = renk(0, 255), renk(0, 255), renk(0, 255)

def kareciz():
    turtle.fillcolor(R, G, B)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def ucgen():
    turtle.fillcolor(R, G, B)
    turtle.pendown()
    turtle.begin_fill()

kareciz()
turtle.mainloop() # ekranı açık tut