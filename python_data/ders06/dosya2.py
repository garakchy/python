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

    for kenar in range(3):
        turtle.forward(100)
        turtle.right(120)
    
    turtle.end_fill()
    turtle.penup()

def yazi():
    turtle.pendown()
    yaziFontu = ("Arial", 20, "bold")
    turtle.write(bilgi, font=yaziFontu)
    turtle.penup() 

def mesaj():
    bilgi = turtle.textinput("Mesaj", "Bir mesaj yazın")
    print(bilgi)
    if bilgi == "quit" : quit()
    else: yazi(bilgi)

def uygulama():
    # turtle.onscreenclick(fun, btn) : mouse tıklannmasıyla x, y koordinatları alınır
    # btn, üç özelliği var (1, 2, 3) : 1 = sol, 2 = orta, 3 = sağ
    turtle.onscreenclick(ucgen, btn=1)

    turtle.listen()

kareciz()
turtle.mainloop() # ekranı açık tut