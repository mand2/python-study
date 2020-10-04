"""
카카오톡 채팅내용으로 워드클라우드 만들기 - 2
데이터 클렌징
"""

from sparta_py_basic.d02.secret_keys import chat_names


def read_kakao_chat():
    output = ''
    with open('bk_20201002.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '] [' in line:
                chat = replace_txt(line.split('] ')[2])
                output += chat

    return output


def replace_txt(txt):
    cleansed = txt.replace('삭제된 메시지입니다.\n', '') \
        .replace('이모티콘\n', '') \
        .replace('사진\n', '') \
        .replace('샵검색', '') \
        .replace('ㅋ', '') \
        .replace('ㅠ', '') \
        .replace('ㅜ', '') \
        .replace('ㅇ', '') \
        .replace('ㅎ', '') \
        .replace('ㄷ', '')

    for chat_name in chat_names:
        if chat_name in cleansed:
            cleansed = cleansed.replace(chat_name, '')

    return cleansed

