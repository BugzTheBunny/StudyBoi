import requests
from bs4 import BeautifulSoup
import parameters
import parse

class Data:

    def __init__(self,pages):
        self.name = pages

def get_pages(url,query):
    links_list=[]
    links_list.append(url)
    try:
        res = requests.get(url,headers=parameters.headers)
        res = res.text
        data = BeautifulSoup(res, 'lxml')
        workbox = data.find('div', class_='col-sm-9')
        pages = workbox.find('ul', class_='pagination').find_all('li')
        pages_amount = int(pages[-1].text)
        for i in range(pages_amount):
            if i >= 2:
                links_list.append('https://www.real.discount/search-page/page/' + str(i) + '/?keyword=' + query)
    except:
        print('Could not get')
    return links_list

def search(query):
    query = query.lower()
    print(query)
    i = 0
    page_num = 0
    print('Searching for "' + query.lower() + '" .....:')
    EXPIRED = False
    LINKS = []
    pages = get_pages(parameters.search_url + str(query),query)
    print(f'Found {len(pages)} pages to parse.')
    for page in pages:
        if page_num <= 19:
            try:
                page_num = page_num + 1
                print(f'Crawling page number {page_num} > {page}')
                response = requests.get(page, headers=parameters.headers, timeout=3)
                response = response.text
                data = BeautifulSoup(response, 'lxml')
                workbox = data.find('div', class_='col-sm-9')
                boxes = workbox.find_all('div', class_='col-sm-4 masonry-item')
                name_box = workbox.find_all('')
                for box in boxes:
                    check_expired = box.find_all('img')
                    for each in check_expired:
                        try:
                            if 'expired' in check_expired[-1]['src']:
                                EXPIRED = True
                        except:
                            continue
                        if EXPIRED == False:
                            h4 = box.find('h4').text
                            h4 = h4.replace('  ... .... ..... ... .. ...  . .. . . . . .. .. . . . .', '')
                            h4 = h4.lower()
                            if box.find('a')['href'] not in LINKS:
                                if query in h4:
                                    LINKS.append(box.find('a')['href'])
                                    par = box.find('a')['href']
                                    i = i + 1
                                    print(f'Found a link. - Request - {query}, course: {h4}')
                                if i == 5:
                                    return LINKS
                        EXPIRED = False
            except:
                print('Could not retrieve DATA')

    print(len(LINKS))
    return LINKS
