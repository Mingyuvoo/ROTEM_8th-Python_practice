# 어딘가에서 필요한 부품으로 핸들 클래스 작성
class Handle:
    quantity = 0        # 핸들 회전량

    def leftTurn(self, quantity): # 메소드
        self.quantity = quantity
        return "좌회전"
    def rightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"
    