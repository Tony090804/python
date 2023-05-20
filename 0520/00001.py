'''
2023-05-06
장우혁
turtle 모듈 활용하기-그래픽 모듈
'''
import turtle #터틀 모듈을 프로그램에 추가
t=turtle.Turtle() #터틀 별명 만들기
t.shape("turtle") #커서 모양
turtle.bgcolor("black")

# 터틀 그래픽 초기 설정
window = turtle.Screen()
turtle.shape("turtle")
window.bgcolor("black")
window.title("별")
turtle.speed(0)
turtle.color("orange")

# 별 그리기 함수
def draw_star(size):
    turtle.penup()
    turtle.goto(20,35)
    turtle.pendown()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

t.pencolor("orange")
t.speed(0.1)
for i in range(3):
    t.forward(100)
    t.left(120)
t.up()
t.goto(50,-30)
t.down()
t.right(60)
t.backward(100)
t.right(120)
t.backward(100)
t.right(120)
t.backward(100)
t.right(150)
t.up()
t.backward(120)
t.right(90)
t.down()
t.circle(60)
t.penup()
t.goto(70,60)
draw_star(65)


input()