'''
연습문제1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 
출력하는 프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
#Score Input
Num1=int(input("국어점수를 입력해주세요: "))
Num2=int(input("영어범수를 입력해주세요: "))
Num3=int(input("수학점수를 입력해 주세요:  "))

#Avg
avg= int(( (Num1+Num2+Num3)/3))

print(avg)

if 


# 90점 이상은 A학점 
# 80점 이상은 B학점
# 70점 이상은 C학점
# 60점 이상은 D학점    
# 60점 미만은 F학점으로 판단

if avg>90:
  print("당신의 평균학점은 A입니다")
elif avg>80:
  print("당신의 평균학점은 B입니다"
elif avg>70:
  print("당신의 평균학점은 c입니다")
elif avg>60:
  print("당신의 평균학점은 D니다"
esle:
  print("당신의 평균학점은 F입니다")
