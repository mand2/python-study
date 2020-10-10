"""
crawling - selenium, beautifulSoup

selenium:
    특정 웹페이지를 구성하는 HTML 정보를 받아오는 방법 중 파이썬으로 크롬 브라우저를 직접 제어함 브라우저 자동제어
beautifulSoup:
    브라우저에서 내가 원하는 것들을 HTML 태그 등을 이용하여 걸러내는 것.
"""


from selenium import webdriver
driver = webdriver.Chrome('../chromedriver')

driver.get("http://www.naver.com")




