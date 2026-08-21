"""
함수 장식자(데코레이터, Decorator)는 기존 함수의 코드를 고치지 않고도 함수의 앞뒤에 새로운 기능을 더해주는 파이썬의 유용한 기능입니다.
@ 기호를 함수 바로 위에 붙여서 사용합니다.
[주요 특징]
코드 수정 없음: 원래 함수 내용을 바꾸지 않고 실행 전후로 로그 기록, 시간 측정, 권환 확인등 할 수 있음
기능 재사용: 로그 기록, 실행 시간 확인 같은 공통 작업을 여러 함수에 쉽게 적용합니다.
가독성 증가: 코드가 깔끔해지고 핵심 기능만 남게 됩니다.

[기본 작동원리]
장식자는 함수를 인자로 받아 내부에서 새로운 함수(보통 wrapper)를 감싸서 반환.
"""
#%%
def make2(fn):
    return lambda : "안녕 " + fn()

def make1(fn):
    return lambda : "반가워 " + fn()

def hellofunc():
    return "홍길동"

hi = make2(make1(hellofunc))            # Decorator 없이 실행
print(hi())                             # 안녕 반가워 홍길동

@make2
@make1
def hellofunc2():
    return "고길동"
print(hellofunc2())
print()

#%%
def traceFunc(func):
    def wrapperFunc(a,b):
        r = func(a, b)
        print(f"함수명 : {func.__name__} (a = {a}, b = {b} -> {r})")
        return r
    return wrapperFunc                  # 함수 주소 반환

@traceFunc
def addFunc(a,b):
    return a + b 

print(addFunc(10,20))





