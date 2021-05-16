#예제1)리턴문도 없고, 인자도 없는 함수
def printhello():
    print("Hello,user")

printHello()


#예제2) 리턴문이 없는 함수
def printHi(name):
    print("Hi", name)

#printHi("강태영")
name = input()
printHi(name)

#예제3) 리턴문이 있는 함수
def printWelcome(user):
    word = "Welcome," + str(user)
    #str 괄호안에 뭐가 오든 문자열로 취급함
    return word #return 값이 하나인게 아니라 리턴 식이 하나여야함

user = int(input())
#int는 숫자형으로 받아주는 거
print(printwelcome(user))

#예제4) 세 개의 값을 동시에 리턴하는 함수
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x *30
    return y1, y2, y3

a, b, c - func_mul(10)
print(a, b, c)

#참고
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3] #리스트로 반환

    list = func_mul3(a, b, c)


#문자열 안에 우리가 원하는 값을 쉽게 삽입해보자
#파이썬에는 여러 문자열 포매팅 방법이 있습니다.
#여기서는 format 함수를 사용한 포매팅만 알고 넘어가보도록 하겠습니다
#더 자세한 포매팅 방법을 알고 싶다면 여기 참고 https://wikidocs.net/13

#문자열에 숫자를 바로 대입하기
print("저는 덕성 멋사 {}기 입니다.".format(9)) #tap누르면 자동으로 포맷써짐

#문자열에 문자열 입력받아 삽입하기
fruit = input("당신이 좋아하는 과일은")
print("내가 좋아하는 과일은 {}니다.".format(fruit))

#2개 이상의 값 넣기 (숫자는 인덱스, 문자는 이름으로 대입)
print("저는 {0}학번 {major}과 입니다.".format(18, major="컴퓨터공학"))
##포맷 괄호 안에 들어가는 건 0번 1번 순으로 가는 거라서
##알아서 자동으로 0번으로 들어가는 거고, major라고 정해둬서 뒤에 애를 넣는 거임

