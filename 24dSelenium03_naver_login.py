from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
time.sleep(2)
driver.find_element(By.NAME, 'id').send_keys('johnpark0330')
time.sleep(2) 
driver.find_element(By.NAME, 'pw').send_keys('park0330')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(50)
driver.find_element(By.NAME, 'query').send_keys('가산디지털 무한리필')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(30)

# //*[@id="account"]/div/a
# //*[@id="id"]
# //*[@id="log.login"]