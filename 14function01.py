'''
함수
    형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
    상황에 따라 매개변수와 return은 생략 가능하다.  
'''

print(f"{'함수의 정의및 호출':-^45}")
#print(f"{'함수정의 및 호출':-^30}")

def sum():
    sum=0
    for i in range(1,11):
        sum+=i
        print('1-10 합=', sum)      
        
sum()        
        
        
        