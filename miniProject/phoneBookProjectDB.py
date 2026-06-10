import pymysql 

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', database='sample_db', charset='utf8')
curs = conn.cursor()

pList=[]

while True:
  
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    if no == 1:
        print("{:-^50}".format("입력기능"))
    
        people ={}
        people["name"] = input("성명>>> ")
        people["phone"] = input("전화>>> ")       
        people["addr"] = input("주소>>> ")
    
        sql =f"""INSERT INTO phonebook(name, phone, addr)
            VALUES ( '{people["name"]}', '{people["phone"]}','{people["addr"]}')"""
        try:    
            curs.execute(sql)
            conn.commit()
            print("1개의 레코드가 입력됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행시 오류발생", e)
        print("주소 입력 완료!")
    
    elif no == 2:
        print("{:-^50}".format("출력기능")) 
        print("{:^3}{:^10}{:^15}{:^20}".format("번호","성명"
                                              ,"전화","주소"))      
        print("-"*53) 
    
        sql="SELECT * FROM phonebook order by idx desc"
        curs.execute(sql)
        rows=curs.fetchall()
        for rwo in rows:
            print("{:^3}{:^10}{:^15}{:^20}".format(row[0], row[1]
                                                   ,row[2], row[3]))
    
    elif no == 3:
        print("{:-^50}".format("검색기능"))     
        print("이름을 입력해주세요.") 
        name = input("이름: ")
        print("{:^3}{:^10}{:^15}{:^20}".format("번호","성명"
                                                ,"전화","주소"))      
        print("-"*53)
        sql = "SELECT * FROM phonebook where name like '%{0}%' \
                  order by idx desc".format(name)
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print("{:^3}{:^10}{:^15}{:^20}".format(row[0], row[1]
                                                    , row[2], row[3]))

    elif no == 4 :
        print("{:-^50}".format("수정기능"))   
        name = input("수정할 성명을 입력하세요: ")
        sql = """update phonebook 
                set phone='{1}', addr='{2}'
                where name={0}
            """.format(name, input('전화번호:'), input('주소:'))
        try:    
            curs.execute(sql)
            conn.commit()
            print("1개의 레코드가 수정됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행시 오류발생", e)

    elif no == 5 :
        print("{:-^50}".format("삭제기능"))       
        name = input("삭제할 성명을 입력하세요: ")
        sql = f"delete from phonebook where name='{name}'"
        try:
              curs.execute(sql)
              conn.commit()
              print("1개의 레코드가 삭제됨")
        except Exception as e:
              conn.rollback()
              print("쿼리 실행시 오류발생:", e)

    elif no == 6 :
        print("{:-^50}".format("종료합니다."))              
        break
    
    else :
        print("{:-^50}".format("번호를 잘못 입력하셨습니다."))              
          
    print() #공백 라인추가

conn.close()        
print("프로그램종료~")

      
    
    
      
      
      
          
          
      