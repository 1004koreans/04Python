multilambda = lambda x: x*2
listdata1=[1,2,3,4,-1,-2, -32,-4, -5, -10]
result = list(map(multilambda, listdata1))
print( 'final', result)
#sss
listdata2=[1,2,3,4,5,6,7,8,9,10]
strlambda =lambda: '3X' if x%3==0 else x
result = list (map(strlambda, listdata2))
print('final', result)
