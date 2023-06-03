import turtle

t=turtle.Turtle()
def draw_square(length,index):
    t.color(color[index])
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

color=['red','blue','green']
x=-200

for i in range(len(color)):
    t.penup()
    t.goto(x,0)
    t.pendown()
    draw_square(100,i)
    x+=200

input()
