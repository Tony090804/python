'''
2023-05-13
장우혁
#문제 정의
    정수를 입력 받아서 직각삼각형 별 출력하기
#문제 분석
    변수-정수(num),줄 반복(i),별 찍기 반복(j)
#알고리즘
    1.변수 선언
        num에 줄수 입력 받기
    2.논리(중첩반복)
        (줄 반복) for i in range(1,num+1):
            for j in range(1,i=1):
                print("*"*j)
'''

num=int(input('원하는 정수를 입력하시오:'))
for i in range(1,num+1): # 줄 반복 조건
    for j in range(1,i+1): # 별 찍기 반복 조건
        print("*",end=" ") #별 출력
    print()
        
'''
2023-05-13
장우혁
#문제 정의
#문제 분석
#알고리즘
    1.변수 선언
    2.논리
'''