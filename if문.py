#%%
# 조건 판단문 if
var = 1

if var >= 3:
    print("크네")
    print("크구만")
print()
if var >= 3:
    print("크구나")
else:
    print("작구나")

print()
print("끝")

#%%
money = 700
age = 55

if money >= 500:
    item = "사과"
    if age <= 30:
        msg = "참 참"
    else:
        msg = "참 거짓"
else:
    item = "복숭아"
    if age >= 20:
        msg = "거짓 참"
    else:
        msg = "거짓 거짓"    

print(f"중복 수행 후 결과{item},{msg}")
print()

data = int(input("점수입력:"))
print(data,type(data))
if data >=90:
    print("우수")
else:
    if data >=80:
        print("보통")

jumsu = 88
print(jumsu)
if jumsu >= 90:
    print("우수")
elif jumsu >= 80:
    print("보통")
else:
    print("저조")
#%%
jum = 80
if 90<= jum <= 100:
    print('A')
elif 70<=jum<90:
    print("B")
else:
    print("C")

#%%
names = ['홍길동','신기해','이기자']
if '홍길동' in names:
    print("있음")
else:
    print("없음")

#%%
if ((count:=len(names)) >= 3):            # := 이거는 대입 표현식
    print(f"인원수가{count}입니다")
else:
    print(f"안됩니다.")

#%%
scores = [95,88,76,92,81]
if (avg := sum(scores) / len(scores)) >= 80:
    print(f"우수반 평균 점수 : {avg}")
else:
    print("별로야")

#%%
print("삼항 연산")
a = 'kbs'
b = 9 if a == 'kbs' else 11
print('b : ',b)

#%%

a = 11
b = 'mbc' if a == 9 else 'kbs'
print("b : ",b)

#%%
a = 3
print(0 if a < 5 else 1 if a < 10 else 2)