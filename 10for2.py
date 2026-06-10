total =0
for i in range(1, 101):
   if i%3==00:
     total+=1
     print(i, end=' ')
     
     
print('\b', '+', total)

print()
print("="*45)
      
list=[n**2 for n in range(10) if n%3==0]
print(list)
print()

list=[n**2 for n in range(10) ]
print(list)
print()

print("="*45)

'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
''' 

# list=[0,0,0,0]
# list.insert(1):

print('insert(1)', list)
for x in range (5):
    for y in range(5):
      if x==y:
        print("1", end=' ')
      else:
          print("0", end=' ')
print()

for i in range(5):
  for j in range(5):
     if i>=j:
       print(" ", end='  ')
       
       print()
    