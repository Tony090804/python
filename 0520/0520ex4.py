'''
2023-05-06
장우혁
turtle 활용2-입력, 색 채우기
'''

import turtle
t=turtle.Turtle()
#t. color("yellow")
co=turtle.textinput("색상","색상입력(영어로 입력하시오)")
r=turtle.numinput("반지름","반지름입력(숫자로 입력하시오)")
t.color(co)

t.begin_fill()
t.circle(r)
t.end_fill()

input()