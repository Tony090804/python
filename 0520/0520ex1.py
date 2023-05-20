'''
2023-05-06
장우혁
turtle 모듈 활용하기-그래픽 모듈
'''
import turtle #터틀 모듈을 프로그램에 추가
t=turtle.Turtle() #터틀 별명 만들기
t.shape("turtle") #커서 모양


t.forward(100) #앞으로 전진
t.left(90) #90도 회전
t.forward(50) #앞으로 전진
t.left(90) 
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)

# 반복문을 이용한 직사각형 그리기
for i in range(2):
    t.forward(100) #앞으로 전진
    t.left(90) #90도 회전
    t.forward(50) #앞으로 전진
    t.left(90) 

#반복문 이용한 정사각형 그리기

for i in range(4):
    t.forward(50)
    t.left(90)

#정삼각형 그리기(한변 100)

for i in range(3):
    t.forward(100)
    t.left(120)
    
t.circle(100)  
    
# 오각형 그리기

for  i in range(5):
    t.forward(100)
    t.left(72)
    
input()


