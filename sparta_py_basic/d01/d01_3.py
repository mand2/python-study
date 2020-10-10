"""
기본적인 크롤링 하기- 2
수업에선 dload 라이브러리를 사용하라고 했는데 (dload.save(url, f'')
dload 사용보단 urllib.request 쓰는게 더 나아보여서 이걸로.

    select     : list 형태로 보여줌
    select_one : 단 하나만 가져온다.

저장시 80개 파일이 저장된다...wow....
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request as url_req  # dload 대신 사용.

driver = webdriver.Chrome('../chromedriver')  # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5)  # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')

for idx, thumbnail in enumerate(thumbnails):
    img = thumbnail['src']
    url_req.urlretrieve(img, 'img/iu_' + str(idx) + '.jpg')   # 0부터 시작하므로, 1부터 원한다면 idx+1 로 바꿔야함.

driver.quit()  # 끝나면 닫아주기

