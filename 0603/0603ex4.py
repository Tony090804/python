import turtle

t=turtle.Turtle()
def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

t.penup()
t.goto(-200,0)
t.pendown()
draw_square(100)

t.penup()
t.goto(0,0)
t.pendown()
draw_square(100)

t.penup()
t.goto(200,0)
t.pendown()
draw_square(100)

input()