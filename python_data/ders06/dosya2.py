# mouse kontrol olayları ile şekil çizme ve mesaj yazma
import turtle
from random import randint as renk
from datetime import datetime 

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

def yazi(bilgi, x, y):
    turtle.color("#000")
    turtle.pendown()
    turtle.goto(x, y)
    yaziFontu = ("Arial", 20, "bold")
    turtle.write(bilgi, font=yaziFontu)
    turtle.penup() 

def mesaj(x, y):
    bilgi = turtle.textinput("Mesaj", "Bir mesaj yazın")
    print(bilgi)
    if bilgi == "quit" : quit()
    else: yazi(bilgi, x, y)

def uygulama():
    # turtle.onscreenclick(fun, btn) : mouse tıklannmasıyla x, y koordinatları alınır
    # btn, üç özelliği var (1, 2, 3) : 1 = sol, 2 = orta, 3 = sağ
    turtle.onscreenclick(ucgen, btn=1) # sol tıklama
    turtle.onscreenclick(kareciz, btn=3)   # sağ tıklama
    turtle.onscreenclick(mesaj, btn=2)  # orta tıklama

    turtle.listen() # klavye girişlerini dinle

uygulama()
kareciz()
turtle.mainloop() # ekranı açık tut