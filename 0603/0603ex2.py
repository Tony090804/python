'''
2023-06-03
장우혁
사용자 정의 함수 만들기
'''

def print_address(): #print_adress라는 함수 정의
    print("부산광역시")
    print("사상구 괘법동")
    print("신라대학교")
    
print_address()

print()

def person(): #person라는 함수 정의
    print("장우혁")
    print("15살")
    print("해운대중학교")
    
person()

print()

def print_address(name): #매개변수 있는 print_adress라는 함수 정의
    print("부산광역시")
    print("사상구 괘법동")
    print("신라대학교")
    print(name) #전달받은 name 값을 출력
    
print_address('장우혁')