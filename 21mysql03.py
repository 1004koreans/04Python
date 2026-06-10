import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', database='sample_db', charset='utf8')
curs = conn.cursor()

sql = """update board 
            set title='{1}', content='{2}'
            where num={0}
""".format(input('수정할일련번호:'), input('제목:'), input('내용:'))


import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8')
curs = conn.cursor()