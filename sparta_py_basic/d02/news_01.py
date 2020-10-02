"""
news scrapping
"""


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('../chromedriver')

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=트럼프+확진'

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 맨처음, 대표 기사
article_1st = soup.select_one('#sp_nws1 > dl > dt > a')
print(article_1st.text)  # 문대통령, '코로나 확진' 트럼프에 위로전…"조속한 쾌유 기원"(종합)
print(article_1st['href'])  # http://yna.kr/AKR20201002045851001?did=1195m


# 기사 블럭으로 블럭별 대표기사 제목/url/언론사
article_block = soup.select('#main_pack > div > ul > li')

for article in article_block:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text

    print(title, url, company[:len(company)-6])

driver.quit()

