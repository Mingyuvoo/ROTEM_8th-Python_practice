# 상속
#%%
class Person:                                       # 용도 : 부모 클래스로 사용 
    say = "난 사람입니다"                            # 접근권한 : public
    age = "20"                                      # 전역변수

    __msg = "good : private 멤버 - 현재 클래스에서만 유효" # __ 붙이면 현재 클래스에서만 사용가능 다른 클래스에서는 못불러옴

    def __init__(self,age):
        print("Person 생성자")
        self.age = age

    def printInfo(self):       # 접근권한 
        print(f'나이 : {self.age}, 이야기 : {self.say}')

    def helloMethod(self):
        print("안녕")
        print("hello :", self.say, self.age, self.__msg)

print(Person.say, Person.age)                       # 원형 클래스로 멤버 호출(비권장)
Person("20").printInfo()        
p1 = Person("25")                                   # 원형 클래스로 멤버 호출(권장)
p1.printInfo()
p1.helloMethod()

print()

class Employee(Person):
    subject = "근로자"
    say = "일하는 동물"                              # hiding(shadowing)
    def __init__(self):
        print("Employee 생성자")

    def printInfo(self):                            # 메소드 오버라이딩(override)
        print("Employee 클래스의 printInfo 호출됨")

    def ePrintInfo(self):
        print(self.subject, self.say, self.age)
        # print(self.__msg)                         # 부모 클래스의 private 멤버 호출시 에러 : private이니
        self.helloMethod()                          
        self.printInfo()                            # 현재 클래스에서 먼저 검색 후 없으면 부모 메소드 호출
        super().printInfo()                         # 현재 클래스가 아니라 바로 부모 메소드 호출
        print(self.say, super().say)

emp = Employee()
print(emp.subject, emp.age, emp.say)                # say가 부모에도 있고 자식 클래스에도 있는데 두군데 같은 변수가 있다면 자식에 있는 지역변수를 우선시함
emp.printInfo()
emp.ePrintInfo()

print("----" * 5)
class Worker(Person):
    # def __init__(self,age):
    #     pass                                      자식이 pass면 부모로 올라가서 수행함
    def __init__(self,age):
        print("Worker 생성자")
        super().__init__(age)                       # 부모 클래스의 생성자 호출

    def wPrintInfo(self):
        print("Worker - wPrintInfo() 처리")
        self.printInfo()
        super().printInfo()


wor = Worker("30")
print(wor.say, wor.age)
wor.wPrintInfo()

print("----" * 5)
class Programmer(Worker):
    def __init__(self,age):
        print("Programmer 생성자")
        #super().__init__(age)                   # Bound method call
        Worker.__init__(self,age)               # unBound method call

    def pPrintInfo(self):
        print("Programmer - pPrintInfo() 처리함 ")

    def wPrintInfo(self):
        print("Programmer 클래스에서 오버라이딩")


pro = Programmer(35)
print(pro.say, pro.age)
pro.pPrintInfo()
pro.wPrintInfo()

print(" 클래스 타입 확인 -----------")
a = 3; print(type(a))           # <class 'int'> : Maker가 만든 기본 타입
print(type(pro))                # <class '__main__.Programmer'>
print(type(wor))                # <class '__main__.Worker'>

print(Person.__bases__)         # (<class 'object'>,)
print(Employee.__bases__)       # (<class '__main__.Person'>,)
print(Worker.__bases__)         # (<class '__main__.Person'>,)
print(Programmer.__bases__)     # (<class '__main__.Worker'>,)


