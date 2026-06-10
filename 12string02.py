str='my name is %s'

print('str1=', str)

names=['John', 'Hyun', 'becky']
for n in names:
  print( 'name:%s' %n)
  
  money =10000
  str='my mouse price is %d' % money
  print(str)
  
  pi=3.14
  print('circle %f' % pi)
  print('circle %5.3f' % pi)
  
  str='name: %s, age:%d' %('name', 70)
  print(str)
  
  phone, age, height ='010-5954-2030', 70, 171.78
  str2='phone:%s, age:%d, height: %f' % (phone, age, height)
  print('str2=', str2)