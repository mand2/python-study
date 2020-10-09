"""
카카오톡 채팅내용으로 워드클라우드 만들기 - 3
데이터 클렌징 + 컬러 변경
컬러변경 참조 : https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32
"""

from wordcloud import WordCloud
from sparta_py_basic.d02.secret_keys import my_font, filter_str

from PIL import Image
import numpy as np


def read_kakao_chat(chat_file):
    chat = ''
    with open(chat_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '] [' in line:
                msg = replace_txt(line.split('] ')[2])
                chat += msg

    return chat


def replace_txt(txt):
    import re
    pattern = re.compile(filter_str)
    cleansed = pattern.sub('', txt, count=0)
    return cleansed


def get_color(word=None, font_size=None,
              position=None, orientation=None,
              font_path=None, random_state=None):
    colors = [[4, 77, 82],
              [25, 74, 85],
              [82, 43, 84],
              [158, 48, 79]]
    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])


def generate_word_cloud():
    kakao_txt = read_kakao_chat('bk_20201002.txt')

    mask = np.array(Image.open('cloud.png'))
    wc = WordCloud(font_path=my_font, background_color='white', mask=mask, random_state=42, color_func=get_color)
    wc.generate(kakao_txt)
    wc.to_file("result_masked_2.png")


generate_word_cloud()
