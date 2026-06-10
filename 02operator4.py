'''
문자에서 사용하는 연산자'''

''''
여러줄의 문자열은 싱글 또는 더블 퀘테인션마크로 작성한다'''
str=""" 여러줄의 문자열은 더블퀘테이션을 3개 작성한다"""

print(str)
# 문자열 변수
head="난 헤더  "
bottom = "난 바텀"
# 문자열+는 연결함
print(head+bottom)
print(head*3)
print("==="*13)

# 문자열 슬라이싱
'''문자열을 짤라내시 인테스는 0에 시작
콜론 범위를 지정할 수있다
0:10는 0~9ㅡ를 의마한다
즉 시작은 포함되고 종료는 미만이다'''
engStr="Hello Python Good"  
print(engStr[0]) #0번 인테스 H
print(engStr[:3])#시작이 없으면 처음부터시작 0~2까지
print(engStr[1:3])#1~2
print(engStr[1:])#종료가 없으면 끝까지
'''종료바로 앞에 까지 '''

#파이션은 한ㄱ들링든지 영어든지 동일하다
korStr =" 안녕하세요? 파인션입니다" 
print(korStr[0])
print(korStr[:2])
print(korStr[0:6])

'''정수와 문자는 연결할 수가 없다. 타임에러이다'''
# print(engStr+100)