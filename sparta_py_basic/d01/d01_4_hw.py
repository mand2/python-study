from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request as url_req


driver = webdriver.Chrome('../chromedriver')
driver.get('https://search.naver.com/search.naver?where=image&section=image&query=('
           '%EC%97%AC%EC%9E%90)%EC%95%84%EC%9D%B4%EB%93%A4%20%EC%8A%88%ED%99%94&res_fr=786432&res_to=100000000&sm'
           '=tab_opt&face=0&color=0&ccl=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&datetype=0&startdate=0&enddate=0&start=1')
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > '
                         'a.thumb._thumb > img')

for idx, thumbnail in enumerate(thumbnails):
    img = thumbnail['src']
    url_req.urlretrieve(img, 'img_day01_hw/슈화_' + str(idx + 1) + '.jpg')

driver.quit()
