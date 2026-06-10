# 산술연산자
#3개의 변수를 사용한다, 정수형이다
x=2
y=4
z=8

print("x+y",x+y)
print("x-y",x-y)
print("x*y",x*y)

# 나누기 /인경우 결과는 실수형으로 반환
# 나누기//인겨우 결과는 몫으로 정수으로 반환
print("x/y",x/y)
print("x//y",x//y)

# 거듭제곱 x의 y승
print("x**y",x**y)

# 거듭제곱의 반환
print("pow(w,y)",pow(x,y))  
     
# x의 y승을 z로 나눔
print("pow(x,u,z)",pow(x,y,z))

# x를 y로 나눈 몫과 나머지를 tuple로 반환
#tutple = array
print("divmod(x,y)",divmod(x,y))

'''
수학게 관련된 함수를 수학(math)모듈을 현재 문서에
수입(Import)한후 책토일얼 함수를 실행한다'''

import math
print("math.factorial(5)",math.factorial(5))