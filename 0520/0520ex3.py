'''
2023-05-06
장우혁
turtle 모듈 활용
'''

import turtle
t=turtle.Turtle()
t.shape("arrow") #터트 모양
t.color("purple") #선의 색상
t.width(2) #선의 굵기

t.down() #펜 내리기
t.goto(100,0)#100,0으로 이동하면서 선 그리기

t.up() #펜 들기
t.goto(0,200)#0,200위치로 이동
t.down()
t.forward(100)

t.pencolor("blue")
t.goto(100,0)
t.up()
t.goto(0,0)
t.down()
t.goto(0,200)

input()