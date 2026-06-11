from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = 'https://www.ikosmo.co.kr/main'
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="subConts"]/div/div/div/div/section/section/form/fieldset/div[2]/ul/li/a').click()
time.sleep(2)
driver.find_element(By.NAME, 'id').send_keys('johnparker')
time.sleep(2) 
driver.find_element(By.NAME, 'pw').send_keys('park0330!')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="subConts"]/div/div[1]/div/div[2]/section/section[1]/form/fieldset/p[2]/a').click()
time.sleep(2)
driver.find_element(By.NAME, 'query').send_keys('교육은 온/오프라인 강의로 진행되나요?')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(50)

 


#//*[@id="subConts"]/div/div/div/div/section/section/form/fieldset/div[2]/ul/li/a

#//*[@id="subConts"]/div/div[1]/div/div[2]/section/section[1]/form/fieldset/p[2]/a