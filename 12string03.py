"""
format() 함수 사용하기
    : 문자열 포매팅(String formatting)은 서식문자보다 더 간단히 문자열을
    표현할 수 있다. 
    {} 중괄호 안에 포매팅을 지정하고 format() 함수로 값을 삽입한다. 
    형식]
        '{인덱스}' . format(값 또는 변수)
"""

str1='name:{0}'.format('johnparker')
print(str1)

age=55
str2='age:{0}'.format(age)
print(str2)

str3='name:{name},age:{age}'.forma(name='johnparker',age=33)

str4='name;{name}, age:{age}'.format(name='johnparker',age=70)

str5='age:{1}, name{0}'.format('johnparker',70)

str6='iteem1:{0}, g item2:{1}, item3:{0}'.format('seoul', 'busan')

str7=' naumber position: {0.03d}, {1:03d}',foamt(12345,12)

str8=' under deciaml:{0:0.2f}., demal under5 position:{1:0.5f}\
  .format(123.12345667788898,31.4}
  str9='{{{0]}}}.formamt('Pysthon {}')
  print('str9-'. sat9)
  
  str10=159200
  print(format(st10, ','))


