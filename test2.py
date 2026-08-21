# 연산자
v1 = 3
v1 = v2 = v3 = 5
print(v1,v2,v3)


v1 = 10,20,30
print('v1 : ',v1)

a = [1,2,3]
a.insert(1,200)
print(a)

*v1, v2 , v3 = 1,2,3,4,5
print(v1,v2,v3)

print()
print(format(3.14159, '10.4f'))
print(format(3.14159, '10.3'))

name = "민규보"
age = 26
print(f"이름 : {name}, 나이 : {age}")

print("\n")
print("abc")
print("def")
print("abc", end=' ')
print("def")

print(divmod(5,3)) # 몫,나머지 결과 출력
print()
# append와 extend의 차이
a = [1,2,3,4]
b = [5,6,7,8]
a.append(b)
print(a)
print(a[4])
print()
c = [1,2,3,4]
d = [5,6,7,8]
c.extend(d)
print(c)
print(c[4])

# 연산자 우선순위
# () -> ** -> 단항 -> *, / -> +. - -> 비교 -> not -> and -> or -> =

print('관계(비교) 연산자')
print(5 > 3, 5 == 3, 5!=3)

print('논리 연산자')
print(5>4 and 4<3, 5>4 or 4<3, not(5>=4))

print('문자열 더하기')
print('한'+'국'+'만세')
print('한국'*5)

# bool 안에 값이 있으면 True, 없으면 False
print("boolean 처리 :", bool(123), bool(1), bool(-3.5), bool(True))
print("boolean 처리 :", bool(0), bool(0.0), bool(False), bool(None))
print("boolean 처리 :", bool([]), bool({}), bool(set()))

print("이스케이프 문자")
print("aa\tbb")
print(r"aa\tbb")
print("aa\bbb")
print(r"aa\bbb")
print("aa\nbb")
print(r"aa\nbb")
print('c:\a\abc.txt')
print(r'c:\n\abc.txt')