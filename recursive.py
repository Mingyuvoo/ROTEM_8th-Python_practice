# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리 가능

#%%
def countDown(n):
    if n == 0:
        print("완료")
        return
    else:
        print(n, end = ' ')
    countDown(n -1)             # 재귀

countDown(5)

#%%
print("1부터 n까지의 정수의 합 구하기")
def sumAll(n):
    if n == 1:
        return 1

    return n + sumAll(n-1)    

print(sumAll(5))

#%%
print("")
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n * factorial(n-1)    

print(factorial(0))
