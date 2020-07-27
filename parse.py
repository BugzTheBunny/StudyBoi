import requests
from bs4 import BeautifulSoup
import parameters

class Data:

    def __init__(self,NAME,IMAGE,PRICE,USERS,RATE,LINK):
        self.name = NAME
        self.image = IMAGE
        self.price = PRICE
        self.users = USERS
        self.rate = RATE
        self.link = LINK

    def __2str__(self):
        return 'Name: ' + self.name + '\nPrice: ' + self.price + '\nRate: ' + self.rate + '\nUsers: ' + self.users + '\nLink: ' + self.link

def parse_course(url):
    NAME = ''
    IMAGE = ''
    PRICE = ''
    USERS = ''
    RATE = ''
    LINK = ''
    try:
        response = requests.get(url, headers=parameters.headers)
        response = response.text
        data = BeautifulSoup(response, 'lxml')
        work_box = data.find('div',class_='col-sm-6 roundedtopright roundedtopleft roundedbottomleft roundedbottomright')
        work_box_a = work_box.find('div',class_='col-sm-12 roundedbottomleft roundedbottomright letshover')
        NAME = data.find('span', class_='breadcrumb_last').text
        IMAGE = work_box.find('img')['src']
        PRICE = work_box.find('h5',class_='price').text.split(' ')
        PRICE = PRICE[0]
        if PRICE == '$0.00':
            PRICE = 'FREE'
        details = work_box.find_all('div',class_='col-sm-3 col-xs-3')
        for detail in details:
            try:
                field = str(detail.find('i')['class'])
                if 'users' in field:
                    USERS = detail.text.replace(' ','').replace('\n','').replace('							','').replace('\t','')
                if 'star' in field:
                    RATE = detail.text.replace(' ','').replace('\n','').split('/')
                    RATE = RATE[0]
            except:
                continue
        LINK = work_box_a.find('a')['href']
    except:
        print('Could not parse')
    return Data(NAME,IMAGE,PRICE,USERS,RATE,LINK)
