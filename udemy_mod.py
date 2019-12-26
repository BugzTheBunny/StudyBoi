#Date created - 22/12/19
#Author - Slava Kutuzov
# Udemy API Module.
# API Overview = https://www.udemy.com/developers/affiliate/

import requests
import os

auth_token = os.environ['AUTH_TOKEN']

headers = {
    "Accept": "application/json, text/plain, */*",
  	"Authorization": f"{auth_token}",
  	"Content-Type": "application/json;charset=utf-8",
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36',
}

def get_courses(query):
    course_list = []
    try:
        response = requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size=10&search={query}&price=price-free&ratings=4.2',
            headers=headers)
        data = response.json()
        data = data['results']
        for c in data:
            course_list.append({
                'name': c['title'],
                'url': c['url'],
                'price': c['price'],
                'headline':c['headline']
            })
    except:
        return course_list
    return course_list

def get_heb_courses():
    course_list = []
    try:
        response = requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size=100&language=he',
            headers=headers)
        data = response.json()
        data = data['results']
        for c in data:
            course_list.append({
                'name': c['title'],
                'url': c['url'],
                'price': c['price'],
                'headline':c['headline']
            })
    except:
        return course_list
    return course_list

def get_best_courses(query):
    course_list = []
    try:
        response = requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size=10&search={query}&price=price-free&ordering=most-reviewed',
            headers=headers)
        data = response.json()
        data = data['results']
        for c in data:
            course_list.append({
                'name': c['title'],
                'url': c['url'],
                'price': c['price'],
                'headline':c['headline']
            })
    except:
        return course_list
    return course_list




