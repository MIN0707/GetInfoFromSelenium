import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://naver.com/'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=url)
driver.find_element('id', 'query').send_keys("파이썬")
driver.find_element('xpath', '//*[@id="search_btn"]').click()
driver.find_element(By.LINK_TEXT, 'VIEW').click()
driver.find_element(By.LINK_TEXT, '블로그').click()

html = driver.page_source  # 셀레니움으로 html 문서 가져오기
dom = BeautifulSoup(html, 'html.parser')

item_list = dom.select('.total_area')

result = []
for item in item_list:
    tempdict = {
        'post_title': item.select_one('.total_tit').text,
        'blog_title': item.select_one('.sub_name').text
    }
    result.append(tempdict)
print(result)
