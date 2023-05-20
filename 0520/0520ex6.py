import turtle

t=turtle.Turtle()
t.color("yellow")
turtle.bgcolor("skyblue")
t.speed(0)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.goto(0,100)
t.color("red")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(35,65)
t.pendown()
t.color("sky blue")
t.begin_fill()
for i in range(4):
    t.forward(30)
    t.left(90)
t.end_fill()

t.penup()
t.goto(35,0)
t.pendown()
t.color("brown")
t.begin_fill()
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-900,0)
t.pendown()
t.color("green")
t.begin_fill()
for i in range(2):
    t.forward(9000)
    t.right(90)
    t.forward(500)
    t.right(90)
t.end_fill()

input()