"""
카카오톡 채팅내용으로 워드클라우드 만들기 - 1
데이터 클렌징을 안해서 이상한게 많음.
"""

from wordcloud import WordCloud
from sparta_py_basic.d02.secret_keys import my_font


def read_kakao_chat():
    output = ''
    with open('bk_20201002.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            output += line
    return output


kakao_txt = read_kakao_chat()
wc = WordCloud(font_path=my_font, background_color='white', width=600, height=400)
wc.generate(kakao_txt)
wc.to_file('result.png')
