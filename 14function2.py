print(f"{'2개 이상의 반환값을 가진 함수':-^30}")


def min_max(num):
  sum =0
  for val in num:
      sum += val
    
  return sum, min(num), max(num)
numbers=(8,9,6,5,4,3,2.7)
sumval, minval, maxval= min_max(numbers)

print("튜풀의 합, 최대값, 최소값:", sumval, minval, maxval)
      
      
total=0
def sum(arg1, arg2):
    total = arg1+arg2
    print( "local variable =", total) 
  return total
print