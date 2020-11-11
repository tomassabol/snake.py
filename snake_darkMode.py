import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.bgcolor("black")
window.setup(width=1400, height= 900)
pen.pencolor("white")
pen.speed(0)
pen.penup()
pen.goto(-400, 200)
pen.pendown()

a = 0
b = 0

while True:
    pen.forward(a)
    pen.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    pen.hideturtle()

pen.penup()
pen.goto(320, 0)
pen.pendown()

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    pen.pencolor(colours[i % 6])
    pen.width(int(i/250) + 1)
    pen.forward(i)
    pen.left(59)
pen.hideturtle()

window.mainloop()

