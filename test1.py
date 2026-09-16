print("환영합니다. 파이썬 세상!")
"""
이건 주석입니다.
실행과는 상관없이 코드에 설명을 달 때 사용
작은 따음표 3개도 가능
"""
# 한 줄 주석
print("작업 계속")

# 변수 : 기억 장소의 이름 - 동적
# 상수 : 기억 장소의 이름 - 정적
var1 = "안녕 파이썬"   
print(var1)

a= 10
b = 20
c = b
print(a,b,c)
print("주소출력 : ",id(a),id(b))
print(a is b , a==b)             # a is b : 주소를 비교하는 것, a == b : 값을 비교하는 것
print(b is c, b == c)            # a is b : 주소를 비교하는 것, a == b : 값을 비교하는 것

aa = [100]
bb = [100]
print(" ")
print(aa is bb, aa == bb)
print(id(aa), id(bb))

print()

import keyword # 외부 모듈 읽기 - 보조 기억장치에 저장된 모듈을 주깅거 장치로 로딩
print('키워드(예약어) 목록 :', keyword.kwlist)
# 주의 : 예약어는 사용자 이름으로 사용불가
print('type(자료형) 확인')
print(5,type(5))
print(5.4,type(5.4))
print(3+4j, type(3+4j))
print(True, type(True))
print('kbs', type('kbs'))

print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'key' : 3}, type({'key' : 3}))
print()

a = "strong"
print('b'.join(a))

