# 반복문 for
# for target in object:
#      statement...

# for i in [1,2,3,4,5]:         --> () : tuple 가능 // {} : set 가능
#     print(i, end = ' ')
import numpy as np
print("분산/표준편차")
numbers = [1,3,5,7,9]
sum = 0

for i in numbers:
    sum += i

print(f"합 = {sum}, 평균 = {sum/len(numbers)}")

avg = sum / len(numbers)
# 편차의 합
total_sum = 0
for i in numbers:
    total_sum += (i-avg)**2

print(total_sum)
var = total_sum / len(numbers)
print(f"분산은 {var}")
print(f"표준편차는 {np.sqrt(var)}")
print()

colors = ["빨강", "초록", "파랑"]
for v in colors:
    print(v, end = ' ')
print()

print("iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수")
iterator = iter(colors)
for v in iterator:
    print(v)
print()

# enumerate() : 인덱스와 값을 반환 할 수 있는 함수
# enumerate(.., start = 1) : 0 1 2 인데 start = 1로 함으로써 1 2 3으로 됨
for idx, d in enumerate(colors, start = 1):
    print(idx,' ',d)
print()
#%%
print("===사전형===")
datas = {'python':'만능언어', 'java':'웹용언어','mariadb' : 'RDMBS'}
print(datas)
print()
print(datas.items()) # 반환값이 리스트 안에 튜플 형태로 있음 --> dict_items([('python', '만능언어'), ('java', '웹용언어'), ('mariadb', 'RDMBS')])

for i in datas.items():
    print(i[0], '==' , i[1])      # i[0] : key가 나옴 // i[1] : value가 나옴
print()

for k,v in datas.items():
    print(k, '==', v)

print()
for k in datas.keys():
    print(k,end =  ' ')

print()
for v in datas.values():
    print(v, end = ' ')

print('다중 for')
for n in [2,3,]:
    print(f"{n}단")
    for su in [1,2,3,4,5,6,7,8,9]:
        print(f"{n} * {su} = {n*su}")

#%%
print("===nfor : continue, break ===")
nums = [1,2,3,4,5]
for i in nums:
    if i == 2:
        continue
    if i == 4:
        break
    print(i, end = ' ')
else:
    print("정상 종료")

#%%
print("정규표현식 + for문 연습")
message = """
미국프로야구 메이저리그(MLB) 구단주들이 샌디에이고 파드리스의 매각을 만장일치로 승인했다.
매각 금액은 39억 달러(약 5조5000억 원)로 MLB 구단 거래 사상 최고액이다.

MLB는 17일(현지시간) 화상 회의를 열고 억만장자 투자자 호세 E. 펠리시아노와 콴자 존스 부부의 샌디에이고 인수를 승인했다.
두 사람은 지난 4월 사이들러 가문으로부터 구단 지분 40% 이상을 사들이기로 합의했다. 구단 매각 절차는 수일 안에 마무리될 예정이다
"""
import re
# 패턴과 일치하는 문자열을 다른 문자열로 치환
message2 = re.sub(r'[^가-힣\s]', '',message) # r'^[] : 시작을 의미 // r'[^] : 부정을 의미
print(message2)
message3 = message2.split(' ') # 공백 기준 문자열 분리
print()
print(message3, '', len(message3))

# 단어별 빈도수 출력 : dict 사용
count = {}
for i in message3:
    if i in count:
        count[i] += 1 # 같은 단어가 있으면 누적
    else:
        count[i] = 1 # 최초 단어일 경우 '단어' : 1
print(count)

#%%
print("정규표현식 +a")
for imsi in ['111-1234','일이삼-일이삼사','222-1234','333&1234']:
    if re.match(r'^\d{3}-\d{4}$', imsi):
        print(imsi, '전화번호 맞습니다.')
    else:
        print(imsi, "전화번호 아닙니다.")

#%%
print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
print(list(i for i in a if i % 2 == 0))

#%%
datas = [1,2,'a',True, 3.0]
li2 = [i for i in datas if type(i) == int]
print(li2)

#%%
id_name = {1:'tom', 2:'james'}
name_id = {val : key for key, val in id_name.items()}
print(name_id)

#%%
aa = [(1,2),(3,4),(5,6)]

for a,b in aa:
    print(a+b)

print(*[a + b for a, b in aa], sep='\n')

#%%
print("수열 생성 : range(start, stop, step) 사용")
print(list(range(1,6)))
print(tuple(range(1,6)))
print(set(range(0,6)))
print(set(range(6)))
print(list(range(-10,-100,-20)))
print()

for i in range(6):
    print(i, end = ',')

print()
for _ in range(6):
    print("반복")

print("1~10까지의 정수 합")
total = 0
for i in range(1,11):
    total+= i
print(total)
print(sum(range(1,11)))
print()

for i in range(1,10):
    print(f'2*{i} = {2*i}')

#%%
print("2~9 구구단")
for i in range(2,10,1):
    print()
    print(f"{i}단")
    for k in range(1,10,1):
        print(f"{i}X{k} = {i*k}")

#%%
print("주사위를 두번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력")

for i in range(1,7,1):
    for k in range(1,7,1):
        sum = i + k
        if sum % 4 == 0:
            print(f"{i},{k} --> {sum}")
        else:
            continue

print()
for i in range(6):
    n1 = i+1
    for j in range(6):
        n2 = j+1
        n = n1 + n2
        if n % 4 == 0:
            print(n1,n2)







