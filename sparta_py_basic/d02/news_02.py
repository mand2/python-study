"""
`scrapping`한 기사 `excel`로 저장하기
"""

from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('../chromedriver')
search_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=트럼프+확진'

driver.get(search_url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# excel 파일 생성
wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

# 기사 블럭으로 블럭별 대표기사 제목/url/언론사
article_block = soup.select('#main_pack > div > ul > li')

for article in article_block:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text

    ws1.append([title, url, company[:len(company) - 6]])

driver.quit()

wb.save(filename='articles_1002.xlsx')
