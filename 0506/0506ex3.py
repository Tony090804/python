'''
2023-05-06
장우혁
반복문 - for
'''
#시퀸스 반복문 정하기

for i in [1,2,3,4,5,6,7,8,9,10]: #반복 조건
    print(i, end=" ") #i출력
    
print() #줄 바꿈
for i in range(1,11): #반복 조건
    print(i, end=" ") #i 출력

#1~10까지 합계를 출력 하시오
sum=0

print()

for num in range(1,11):
    sum=sum+num
print("1~10까지의 합계는 {}이다.".format(sum))

#1~입력받은 숫자까지 합계 수하기
num1=int(input('숫자를 입력하시오:'))

sum1=0

print()

for num1 in range(1,num1+1): #반복 조건
    sum1=sum1+num1
print("1~{}까지의 합계는 {}이다.".format(num1,sum1))