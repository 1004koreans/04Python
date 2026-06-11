# 셀레니움에서 웹드라이버 임포트 
from selenium import webdriver
# 크롬 드라이버 로드. 이때 웹브라우저가 실행됨 
driver = webdriver.Chrome()

 

# 셀레니움을 통해 접속한 후 페이지의 데이터(HTML소스)를 얻어온다. 
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

# 뷰티플숩을 임포트 한 후 얻어온 데이터를 Soup객체로 변환 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보(순위곡)를 저장할 리스트 생성 
song_data = [] 
rank = 1
# 셀렉터를 이용해서 반복되는 엘리먼트(tr태그)를 얻어온다. 
songs = soup.select('tbody > tr') 
for song in songs:
    # 노래제목
    title = song.select('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')[0].text 
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    
    # 가수
    singer = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')[0].text 
    
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
    
    
    # 좋아요 갯수 
    favo = song.select('td:nth-child(8) > div > button > span.cnt')[0].text 
    #lst50 > td:nth-child(8) > div > button > span.cnt
    
    # 파싱한 내용을 콘솔에 출력 
    print(title, singer, favo, sep="|")
    # 리스트에 추가 
    song_data.append(['Melon', rank, title, singer, favo])
    # 순위는 1씩 증가 
    rank += 1

# 판다스 모듈 임포트 
import pandas as pd
# 데이터프레임으로 변환시 상단에 컬럼명을 추가 
columns = ['서비스','순위','타이틀','가수','좋아요'] 
# columns 속성으로 컬럼 추가 
pd_data = pd.DataFrame(song_data, columns=columns)
# 데이터프레임의 상위 5개 행을 출력해서 확인 5이상은 10
print(pd_data.head(11))
# 엑셀로 저장 
pd_data.to_excel('./saveFiles/melon_chart3.xlsx', index=False)
