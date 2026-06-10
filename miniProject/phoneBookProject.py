#phobeBookProject

str="1.입력 2.출력 3.검색 4.수정 5. 삭제 6.종료"
result=f'{str}의 메뉴입니다.'
print(result)

print(f"{'입력기능':-^45}")

pList=[]

while True:
    no= int(input("선택: "))
    if  no==1:
        people ={}
        people["name"]=input("성명:  ")
        people["phone"]=input("전화:  ")
        people["addr"]=input("주소:  ")
        pList.append(people)
        print("주소입력완료")
    
    elif no==2:
      print(f"{'출력기능':-^45}")
      print("{:^3} {:^10}{:15}{:20}".format("번호","성명","전화","주소"))
 
      for i, p in enumerate(pList):
        print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
        
    elif no==3:
       print(f"{'검색기능':-^45}")
       print("이름을 입력해 주세요")
       name=input("이름: ")
       found = False
       for p in pList:
          if p["name"]==name:
            print("{:^3}{:^10}{:^15}{:^20}".format("번호","성명","전화","주소"))  
            print("-"*53)
            print("{:^3}{:^10}{:^15}{:^20}".format(pList.index(p)+1,p["name"],p["phone"],p["addr"]))
            found =True
            break
    elif no==4:
        print(f"{'수정기능':-^45}")
        name= input("수정할 이름을 입력하세요:  ")
        found = False
        for p in pList:
            if p['name']== name:
                print("수정할 이름 연락처 주소를 입력하세요")
                p['name']=input("새로운이름: ")
                p['phone'] = input("새로운 전화번호: ")
                p['addr'] = input("새로운 주소: ")                    
                print("연락처가 수정되었습니다.")
                found = True
                break      
        if not found:
            print("해당하는 연락처가 없습니다.")

    elif no == 5:
        print("{:-^50}".format("삭제기능"))       
        name = input("삭제할 성명을 입력하세요: ")
        found = False
        for p in pList:
            if p['name'] == name:                
                pList.remove(p)                              
                print("정보가 삭제되었습니다.")
                found = True
                break
        if not found:
            print("해당하는 정보가 없습니다.")       
    elif no == 6 :
        print("{:-^50}".format("종료합니다."))              
        break
    else :
        print("{:-^50}".format("번호를 잘못 입력하셨습니다."))              
        
    print() #공백 라인추가
   
print("프로그램종료입니다~")




 