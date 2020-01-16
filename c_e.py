import requests
from bs4 import BeautifulSoup
from parameters import *


class Course:

    def __init__(self, title,duration,link,description):
        self.title = title
        self.duration = duration
        self.link = link
        self.description = description


def fetch_course_list():
    title = ''
    link = ''
    duration = ''
    description = ''
    courses_list = []
    try:
        response = requests.get('https://campus.gov.il/course/', headers=headers)
        response = response.text
        data = BeautifulSoup(response, 'lxml')
        courses = data.find_all('div',class_='more-courses-item-inner course-item-courses')
        for c in courses:
            # Databox:
            details = c.find('a',class_='course-details-more-courses course-details link-more-courses')
            # >> Title
            try:
                title = details.find('h5').text
            except:
                title = ''
                print('Could not retrive title')
            # >> Duration
            try:
                duration = details.find('div',class_='duration-single-course duration--more-courses')
                duration = duration.text.replace('|','-')
            except:
                duration = ''
                print('Could not get duration')
            # >> Course URL
            try:
                link = details['href']
            except:
                link = ''
                print('Could not retrieve link.')
            # >> Course description
            try:
                description = details.find('p',class_='org-course-front').text
            except:
                description = ''
                print('Could not retrieve description')
            # Building class.
            course = Course(title,duration,link,description)
            courses_list.append(course)
    except:
        print('Something went wrong')
    return courses_list


def fetch_course_list_by_input(input):
    title = ''
    link = ''
    duration = ''
    description = ''
    courses_list = []
    try:
        response = requests.get(f'https://campus.gov.il/?s={input}', headers=headers)
        response = response.text
        data = BeautifulSoup(response, 'lxml')
        courses = data.find_all('div',class_='more-courses-item-inner course-item-courses')
        for c in courses:
            # Databox:
            details = c.find('a',class_='course-details-more-courses course-details link-more-courses')
            # >> Title
            try:
                title = details.find('h5').text
            except:
                title = ''
                print('Could not retrive title')
            # >> Duration
            try:
                duration = details.find('div',class_='duration-single-course duration--more-courses')
                duration = duration.text.replace('|','-')
            except:
                duration = ''
                print('Could not get duration')
            # >> Course URL
            try:
                link = details['href']
            except:
                link = ''
                print('Could not retrieve link.')
            # >> Course description
            try:
                description = details.find('p',class_='org-course-front').text
            except:
                description = ''
                print('Could not retrieve description')
            # Building class.
            course = Course(title,duration,link,description)
            courses_list.append(course)
    except:
        print('Something went wrong')
    return courses_list


# list = fetch_course_list()
#
# for l in list:
#     print('====================================')
#     print(l.title)
#     print(l.duration)
#     print(l.link)
#     print(l.description)
