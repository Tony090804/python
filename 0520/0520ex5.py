import turtle
t=turtle.Turtle()
co=turtle.textinput("색상","색상입력(영어로 입력하시오)")
ti=turtle.numinput("다각형","원하는 다각형의 각도 수입력(숫자로 입력하시오)")
t.color(co)
ti1=360//ti

t.begin_fill()
for i in range(int(ti)):
    t.forward(100)
    t.left(ti1)
t.end_fill()

input()

