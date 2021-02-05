"""
1. 클래스로 저장?
2. 23~24시 기준으로 업데이트 웹툰만 크롤링?
"""
import django
from datetime import date
from selenium import webdriver
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contents.settings")
django.setup()
from webtoons.models import Naver


save_data = []
today_date = date.today()

# chrome 창 크기 조절
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

URL_webtoon_home = 'https://comic.naver.com/webtoon/weekday.nhn'
driver = webdriver.Chrome('chromedriver87', options=options)

# 응답 대기
driver.implicitly_wait(5)

# webtoon home으로 이동
driver.get(url=URL_webtoon_home)

# li tag
li_list = driver.find_elements_by_css_selector(
    '#content > div.list_area.daily_all > div.col.col_selected > div > ul > li')
for i in range(5):

    # li tag
    li_list = driver.find_elements_by_css_selector(
        '#content > div.list_area.daily_all > div.col.col_selected > div > ul > li')

    # 웹툰 제목
    webtoon_title = li_list[i].text.replace(
        'NEW\n', '').replace('18세 이상 이용 가능\n', '').replace('컷툰\n', '')

    # 웹툰 url
    webtoon_url = li_list[i].find_element_by_css_selector(
        'div > a').get_attribute('href')

    # 웹툰 상태 ico_updt == 업데이트 완료
    webtoon_status = li_list[i].find_element_by_css_selector(
        'div > a > em').get_attribute('class')

    # 응답 대기
    driver.implicitly_wait(5)

    # 웹툰 url로 페이지 이동
    driver.get(url=webtoon_url)

    # 웹툰 작가
    webtoon_author = driver.find_element_by_css_selector(
        '#content > div.comicinfo > div.detail > h2')
    webtoon_author = webtoon_author.find_element_by_class_name('wrt_nm').text

    # 웹툰 썸네일
    webtoon_thumbnail = driver.find_element_by_css_selector(
        '#content > div.comicinfo > div.thumb > a > img').get_attribute('src')

    # 웹툰 카테고리
    webtoon_category = driver.find_element_by_css_selector(
        '#content > div.comicinfo > div.detail > p.detail_info > span.genre').text
    webtoon_category = webtoon_category.replace(" ", '')

    recent_thumbnail = ''
    recent_url = ''
    recent_title = ''
    try:
        # 웹툰 화별 썸네일
        recent_thumbnail = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(2) > td:nth-child(1) > a > img').get_attribute('src')

        # 웹툰 화별 url
        recent_url = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(2) > td.title > a').get_attribute('href')

        # 웹툰 화별 제목
        recent_title = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(2) > td.title > a').text
    except:
        # 웹툰 화별 썸네일
        recent_thumbnail = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(3) > td:nth-child(1) > a > img').get_attribute('src')

        # 웹툰 화별 url
        recent_url = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(3) > td.title > a').get_attribute('href')

        # 웹툰 화별 제목
        recent_title = driver.find_element_by_css_selector(
            '#content > table > tbody > tr:nth-child(3) > td.title > a').text

    print("제목 : " + webtoon_title +
          "\n작가 : " + webtoon_author +
          "\n카테고리 : " + webtoon_category +
          "\n업데이트 상태 : " + webtoon_status +
          "\n썸네일 : " + webtoon_thumbnail +
          "\nURL : " + webtoon_url +
          "\n최신 작품 제목 : " + recent_title +
          "\n최신 작품 썸네일 : " + recent_thumbnail +
          "\n최신 작품 URL : " + recent_url + "\n")

    temp_data = []

    temp_data.append(webtoon_title+' '+recent_title)
    temp_data.append(recent_url)
    temp_data.append(recent_thumbnail)
    temp_data.append(webtoon_category)

    save_data.append(temp_data)
    # 응답 대기
    driver.implicitly_wait(5)

    # webtoon home으로 이동
    driver.get(url=URL_webtoon_home)


for name, url, image, category in save_data:
    obj = Naver(name=name, url=url, image=image, category=category)
    obj.save()

driver.close()
