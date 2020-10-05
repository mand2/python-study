"""
카카오톡 채팅내용으로 워드클라우드 만들기 - 2
데이터 클렌징
"""

from wordcloud import WordCloud
from sparta_py_basic.d02.secret_keys import my_font
from sparta_py_basic.d03.wordcloud_03 import read_kakao_chat

from PIL import Image
import numpy as np


def generate_word_cloud():
    kakao_txt = read_kakao_chat()

    mask = np.array(Image.open('cloud.png'))
    wc = WordCloud(font_path=my_font, background_color='white', mask=mask)
    wc.generate(kakao_txt)
    wc.to_file("result_masked.png")


generate_word_cloud()
