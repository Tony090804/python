'''
2023-05-13
장우혁
#문제 정의
    정수 2개와 연산자(+,-,*,/)1개를 입력 받아서 
    사칙연산을 수행하는 계산기 프로그램 만들기
#문제 분석
    변수-정수1(num1),정수2(num2),연산자(op)
#알고리즘
    1.변수 선언
    num1=int(input("숫자를 입력하시오.")),
    op=input("연산자를 입력하시오(+,-,*,/ 중 하나만 사용 가능)")
    num2=int(input("숫자를 입력하시오."))
    2.논리(선택논리)
'''

num1=int(input("숫자를 입력하시오:"))
op=(input("연산자를 입력하시오(+,-,*,/ 중 하나만 사용 가능):"))
num2=int(input("숫자를 입력하시오:"))

if op=="+":
    print("{}{}{}={}".format(num1,op,num2,num1+num2))
elif op=="-":
    print("{}{}{}={}".format(num1,op,num2,num1-num2))
elif op=="*":
    print("{}{}{}={}".format(num1,op,num2,num1*num2))
else:
    print("{}{}{}={}".format(num1,op,num2,num1/num2))