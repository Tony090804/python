'''
2023-05-06
장우혁
반복문 - while
'''
#1~10까지 출력하기

i=1 #반복 변수 초기화
while i<=10: #반복 조건
    print(i, end=" ") #i 출력
    i=i+1 #i 1씩 증가(증감식)
print()

#1~10까지 합계구하기
total=0 #합계
num=1 #반복 횟수
while num<=10:
    total=total+num #합계 구하기
    num=num+1 #num1증가하기
print('1~{}까지의 합계는 {}입니다.'.format(num-1,total))

