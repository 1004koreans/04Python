did1=dict()
dic2= dict(birth =1957, name="Park", size="173cm")
print(dic2)

fruits = {'apple':100, 'grape'=200,'orange'=300, 'peach'=400}
 for key in fruits:
     val=fruits[key]
    print("%s: %d:" %(key, val))
     
print('봉숭아", fruits['peach'])

del fruits['peach']
print('봉숭아삭제', fruits)

