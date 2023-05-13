'''
2023-05-13
장우혁
#문제 정의
    숫자를 반복적으로 입력 받아서 합계가 1000이상이면 반복을 종료하고
    합계와 평균을 출력하시오.
#문제 분석
    변수-정수(num)합계,(sum),평균(avg),압력횟수(cnt) 
#알고리즘
    1.변수 선언
        sum=0;avg=0;cnt=0
    2.논리(반복 안에 선택 포함)
        (반복) while True: #무한 반복
            num에 정수 입력
            입력횟수 증가
            입력받은 수 합계
            (선택) if sum>=1000:
                break #반복 탈출
    3.평균 계산
    4.합계, 평균 출력
'''

sum=0;avg=0;cnt=0

while True: #무한 반복
    num=int(input("숫자 입력:"))
    sum=sum+num
    cnt=cnt+1
    if sum>=1000:
        break
print("합계:{},평균:{}.".format(sum,sum/cnt))