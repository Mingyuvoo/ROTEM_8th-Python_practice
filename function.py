#%%
# function : 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 고유의 공간을 갖는다.
# 자원의 재활용이 가능.

# 내장함수
print(sum([1,2,3]))
print(8,bin(8))
print(eval('4+5'))
print(round(1.2))   # ceil : 올림, floor : 내림
import math
print(math.ceil(1.2), ' ', math.floor(1.7))

b_list = [True, 1, False]
print(all(b_list))      # False  : 모두 참일경우에만 True가 나옴
print(any(b_list))      # True   : 모두 false일 경우에만 false 나옴

data1 = [10,20,30]
data2 = ['a','b']

# zip으로 만들면 최종적으로 tuple 형태가 됨
for i in zip(data1, data2):
    print(i)

#%%
# 사용자 정의 함수
"""
def 함수명(가인수,,):    # dummy argument, 매개변수    
    #...
    return 반환값       # 1개만 반환, return이 없으면 return None

"""

# 함수 선언
def doFunc1():
    print('doFunc 수행')

doFunc1()


#%%
def doFunc2(name):
    print('name:', name)
doFunc2("민규보")

def doFunc3(arg1,arg2):
    re = arg1 + arg2 
    return re

doFunc3

def doFunc4(a1,a2):
    imsi = a1+ a2
    if imsi % 2 ==  1:
        return # 함수 내에 return은 무ㅗ건 탈출
    else:
#%%
# def triArea(a,b):
#     c = a*b/2
#     triAreaPrint(c)

# def triAreaPrint(arg):
#     print("삼각형의 면적", arg)

# triArea(20,30)
# print()

#%%
def passResult(kor,eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20,30):
    print("합격")
else:
    print("불합격")

#%%
def swapFunc(a,b):
    return {b,a}
a = 10
b = 10
print(a,' ',b)
print(swapFunc(a,b))

#%%
def funcTest():
    print('funcTest 맴버 처리')
    def funcInner():
        print('내부함수 실행')
    funcInner()

funcTest()

#%%
# if 조건식 안에 함수 적용
def isOdd(para):
    return para % 2 == 1    # 홀수이면 True 반환

# mydict = {x:x for x in range(11) if isOdd(x)}

# print(mydict)

mydict = {}

for i in range(11):
    if isOdd(i) == 1:
        mydict.update(i)
print(mydict)

#%%
print("변수의 생존 범위(scope rule)")
# 변수가 저장되는 이름공간은 변수가 어디에서 선언 되었는가에 따라 생존 시간이 다르다 
# 전역, 지역 변수
# Local > Enclosing function > Global > Built-in

player = "전국대표"         # 전역변수 (현재파일(모듈) 어디서든 호출 가능)
name = "신기해"

def funcSoccer():
    name = '이기자'         # 지역변수 (현재 함수 내에서만 유효)
    city = "서울"           
    print(f"이름은{name} 수준은 {player}")
    print(f"지역은{city}")

funcSoccer()

#%%
a = 10; b = 20; c = 30      # 전역 변수
print(f"foo 수행 전 a : {a}, b:{b}, c:{c}")

def foo():
    a = 7                   # 지역 변수
    b = 100
    def bar():
        global c            # bar의 맴버가 아니라 모듈의 맴버가 됨(전역 변수)
        nonlocal b          # 이걸 사용함으로써 bar의 지역변수가 아닌 foo 지역변수로 승격
        b = 8               # 지역 변수
        print(f"Bar 수행 중 a : {a}, b:{b}, c:{c}")
        c = 9
        b = 200
    bar()
    print(f"Bar 수행 후 a : {a}, b:{b}, c:{c}")

foo()
print(f"foo 수행 후 a : {a}, b:{b}, c:{c}")


#%%
g = 1
print('g:',g)
def func():
    global g
    a = g
    g = 2
    return a

print(func())
print('g:',g)
