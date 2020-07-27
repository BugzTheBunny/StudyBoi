import requests
from bs4 import BeautifulSoup
from parameters import *


class Course:

    def __init__(self, title, duration, link, description):
        self.title = title
        self.duration = duration
        self.link = link
        self.description = description


def parse_course(url):
    try:
        response = requests.get(url, headers=headers)
        response = response.text
        data = BeautifulSoup(response, 'lxml')
        workbox = data.find('div',class_='wrap-info-single-course-inner')
        inner_workbox = workbox.find('div',class_='content-info-wrap')
        for field in inner_workbox:
            try:
                spans = field.find_all('span')
                print(f"{spans[0].text}{spans[1].text.replace('  ','').replace('', '')}")
                print('_____________________')

            except:
                pass
    except:
        print('a')