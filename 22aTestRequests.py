import requests
response1 = requests.get('https://www.dhlottery.co.kr/lt645/result')
# print(response1.status_code) # 응답코드를 출력
# print(response1.text) # HTML 코드를 출력


#네이버 통합페이지에서 사용하는 파라메터를 딕션너러로 정의
paramJson = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬 웹크롤링'
}
response2 = requests.get('https://section.blog.naver.com/Search/Post.naver', params=paramJson)
# print(response2.status_code) # 응답코드를 출력
# print(response2.text) # HTML 코드를 출력

#뷰티물슙 모듈 임포트
from bs4 import BeautifulSoup

#reques에서 페이지 정보 수집
url = 'http://daum.net/'
response = requests.get(url)


# 응답코드200이면 ㅇㅋ

if response.status_code == 200:
    
    #뷰티플 객체로 변환한다
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else : 
  # 통신문제가 발생시 응답코드만 출력한다
    print(response.status_code)
    
    
    
    
    
    
    
    
    
    
    '''
    #s_content > div.section > ul > li:nth-child(1) > dl > dt > a > b
    
    '''
    
