import turtle

sc = turtle.Screen()

t = turtle.Turtle()
# name = sc.textinput("b","a")
# t.write(name, font=("arial", 24), align="center")
t.color("red")
t.shape("turtle")
t.shapesize(3)
t.pensize(3)
t.pencolor("green")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()
for i in range(4):
    t.fd(200)
    t.right(90)

turtle.done()