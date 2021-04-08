"""
1. 로그인(성인 인증)해야 내부 썸네일 크롤링 가능
    성인 웹툰은 어떻게 처리?
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contents.settings")
django.setup()
from webtoons.models import Daum

save_data = []
def daum_crawling(li_list, num):

    for i in range(len(li_list)):

        li_list = driver.find_elements_by_css_selector('#dayList' + str(num) +' > li')

        webtoon_title = li_list[i].find_element_by_css_selector(
            'a > img').get_attribute('alt')

        webtoon_url = li_list[i].find_element_by_css_selector(
            'a').get_attribute('href')

        webtoon_status = li_list[i].find_element_by_css_selector(
            'a > em').text

        webtoon_author = li_list[i].find_element_by_class_name('txt_info').text

        webtoon_thumbnail = li_list[i].find_element_by_css_selector(
            'a > img').get_attribute('src')

        driver.implicitly_wait(5)
        driver.get(url=webtoon_url)

        try: 
            webtoon_category = tmp = driver.find_element_by_css_selector(
                '#cSub > div.product_info > div > div > dl > dd').text
            webtoon_category = webtoon_category.replace(" ", '')

            li_list_webtoon = driver.find_elements_by_css_selector(
                '#episodeList > ul > li')

            recent_title = ''
            recent_thumbnail = ''
            recent_url = ''

            for j in range(len(li_list_webtoon)):

                li_list_webtoon = driver.find_elements_by_css_selector(
                    '#episodeList > ul > li')

                try:
                    li_list_webtoon[j].find_element_by_class_name('ico_preview')
                except NoSuchElementException:
                    recent_thumbnail = li_list_webtoon[j].find_element_by_css_selector(
                        'a > img').get_attribute('src')

                    recent_title = li_list_webtoon[j].find_element_by_css_selector(
                        'a > strong').text

                    recent_url = li_list_webtoon[j].find_element_by_css_selector(
                        'a').get_attribute('href')
                    break

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
        except :
            continue
        finally :            
            driver.implicitly_wait(5)
            driver.get(url=URL_webtoon_home)

def data_save():
    for name, url, image, category in save_data:
        obj = Daum(name=name, url=url, image=image, category=category)
        obj.save()

# chrome 창 크기 조절
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

URL_webtoon_home = 'http://webtoon.daum.net/'
driver = webdriver.Chrome('chromedriver89', options=options)

driver.implicitly_wait(5)
driver.get(url=URL_webtoon_home)

li_list_up = driver.find_elements_by_css_selector('#dayList1 > li')
li_list_down = driver.find_elements_by_css_selector('#dayList2 > li')

daum_crawling(li_list_up, 1)
daum_crawling(li_list_down, 2)

data_save()