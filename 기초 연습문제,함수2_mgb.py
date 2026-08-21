#%%
# ======================== 문제 1 ======================== #
# 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기

def inputfunc():
    global datas
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas
datas = inputfunc()
def professfunc(datas):
    # 급여액 = 기본급 + 근속수당
    # 수령액 = 급여액 - 공제액
    print("사번     이름     기본급     근무년수     근속수당     공제액     수령액")
    print("--------------------------------------------------------------------")
    give_money = []
    for i in range(0,len(datas)):
        work_year_list = []
        start_year = datas[i][3]
        work_year = 2026 - start_year
        
        work_year_list.append(work_year)
        if 0<= work_year and work_year <= 3:
            give_money.append(datas[i][2] + 150000)
        elif 4<= work_year and work_year <= 8:
            give_money.append(datas[i][2] + 450000)
        elif work_year>= 9:
            give_money.append(datas[i][2] + 1000000)

    take_money = []
    for j in range(0,len(datas)):
        if give_money[j] >= 3000000:
            take_money.append(give_money[j] - give_money[j]*0.5)
        elif give_money[j] >= 2000000:
            take_money.append(give_money[j] - give_money[j]*0.3)            
        elif give_money[j] < 2000000:
            take_money.append(give_money[j] - give_money[j]*0.15)

    for i in range(len(datas)):
        print(datas[i][0], '      ' + str(datas[i][1]), '  ', datas[i][2],'    ', work_year, '      ', give_money[i] - datas[i][2], '   ', int(give_money[i] - take_money[i]), '    ', int(take_money[i]))
    return print(f"처리 건수 : {len(datas)}")

professfunc(datas)

# %%
# ======================== 문제 2 ======================== #
# 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기


# 입력 함수
def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

datas = inputfunc()
dic = {"새우깡" : 450, "감자깡" : 300, "양파깡" : 350}

def output(datas):
    print("상품명   수량   단가    금액")
    print("--------------------------")
    sum_shirimp = 0
    tot_shirimp_sum = 0

    sum_potato = 0
    tot_potato_sum = 0

    sum_onion = 0
    tot_onion_sum = 0
    for i in range(len(datas)):
        menu = datas[i][0:3]
        num = int(datas[i][4:])
        
        if menu == "새우깡":
            price = num * dic["새우깡"]
            sum_shirimp += num
            tot_shirimp_sum += price 

        elif menu == "감자깡":
            price = num * dic["감자깡"]
            sum_potato += num
            tot_potato_sum += price

        elif menu == "양파깡":
            price = num * dic["양파깡"]
            sum_onion += num
            tot_onion_sum += price

        print(menu,'  ', num, '  ', price // num, '  ', price)
    print()
    print("소계")
    print(f"새우깡 : {sum_shirimp}건   소계액 : {tot_shirimp_sum}원")
    print(f"감자깡 : {sum_potato}건   소계액 : {tot_potato_sum}원")
    print(f"양파깡 : {sum_onion}건   소계액 : {tot_onion_sum}원")
    print("총계")
    print(f"총 건수 : {sum_shirimp + sum_onion + sum_onion}")
    print(f"총 액 : {tot_shirimp_sum + tot_onion_sum + tot_potato_sum}")

output(datas)

#%%
# ======================== 문제 3 ======================== #
# 상품 주문 및 할인 처리 프로그램
products = {
    "노트북": 1500000,
    "모니터": 350000,
    "키보드": 80000,
    "마우스": 50000
}
price = products.values()
print(price)
#%%
# logic 설계
# discount_func을 바꿔줘야됨(discount10, discount20)
    # discount10,20을 lambda 함수를 사용해서 설정해야됨
    # discount10,20을 통해서 적용된 값이 나와야됨
    # closure를 사용해야하는데 만약에 discount10,20이 적용되면 return으로 최종 금액이 나와야됨

def order(product, count, discount_func_None):

    price = product.values() * count

    print(price)
    discount10 = lambda dc_10 = 0.1 : price * dc_10
    discount20 = lambda dc_20 = 0.2 : price * dc_20

print(order("노트북",1))                      # 1500000

