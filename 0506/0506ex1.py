'''
2023-05-06
장우혁
시퀀스 자료형 연습(리스트 자료형)
'''
line_up=[] #원소가 없는 리스트 변수 만들기
line_up.append('꼬부기') #리스트에 원소 추가하기
print(line_up)

line_up.append('파르빗') #리스트에 마지막에 원소 추가하기
print(line_up)

line_up.insert(1,'탐리스') #인덱스1 위치에 원소 추가하기
print(line_up)

line_up.remove('꼬부기')
print(line_up)

num_list=[5,3,8,2,10] #리스트 변수
num_list.insert(2,4) #인덱스 2 자리에 원소 4 추가하기

print(num_list)

num_list.remove(10) #원소 10 삭제하기

print(num_list)

num_list.sort()
print(num_list)

