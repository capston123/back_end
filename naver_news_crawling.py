"""
기본적으로 이미지 가지고 올 경우 가져온 이미지로 하되
이미지가 없거나 동영상 같은 경우는 신문사 로고로 대체
"""


import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contents.settings")
django.setup()

from selenium import webdriver
from news.models import News
from datetime import date

def head_line_news(news_category):
    li_list = driver.find_elements_by_css_selector(
        '#today_main_news > div.hdline_news > ul > li')

    for i in range(len(li_list)):
        li_list = driver.find_elements_by_css_selector(
            '#today_main_news > div.hdline_news > ul > li')

        url = li_list[i].find_element_by_css_selector(
            'a').get_attribute('href')

        handle_news(url)


def normal_news(news_category, str):

    head_url = news_category.find_element_by_css_selector(
        'a').get_attribute('href')

    handle_news(head_url)

    li_list = driver.find_elements_by_css_selector(
        '#section_' + str + ' > div.com_list > div > ul > li')

    for i in range(len(li_list)):
        li_list = driver.find_elements_by_css_selector(
            '#today_main_news > div.hdline_news > ul > li')

        url = li_list[i].find_element_by_css_selector(
            'a').get_attribute('href')

        handle_news(url)


def handle_news(url):

    driver.implicitly_wait(5)
    driver.get(url=url)

    news_title = driver.find_element_by_css_selector(
        '#articleTitle').text

    news_category = find_category(url)

    news_thumbnail = ''
    try:
        news_thumbnail = driver.find_element_by_class_name('end_photo_org').find_element_by_tag_name(
            'img').get_attribute('src')
    except:
        news_thumbnail = 'Video News'

    newspaper = driver.find_element_by_css_selector(
        '#articleBody > div.link_news > h3').text
    newspaper = newspaper.split(' ')[0]

    print("url : " + url + "\nnews_thumbnail : " + news_thumbnail + "\nnews_title : " +
          news_title + "\ncategory : " + news_category + "\nnewspaper : " + newspaper + "\n")

    driver.implicitly_wait(5)
    driver.get(url=URL_news_home)

    temp_data = []

    temp_data.append(url)
    temp_data.append(news_thumbnail)
    temp_data.append(news_title)
    temp_data.append(news_category)
    temp_data.append(newspaper)

    save_data.append(temp_data)


def find_category(url):
    if 'sid1=100' in url:
        return '정치'
    elif 'sid1=101' in url:
        return '경제'
    elif 'sid1=102' in url:
        return '사회'
    elif 'sid1=103' in url:
        return '생활/문화'
    elif 'sid1=104' in url:
        return '세계'
    elif 'sid1=105' in url:
        return 'IT/과학'
    else:
        return '기타'


# chrome 창 크기 조절
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

URL_news_home = 'https://news.naver.com/'
driver = webdriver.Chrome('chromedriver89', options=options)

# 응답 대기
driver.implicitly_wait(5)

# news home으로 이동
driver.get(url=URL_news_home)

save_data = []

# 헤드라인
head_line = driver.find_elements_by_css_selector(
    '#today_main_news > div.hdline_news')
head_line_news(head_line[0])

# 정치
politics = driver.find_elements_by_css_selector(
    '#section_politics > div.com_list')
normal_news(politics[0], 'politics')

# 경제
economy = driver.find_elements_by_css_selector(
    '#section_economy > div.com_list')
normal_news(economy[0], 'economy')

# 사회
society = driver.find_elements_by_css_selector(
    '#section_society > div.com_list')
normal_news(society[0], 'society')

# 생활/문화
life = driver.find_elements_by_css_selector(
    '#section_life > div.com_list')
normal_news(life[0], 'life')

# 세계
world = driver.find_elements_by_css_selector(
    '#section_world > div.com_list')
normal_news(world[0], 'world')

# IT/과학
it = driver.find_elements_by_css_selector(
    '#section_it > div.com_list')
normal_news(it[0], 'it')

print('---------------------------------')
for url, news_thumbnail, news_title, news_category, newspaper in save_data:
    obj = News(url=url, image=news_thumbnail, name=news_title,
               category=news_category, newspaper=newspaper)
    obj.save()

driver.close()
