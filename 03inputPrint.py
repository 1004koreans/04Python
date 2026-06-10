#표준 입출력 장치
#좌측 우측 변수 와 값이 있다
i,j,k=7,8,9,
#출력값쇼ㅏ이에 스페이스을 추자함
print(i,j,k)

# 다른 기호를 추가하고 싶으면 _로 추가 가능하다
print(i,k,j, sep='_')
# ㅈ값을 줄 바꾸지 않고 싶을때 end를 사용한다
print(i, end=',')
print(j,end=', ') 
# 여기이서 줄 바꿈이 시작된다
print(k)


#format function; 출력시  서식에 맞추기 위해서 사용한다

#전체 8자리 소수는 3자리
print("원주율=", format(3.143249, "8.3f"))# 소수

#정수는 정체 10자리  
print('맥주=',format(500,"10d")) #정수 ######500

#세자리마다 ,
print('노크북=', format(1580000,"3,d"))# 1,580,000
  
  #서식문자
name="박종훈"
age=13
prince=123.456
print(" 이름; %s, 나이:%d, 용돈: %.2f" % (name, age, prince)) # %.2 소수 두째자리까지  ==%==

#format함수

#인텍스  또는 변수명을 지정한다
menu1="치킨" 
menu2="맥주"
print("오늘{str}은 {0}과{1}로 정했습니다".format(menu1,menu2,str="저녁"))

print("오늘{}은 {}과{str}로 정했습니다".format(menu1,menu2,str="아침"))
  
  #입력받기;키보드로 받으면 무조건 문빠(str)이다
num=input('수자를 입력 받으세요')
print('입력 수자는', num, '이고 , 타입은'type(num))
  
  #문자와 숫자의 합은 에러이다
  
  #연산하려면 모두 정수형으로 교체 int(nmu)
result1=int(num) +10

#입력
results = int(input('123'))*int(input(123)
                                
                                
  #줄 바꾸려면 \를 사용한ㄷ가                            # 
result3= float(input('원주))*\
  (float(input('원지름; )) **2



