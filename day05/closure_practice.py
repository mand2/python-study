"""
practice the Closure: make encapsulation
ref: http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/
"""


# 1.
def get_better(msg):
    def feelings():
        print(msg)
    feelings()


get_better('I feel better than before')


# 2.
def make_tags(tag):
    text = '가나다라마바사'
    tag = tag

    def inner_func():
        print('<{0}>{1}<{0}>'.format(tag, text))
    return inner_func


li_tag = make_tags('li')
b_tag = make_tags('b')

li_tag()  # <li>가나다라마바사<li>
b_tag()  # <b>가나다라마바사<b>


# 3. make more encapsulation of #2
def make_notice(tag):

    def make_message(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))
    return make_message


h2_tag = make_notice('h2')
h2_tag('Welcome to our App!')
paragraph = make_notice('p')
paragraph('If you want to start, press [Enter] and wait for a second ✨')

# result:
# <h2>Welcome to our App!<h2>
# <p>If you want to start, press [Enter] and wait for a second ✨<p>


"""
conclusion :
슬랙 app 커스터마이징하려고 할 때 본 형식 중 하나. 
메세지까지 커스터마이징하려면 이런 형식으로 해야하던데.. 
이걸 참고해서 slack app 을 만들면 좋을 거 같음.  
"""
