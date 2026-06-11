# 셀레니움에서 웹드라이버 임포트 
from selenium import webdriver
# 크롬 드라이버 로드. 이때 웹브라우저가 실행됨 
driver = webdriver.Chrome()

 

# 셀레니움을 통해 접속한 후 페이지의 데이터(HTML소스)를 얻어온다. 
url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

# 뷰티플숩을 임포트 한 후 얻어온 데이터를 Soup객체로 변환 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보(순위곡)를 저장할 리스트 생성 
song_data = [] 
rank = 1
# 셀렉터를 이용해서 반복되는 엘리먼트(tr태그)를 얻어온다. 
songs = soup.select('#CHARTrealtime > table > tbody >  tr') 
for song in songs:
    # 노래제목 #CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a//
    # #CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a
    title = song.select('p.title > a')[0].text 
   
    
    # 가수 #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(8) > p > a
    singer = song.select('p.artist > a')[0].text 
    
 
    
    
    # 좋아요 갯수 #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(9) > a
    albumn = song.select('td:nth-child(9)> a')[0].text 
   
    
    # 파싱한 내용을 콘솔에 출력 
    print(title, singer, albumn, sep="|")
    # 리스트에 추가 
    song_data.append(['Bugs', rank, title, singer, albumn])
    # 순위는 1씩 증가 
    rank += 1

# 판다스 모듈 임포트 
import pandas as pd
# 데이터프레임으로 변환시 상단에 컬럼명을 추가 
columns = ['서비스','순위','타이틀','가수','앨범'] 
# columns 속성으로 컬럼 추가 
pd_data = pd.DataFrame(song_data, columns=columns)
# 데이터프레임의 상위 5개 행을 출력해서 확인 5이상은 10
print(pd_data.head(11))
# 엑셀로 저장 
pd_data.to_excel('./saveFiles/bugs_chart1.xlsx', index=False)
