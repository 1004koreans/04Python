
# 피이선은 문장끝에 세미톨론을 사용하지 않능ㄴ다
# 문자와 문자열의 구분이 없고 싱글 혹은 더불을 사용한다
a="Hello Pytho"
print(a,id(a))
print("한줄에"); print("여려줄 쓰려면"); print("세미톨론이 필요함")

#변수를 사용시 지료형을 알리는 키위드가 필요없다
# 변수하나에 한개만 정한다
a=100
print(a, id(a))

#정수형
i=200
print(i, type(i))
#실수형
i=3.14
print(i,type(i))

# Bool형
# 작성시 첫글자는 대문자
i=True
print(i, type(i))

      
#문지형
i="안녕"
print(i,type(i))

# 변수와 참조값을 좌 = 우로 분리한다 
r,g,b="Red","Green","Blue"
print(r,g,b)
