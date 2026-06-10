import squlite3
conn=sqlite3.connet)'./saveFiles/biograph.db')
curs=conn.cursor()


curs.excute("update people set pay+ where names=?",
            (9999,'곽제우19'))  



curs.execute ("delete from people where pay=?, (1200),))
             