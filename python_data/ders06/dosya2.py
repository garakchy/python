import turtle

turtle.screensize(800, 600)

def kareciz():
    turtle.fillcolor(R, G, B)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

kareciz()
turtle.mainloop() # ekranı açık tut