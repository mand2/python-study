"""
google 검색결과로 image scrapping and save
참고 url: https://medium.com/@wwwanandsuresh/web-scraping-images-from-google-9084545808a2
"""

from selenium import webdriver
import time
import urllib.request as url_req

driver = webdriver.Chrome('chromedriver')
search_url = 'https://www.google.com/search?q=아이들+슈화&source=lnms&tbm=isch'
driver.get(search_url)


# 클릭 > 미리보기 `image url`로 가져오기
def get_image_urls(image_list, image_num):
    idx = 0

    for img in image_list:
        img.click()
        preview_image = driver.find_element_by_css_selector(
            '#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz '
            '> div.OUZ5W > div.zjoqD > div > div.v4dQwb > a > img')
        time.sleep(1)  # driver.implicitly_wait(600) 해도 속도가 너무 빨라서 로드 XX
        # selenium driver에서 바로 속성 가져오지 않는 이유: 일단 변수로 넣고 src 속성가져오는게 더 빠름
        src = preview_image.get_attribute('src')
        if idx >= image_num:
            break
        elif 'http' in src:
            idx += 1
            url_req.urlretrieve(src, 'img_day01_hw/크롬_' + str(idx) + '.jpg')

    print('saved file:', idx)


def crawling(image_num):
    image_list = driver.find_elements_by_css_selector('#islrg > div.islrc a .rg_i.Q4LuWd')
    get_image_urls(image_list, image_num)

    print('end')


crawling(20)

driver.quit()
