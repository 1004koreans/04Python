'''
시나리오] 입력한 문자열에 영문대문자, 소문자, 숫자만 포함되어 있다면 True, 
나머지 문자가 하나라도 포함되면 False를 반환하는 프로그램을 작성하시오.
'''

s = input('문자열을 입력해주세요:')
result=True


for ch in s:
    if not(ch.isupper() or ch.islower() or ch.isdigit()):
      result=False
print(f"입력한 문자열:  {s}")
print("결과:%s" % result )
