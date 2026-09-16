#%%
class ElecProduct:
    volume = 0

    def volumControl(self,volume):
        self.volume = volume
        pass


class ElecTv(ElecProduct):
    def __init__(self):
        print("TV는 삼성 GOAT")

    def volumControl(self, volume):
        self.volume = volume
        print(f"TV 볼륨을 {self.volume} 올렸습니다")


class ElecRadio(ElecProduct):
    def __init__(self):
        print("라디오는 LG GOAT")

    def volumControl(self, volume):
        self.volume = volume
        print(f"라디도 볼륨을 {self.volume} 올렸습니다")


e1 = ElecTv()
e2 = ElecRadio()
e1.volumControl(5)
e2.volumControl(7)

#%%
class ElecProduct:
    def volumControl(self):
        self.volume = int(input("볼륨 입력 : "))


class ElecTv(ElecProduct):
    def __init__(self):
        print("TV는 삼성 GOAT")

    def volumControl(self):
        super().volumControl()
        print(f"TV 볼륨을 {self.volume} 올렸습니다")


class ElecRadio(ElecProduct):
    def __init__(self):
        print("라디오는 LG GOAT")
    def volumControl(self):
        super().volumControl()
        print(f"라디도 볼륨을 {self.volume} 올렸습니다")

e1 = ElecTv()
e1.volumControl()

e2 = ElecRadio()
e2.volumControl()

#%%
class ElecProduct:
    volume = 0

    def volumControl(self,volume):
        self.volume = volume
        print(f"볼륨 {self.volume} 올렸습니다")


class ElecTv(ElecProduct):
    def __init__(self):
        print("TV는 삼성 GOAT")


class ElecRadio(ElecProduct):
    def __init__(self):
        print("라디오는 LG GOAT")

e1 = ElecTv()
e2 = ElecRadio()

volume1 = int(input("볼륨을 몇 올릴려"))
e1.volumControl(volume1)

volume2 = int(input("볼륨을 몇 올릴려"))
e2.volumControl(volume2)

#%%
class Animal:               # TOP Parent
    def __init__(self):
        print("동물입니다.")

    def move(self):
        print(f"{self.name} 사족보행 하는 중")

class Dog(Animal):                  # Middle Parent_1
    name = "개"
    def move(self):
        super().move()

class Cat(Animal):                  # Middle Parent_2
    name = "고양이"
    def move(self):
        super().move()

class Wolf(Dog,Cat):                 # Child_1
    def __init__(self):
        pass

class Fox(Cat,Dog):                  # Child_2
    def foxMethod(self):
        print("나는 여우입니다")
    def move(self):
        super().move()


ani1 = Wolf()
ani1.move()

ani2 = Fox()
ani2.move()
ani2


