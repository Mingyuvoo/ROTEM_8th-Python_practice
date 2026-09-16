#%%
# oop : 객체지향(중심)적인 프로그래밍 가능. 상속, 포함, 다형성 등의 기법 구사 가능
# class : 멤버변수(필드), 멤버 메소드로 구성
# 인스턴스에 의해 새로운 이름공간을 갖는다.

a = 2
print(a)

def func():
    print("ok")

class TestClass:    # 클래스의 헤더, 무조건 대문자로 시작

    aa = 1          # 멤버 변수(필드). 현재 클래스 내에서 전역

    def __init__(self): # 특별 메소드. Method의 첫 인자는 반드시 self
        print("생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당")

    def __del__(self):  # 특별 메소드
        print("소멸자 : 프로그램 종료시 자동 실행. 마무리 작업")

    def showMessage(self): # 일반 메소드
        name = "한국인"     # 지역변수 : showMessage에서만 유효
        print(name)
        print(self.aa)

print(TestClass)
print("클래스 멤버 a : ", TestClass.aa)
# TestClass.showMessage

# 클래스 생성자를 이용해 객체 생성 후 해당 객체의 주소를 객체변수에 치환
test = TestClass()      # 생성자 호출. instance를 함. -> object이 생성됨
print('클래스 맴버 a :',test.aa)
test.showMessage        # 자동으로 객체변수 test가 메소드의 인수로 담겨 호출됨
print()
test.showMessage()
print()

# Bound Method call
test. showMessage()     # 자동으로 객체변수 test가 메소드의 인수로 담겨 호출

# Undbound Method cll 
TestClass.showMessage(test)

print()
print(type("1"))
print(type(1.0))
print(type("ok"))
print(type(test))

print(id(test))
print(id(TestClass))
test2 = TestClass() #객체 한개 더 생성
print(id(test))
