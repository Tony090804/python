'''
2023-06-03
장우혁
사전형자료(딕셔너리) 연습하기
'''
person={'name':'jwh','age':15,'school':'haeundae.ms'} #사전형 자료
print("이름:",(person['name'])) #name 키에 해당하는 갑 (value) 반환
print("나이:",(person['age'])) #age 키에 해당하는 갑 (value) 반환

person['hobby']="game" #사전형 자료에 데이터 추가

print("변경된 person:",person) 

del person['hobby'] #취미 데이터 삭제
print("변경된 person:",person) 

