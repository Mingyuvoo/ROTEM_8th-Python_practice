# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용)
# 포함 관계 : 다른 클래스(객체)를 마치 자신의 멤버처럼 선언하고 사용
#%%
from test24Handle import Handle

class Car:
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = Handle()

    def turnHandle(self,q):
        if q>0:
            self.turnShowMessage = self.handle.rightTurn(q)
        elif q<0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = "직진"

if __name__ == "__main__":
    tom = Car("미스터 톰")
    tom.turnHandle(10)
    print(tom.ownerName + "의 회전량은" + tom.turnShowMessage + " " + str(tom.handle.quantity))

    print()
    suji = Car("미스 수시")
    suji.turnHandle(-20)
    print(suji.ownerName + "의 회전량은" + suji.turnShowMessage + " " + str(suji.handle.quantity))

    suji.turnHandle(0)
    print(suji.ownerName + "의 회전량은" + suji.turnShowMessage + " " + str(suji.handle.quantity))
