'''
2023-04-29
조건문 연습
#문제정의
    입력받은 정수가 짝수이면 "짝수"출력, 아니면 "홀수"출력 하는 프로그램
#문제 분석
    변수:정수(num)
#알고리즘
    1.변수 선언 
        num=int(input('정수를 입력하시오'))
    2.조건식
        if num%2==0:
'''

num=int(input('숫자 입력:')) #num변수에 정수 저장

if num%2==0: #조건문
    print("짝수") #조건이 참일때만 실행
else:
    print("홀수") #조건이 거짓일때만 실행
