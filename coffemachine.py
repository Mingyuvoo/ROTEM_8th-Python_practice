
# class CoinIn에 넣어야할 것들
# 커피 한잔의 가격보다 낮은 금액을 입력하는 경우 요금 부족 메시지
# 입력한 가격과 커피잔을 통해 최종 커피잔과 잔돈 출력
#%%
class CoinIn:
    def __init__(self):
        self.money = int(input("동전을 입력하세요 :"))
        self.num = int(input("몇 잔을 원하세요 :"))

    def calc_coin(self,money,num):
        coffee = 200
        self.money = money
        self.num = num
        total_price = coffee * self.num

        if self.money >= total_price:
            exchange = self.money - total_price    
            self.exchange = exchange     
            return self.num, self.exchange   
        
        else:
            print("다시 입력하세요")

        
        
# class Machine에 넣어야할 것들
# class CoinIn의 출력인 cupCount를 출력 --> 즉 최종 출력
# 최종 출력 형태

class Machine:
    def ShowData(self,num,exchange):
        self.num = num
        self.exchange = exchange
        print("출력형태 ---------")
        print(f"커피{self.num}잔과 잔돈{self.exchange}원")
        

insert = CoinIn()
result_num, result_price = insert.calc_coin(insert.money,insert.num)
Machine.ShowData(insert,result_num, result_price)



#%%
class Machine:
    def __init__(self):
        self.coin_input = CoinIn(self)

    def showData(self):
        coin = input('동전 입력')
        count = input('몇 잔 입력')
        self.coin_input.coin = int(coin)
        self.coin_input.calc(int(count))
        change = self.coin_input.change

        if (change >=0) :
            print("커피", count, "잔과 돈", change, "원")
        else:
            print("잔액이 부족합니다")

class CoinIn:
    def __init__(self, coin = 0, change = 0):
        self.price = 200
        self.coin = coin
        self.change = change

    def calc(self, cupCount):
        total = cupCount * self.price
        self.change = self.coin - total

machine = Machine()
machine.showData()

#%%
class CoinIn():
    def __init__(self):
        self.cupPrice = 200

    def calc(self,coin,cupCount):
        totoalPrice = self.cupPrice * cupCount

        if coin < totoalPrice:
            return None
        else:
            change = coin - totoalPrice
            return cupCount, change

class Machine():
    def __init__(self):
        self.coinIn = CoinIn()

    def showdata(self):
        coin = int(input("동전을 입력하세요"))
        cup = int(input("몇잔을 원하세요"))

        self.coinIn.calc(coin,cup)
        cupCount, change = self.coinIn.calc(coin, cup)

        if cupCount is None:
            print("요금이 부족")
        else:
            print(f"커피 {cupCount} 잔과 잔동{change}")

if __name__ == "__main__":
    machine = Machine()
    machine.showData()
    Machine().showdata()

#%%
var1 = [10,20,30]
var2 = [2,3]
print(var1 + var2)

var1.extend(var2)
print(var1)
