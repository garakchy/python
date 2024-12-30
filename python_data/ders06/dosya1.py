# gülen yüz çizen program
import turtle
import random

turtle.screensize(800, 600)
turtle.speed(0)

# rasgele renk seçimi
turtle.colormode(255)
R, G, B = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# en dış çember
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)
turtle.penup()
# gözler
turtle.begin_fill()
turtle.color("#ffff00") # sarı renk > #ffff00, yellow olarak da yazılabilir
# turtle.home() # başlangıç noktasına git
turtle.goto(25, 25)
turtle.pendown()
turtle.circle(50)
turtle.end_fill()
turtle.penup()
turtle.goto(-100, 25)
turtle.fillcolor("blue")
turtle.pendown()
turtle.circle(50)
turtle.end_fill()

# ağız
turtle.penup()
turtle.goto(-100, -75)
turtle.pendown()
turtle.begin_fill()
turtle.right(90)
turtle.circle(100, extent=180) # 180 derece yay çiz
turtle.end_fill()

turtle.mainloop()