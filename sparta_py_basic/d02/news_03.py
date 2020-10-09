"""
`excel`로 저장된 `scrapping`한 기사 메일로 보내기
"""


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
    msg['Subject'] = '제목2'
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = '메일 내용'
    content_txt = MIMEText(content, 'plain')  # 메일 내용을 기본 txt 형태로 변환
    msg.attach(content_txt)  # 메세지에 추가

    # 첨부파일 만들기
    attachment = MIMEBase('application', 'octet-stream')
    with open('articles_1002.xlsx', 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='추석기사.xlsx')
    msg.attach(attachment)   # 메세지에 추가

    # 메일 보내기
    s.sendmail(me, you, msg.as_string())

s.quit()


