#Date created - 22/12/19
#Author - Slava Kutuzov
# Udemy API Module.
# API Overview = https://www.udemy.com/developers/affiliate/

import requests
import os
from parameters import *


def get_courses(query):
    course_list = []
    try:
        response = requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size=10&search={query}&price=price-free&ratings=4.2',
            headers=udemy_headers)
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
            f'https://www.udemy.com/api-2.0/courses/?page_size=10&search='
            f'{query}&price=price-free&ordering=most-reviewed',
            headers=udemy_headers)
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




