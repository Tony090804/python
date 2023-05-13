'''
2023-05-13
장우혁
#문제 정의
    출력을 원하는 단을 입력받아서 구구단 출력하기
#문제 분석
    변수-단(dan),반복회수(i)
#알고리즘
    1.변수 선언
        dan=input:('원하는 수를 입력하시오:'),i=1
    2.논리(반복-while)
        (반복조건) while i=<9:
        구구단 출력
'''

dan=int(input('원하는 수를 입력하시오:'))
i=1 #반복 변수 초기화
print("##{}단##".format(dan))
while i<=9: #반복 조건
    print("{}*{}={}".format(dan,i,dan*i)) #구구단
    i=i+1 #i 1증가
    
#for
dan=int(input('원하는 수를 입력하시오:'))
i=1 #반복 변수 초기화
print("##{}단##".format(dan))
for i in range(1,10): #반복 조건
    print("{}*{}={}".format(dan,i,dan*i)) #구구단
