import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
        password='1234', db='sample_db', charset='utf8', port=3306)
curs = conn.cursor()

sql = f"""INSERT INTO board (title, content, id, visitcount)
	  VALUES ('{input('제목:')}', '{input('내용:')}', 'nakja', 0)"""
 
try:
    curs.execute(sql)
    conn.commit()
    print("1개입력")
    
except Exception as e:
    conn.rollback()
    print('오류발생', e)
    
    
conn.close()