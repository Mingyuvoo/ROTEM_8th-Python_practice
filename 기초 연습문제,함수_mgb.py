#%%######################################################
# 문1) 1~100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
number = 1
sum = 0
while number <= 100:
    if number % 3 == 0 and number % 2 != 0:
        sum += number
    number +=1
print(sum)

#%%######################################################
# 문2) 2~5 까지의 구구단 출력
first = 2
second = 1
while first <=5:
    print(f"{first}단")
    #second = 1
    while second <= 9:
        result = first * second
        print(f"{first}X{second} = {result}")
        second += 1
    first += 1

#%%######################################################
# 문3) 1~100 사이의 정수 중 "짝수는 더하고, 홀수는 빼서" 최종 결과 출력
number = 1
sum = 0
while number <= 100:
    if number % 2 == 0:
        sum += number
    else:
        sum -= number
    number += 1
print(sum)

#%%######################################################
# 문4) -1,3,-5,7,-9,11~99까지의 모두에 대한 합을 출력
number = 1
num_list = []
while number <= 100:
    # print(number)
    num_list.append(number)
    number += 2

count1 = 0
sum1 = 0
while count1 < len(num_list):
    slt_num1 = num_list[count1]
    count1 += 2
    num1 = slt_num1* -1
    sum1 += num1


count2 = 1
sum2 = 0
while count2 < len(num_list):
    slt_num2 = num_list[count2]
    count2 += 2
    sum2 += slt_num2

print(f"최종닶 = {sum1 + sum2}")

#%%######################################################
#문5) 1~100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력

number = 1
while number <= 100:
    first = number // 10 # 나머지
    last = number % 10   # 몫

    if first + last >= 10:
        print(f"{number}이 조건에 맞는 수 결과 = {first + last}")
    number += 1

#%%######################################################
#문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
sum = 0
number = 0
while True:
    number += 1
    sum += number
    if sum > 1000:
        print(number)
        break
print(sum)

#%%######################################################
# 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
first = 1
while first <=9:
    print(f"{first}단")
    second = 0
    while second <= 9:
        result = first * second
        if result > 30:
            print(f"{first}X{second} = {result}")
            break
        second += 1
    first += 1

#%%######################################################
# 문8) 1~1000 사이의 소수와 그 갯수를 출력
num = 2
count = 0
while num <= 1000:
    i = 2
    is_prime = True
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end = ' ')
        count += 1
    num += 1
#%% continue 연습 문제
# 문제 1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
number = 1
while number <= 50:
    if number % 3 == 0:
        number +=1
        continue
    print(number)
    number += 1

#%%######################################################
# 문제2) 1부터 100까지 출력하되, 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력
number = 1
sum = 0
while number <= 100:
    if number %4 == 0:
        pass
    elif number % 6 == 0:
        pass
    elif number % 5 == 0:
        sum += number
        print(number)
    number += 1
print(sum)


