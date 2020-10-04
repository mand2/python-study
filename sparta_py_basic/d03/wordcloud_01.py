"""
텍스트 파일 읽고 쓰기 / word cloud 용 고딕폰트 리스트 확인
"""


# 파일 쓰기
def write_file():
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write('각 줄마다 번호를 적은 파일입니다.\n')
        for i in range(5):
            f.write(f'이것은 {i+1}번째 줄입니다.\n')


def read_file():
    output = ''
    with open('test.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            output += line
    print(output)


def check_font_gothic():
    import matplotlib.font_manager as fm
    
    # 이용 가능한 폰트 중 '고딕'만 선별
    for font in fm.fontManager.ttflist:
        if 'Gothic' in font.name:
            print(font.name, font.fname)
    


