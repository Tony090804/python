'''
2023-04-29
장우혁
input(), 형변환 함수:int(),float()
'''

name=input('이름 입력:')
print('이름은 {}이고 name변수의 자료형은 {}이다.'.format(name,type(name)))

age=input('나이 입력:')
print('나이는 {}이고 age변수의 자료형은 {}이다.'.format(age,type(age)))

age2=int(input('나이 입력2:'))
print('나이는 {}이고 age2변수의 자료형은 {}이다.'.format(age2,type(age2)))

pi=float(input('원주율 입력:'))
print('원주율은 {}이고, 변수 pi의 자료형은 {}이다.'.format(pi,type(pi)))