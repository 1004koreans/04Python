# 대입연산자
a=tot=100

# 복합연산자
a+=1
tot+=a
print(a,tot)

# 최초100, 200 할당후 교체하려면 서로 교환한다
v1,v2=100,200
v2,v1=v1,v2
print('변수교체',v1,v2)

# 5개의 list를 선언후
mylist =[1,2,3,4,5]

# x1=1,a나머지는 x2로 넣음
x1, *x2= mylist
print('패킹연산자1', x1,x2)


*y1, y2= mylist
print('패킹연산자2',y1,y2)

