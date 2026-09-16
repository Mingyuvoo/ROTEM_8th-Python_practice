#%%
from abc import ABC,abstractclassmethod

class Employee(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @ abstractclassmethod
    def pay(self):
        pass

    @ abstractclassmethod
    def data_print(self):
        pass

    def nameage_print(self):
        print(f"이름 : {self.name}, 나이 : {self.age}", end =' ')




class Temporary(Employee):
    def __init__(self,name,age,day,day_payment):
        super().__init__(name,age)
        self.day = day
        self.day_payment = day_payment

    def pay(self):
        return self.day * self.day_payment

    def data_print(self):
        super().nameage_print()
        print(f"월급 : {self.pay()}")
    
class Regular(Employee):
    def __init__(self,name,age,R_payment):
        super().__init__(name,age)
        self.R_payment = R_payment

    def pay(self):
        return self.R_payment

    def data_print(self):
        super().nameage_print()
        print(f"급여 :{self.pay()}")


    
class Salesman(Regular):
    def __init__(self,name,age,R_payment,sales,commision):
        super().__init__(name,age,R_payment)
        self.commision = commision
        self.sales = sales

    def pay(self):
        return self.R_payment + self.sales * self.commision
    
    def data_print(self):
        super().nameage_print()
        print(f"수령액 :{self.pay()}")

t = Temporary("홍길동", 25, 20, 15000)
r = Regular("한국인", 27, 3500000)
s = Salesman("손오공", 29, 1200000, 5000000,0.25)

t.data_print()
r.data_print()
s.data_print()
