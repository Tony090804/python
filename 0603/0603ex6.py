'''
2023-06-03
장우혁
삼각형 만들기
'''
import turtle
t=turtle.Turtle()
t.speed(0)
t.shape('turtle')
def n_poly(n,length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)
for i in range(18):
    t.left(20)
    n_poly(3,80)
input()