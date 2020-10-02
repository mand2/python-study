"""
`scrapping`한 기사 `excel`로 저장하기, 메일 보내기
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
ws1.title = 'articles'
ws1.append(['제목', '링크', '신문사', '썸네일'])

# 기사 블럭으로 블럭별 대표기사 제목/url/언론사
article_block = soup.select('#main_pack > div > ul > li')

for article in article_block:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text
    thumb_img = article.select_one('div.thumb > a.sp_thmb > img')['src']

    ws1.append([title, url, company[:len(company) - 6], thumb_img])

driver.quit()

wb.save(filename='articles_1002_hw.xlsx')


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from sparta_py_basic.d02.secret_keys import sender, email_receiver


# 보내는 사람 정보
me = sender['email']
my_password = sender['pw']

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
email_list = email_receiver

for you in email_list:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[긴급] 트럼프 코로나 확진'
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = '도널드 트럼프 미 대통령이 <strong>오늘 10.02</strong> 코로나에 확진되었다고 한다.'
    content_txt = MIMEText(content, 'html')  # 메일 내용을 html 태그 형태로 변환
    msg.attach(content_txt)  # 메세지에 추가

    # 첨부파일 만들기
    attachment = MIMEBase('application', 'octet-stream')
    with open('articles_1002_hw.xlsx', 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='추석기사_1002.xlsx')
    msg.attach(attachment)   # 메세지에 추가

    # 메일 보내기
    s.sendmail(me, you, msg.as_string())

s.quit()

