#%%
# 추상 클래스(abstract class)
# 추상 메소드를 가진 클래스를 추상 클래스라고 하며
# 얘는 인스턴스 할 수 없다.(객체 생성 불가)
# 부모 클래스로만 사용됨
# 추상 클래스는 "직접 객체를 만들려고 존재하는 클래스가 아니라, 자식 클래스들이 반드시 지켜야 할 공통 규칙을 정하는 클래스"이다.
# 추상 클래스 = 지식 클래스에게 규칙을 강제(메서도 오버라이딩)하는 부모 클래스


from abc import *

class AbstractClass(metaclass = ABCMeta):

    #@abstractmethod

    def abcMethod(self):
        pass


    def normalMethod(self):
        print("추상 클래스 내의 일반 메소드 : 자식 클래스에서 오버라이딩 선택")

parent = AbstractClass()

class Child1(AbstractClass):
    name = "난 Child1"

    def abcMethod(self):
        print("부모가 가진 추상 메소드를 재정의 - 강요 당함")
# c1 = Child()
ch1 = Child1()
print("name :", ch1.name)
ch1.abcMethod()
ch1.normalMethod()
print()

class Child2(AbstractClass):
    def abcMethod(self):        # 오버라이딩 자의적 서낵함
        print("오버라이딩 함 : Child2에서 수행할 로직 작성")

    def show(self):
        print("Child2의 고유 메소드")

ch2 = Child2()
ch2.abcMethod()
ch2.normalMethod()
ch2.show()

print("-------- 다형성--------")
happy = ch1
print(id(ch1),' ', id(happy), ' ',id(Child1))
happy.abcMethod()

print()
happy = ch2
happy.abcMethod()
print(id(ch2),' ', id(happy), ' ', id(Child2))

