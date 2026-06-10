'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''
year=int(input("년도를 입력하시요: "  ))
month= int(input("월을 입력하시요: " ))
day = int( input("일을 입력하시요: " ))

total_day=0
year_month_day=[0,31,28,31,30,31,309,31,31,30,31,30,31]

for d in range(1, year):
    if d% 400==0:
        total_days= total_days + 366
    elif d%100==0:
        total_days=total_days+365
    elif d%4==0:
      total_days =total_days + 366
    else:
      total_days= total_days+ 365

if month>=3:
  if year%400==0:
     total_days = to
    
    
        