#%%
# 반복문 while  조건:       조건이 참인 동안 블럭 수행
a = 1 # 조건에 초기지
while a<=5:         # 조건
    print(a,end ='')
    a += 2
else:                   # 선택적 : 조건에 따른 종료시 수행
    print('수행성공')
#%%
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i=' + str(i) + ',j=' + str(j))
        j = j+1
    i+=1
#%%
print("1~100 사이의 정수 중 3의 배수의 합은?")

i = 1
sum = 0
while i <= 100:
    i += 1
    if i % 3 == 0:
        sum += i

print(sum)

#%%
colors = ["r","g","b"]
num = 0
while num < len(colors):
    print(colors[num])
    num += 1

#%%
print("if 블럭 내에 while문 사용")
import time
print("a")
time.sleep(2)
print("b")
#%%
"""
import time
sw = input("폭탄 스위치를 누를까요[y/n]")
if sw == 'Y' or sw == 'y':
    count = 5
    while 1 <= count:
        print("%d초"%count)
        time.sleep(1)
        count -=1
    print("뻥")
elif sw == 'N' or sw == 'n':
    print("작업 취소")
else:
    print("다시 입력하세요")

"""

print('countinue/break')
a = 0
while a < 10:
    a += 1
    if a == 7:
        break               # 반복문 무조건 탈출
    elif a == 5:
        continue
    print(a)

#%%
print("키보드로 정수를 입력 받아 홀수, 짝수 출력")
while 1:
    number = int(input("정수입력하세요"))

    if number == 0:
        print("프로그램 종료")
        break
    elif number % 2 == 0:
        print("짝수")
        continue
    else:
        print("홀수")


#%%
