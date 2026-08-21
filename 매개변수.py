# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 이유

#%%
def showGugu(start, end=5):
    for dan in range(start,end+1,1):
        print(f"{dan}단")
        for last in range(1,10,1):
            print(f"{dan}X{last} = {dan*last}")

showGugu(2,5)

#%%
print("가변 매개변수")
def func1(*ar):         # * : 여러 개의 인자를 tuple로 묶어서 받겠다는 의미 
    print(ar)
    for i in ar:
        print('밥 : ' + i)

func1('김밥')

#%%
def func2(a, *ar):
    print(a)
    print(ar)

func2('김밥','비빔밥','국수')

#%%
def func3(w,h,**other):                        # ** : 이걸 쓰면 dict로 받음
    print(f"몸무게 : {w}, 키 : {h}")
    print(f"기타 : {other}")

func3(80,180,name = "신기해", age = "33")
#%%
def func4(a,b,*c,**d):
    print(a,b)
    print(c)    # tuple
    print(d)    # dict

func4(1,2,3,4,5)
func4(1,2,3,4,5,kbs = 9, mbc = 11)

#%%
# type hint : 함수의 인자와 반환 값에 type을 적어 가독성 향상
# type에 대한 강제성은 없다.
def typefunc(num : int,data : list[str]) -> dict[str,int]:
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data,start = 1):
        print(f"idx :  {idx} , item : {item}")
        # result[item]  = idx


rdata = typefunc('1',['일','이','삼'])
print(rdata)
rdata = typefunc('한개',[10,20,30])
print(rdata)