str='coffee'
result=f'{str} is the best in a day'
print(result)

result4 =f'{str:-^50}'
print(result4)

str='문자열처리'
result1=f'{str:<10}'
result2=f'{str:^10}'
result3=f'{str:>10}'
 
print(result1)
print(result2)
print(result3)
 

lists=[11,22,33]
print(f'list: {lists[0]}, {list[1]}, {lists[2]}')
for v in lists:
  print(f'repeat:{v}')