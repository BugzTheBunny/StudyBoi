# Author - Slava Bugz
# Late date updated - 4/1/2020

import json
from parameters import *
from udemy_mod import *
from commands import *
from description_strings import *

import os
import c_e

from langdetect import detect
from flask import Flask
from flask import request
from flask import Response


from flask_sslify import SSLify


#Built in commands.
built_in = ['/start', '/heb', '/info', '/help', '/copyright', '/contact']

app = Flask(__name__)
sslify = SSLify(app)

BANNED_LIST = ['311100878']

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        hebrew = False
        message = request.get_json()
        message = parse_message(message)
        chat_id = message['chat_id']
        input = message['text']
        chat_id = message['chat_id']
        message_id = message['message_id']
        delete_message(chat_id, message_id)
        if chat_id in BANNED_LIST:
            send_message(chat_id, 'לצערינו קרתה בעיה, צרו בבקשה קשר עם המפתח')
            return Response('Ok', status=200)
        try:
            if type(input) is str and detect(input) == 'he':
                hebrew = True
            if input == '/start':
                send_message(chat_id, start_string)
                return Response('Ok', status=200)
        except:
            pass
        ###################################################################################################
        # >> Hebrew courses.


        if input == '/heb':
            #send_message(chat_id, 'וואלה כמה שניות.....מחפש ב campus.gov.il')
            # courses = c_e.fetch_course_list()
            # amount = len(courses)
            # count = 0
            # string = ''
            # for c in courses:
            #     count = count + 1
            #     if c.duration == '':
            #         c.duration = "לא ידוע"
            #     if c.description == '':
            #         c.description = "לא ידוע"
            #     if count <= 6:
            #         course = f'שם הקורס:    {c.title}' \
            #                  f'\n משך הקורס:   {c.duration}' \
            #                  f'\n תיאור:   {c.description} ' \
            #                  f'\n קישור:   {c.link} ' \
            #                  f'\n ==================================\n '
            #
            #         string = str(string) + str(course)
            #         if count == 6:
            #             send_message(chat_id,str(string))
            #             string = ''
            #             count = 0
            #
            # send_message(chat_id, f'נמצאו {amount} קורסים.')
            send_message(chat_id, 'פונקציה זאת כרגע בתהליכי תיקון. - תנסו להשתמש במילות מפתח בעברית.')
            return Response('Ok', status=200)

        if input == '/info':
            send_message(chat_id, info_string)
            return Response('Ok', status=200)
        if input == '/help':
            send_message(chat_id, help_string)
            return Response('Ok', status=200)
        if '/adv_' in input:
            input = input.replace('/adv_', '')
            print(input)
            courses = get_best_courses(input)
            for c in courses:
                send_message(chat_id,
                             f'שם הקורס:\n {c["name"]} \n מחיר הקורס:\n {c["price"]}\n תיאור הקורס: \n{c["headline"]}'
                             f' \n קישור לקורס: \n {"https://www.udemy.com" + c["url"]}')
                return Response('Ok', status=200)
        # >> Copyrights
        if '/copyright' in input:
            send_message(chat_id,copyright_string)
            return Response('Ok', status=200)

        ###################################################################################################
        # >> Campus.gov.il Search
        if input not in built_in and hebrew :
            send_message(chat_id, f" מחפש קורסים עבור-{input}")
            courses = c_e.fetch_course_list_by_input(input)
            amount = len(courses)
            string = ''
            #If no hebrew courses on the subject
            if len(amount) >= 140:
                send_message(chat_id, 'לא נמצאו קורסים בנושא זה כרגע.')
                return Response('Ok', status=200)

            for c in courses:
                if c.duration == '':
                    c.duration = "לא ידוע"
                if c.description == '':
                    c.description = "לא ידוע"
                course = f'שם הקורס:    {c.title}' \
                         f'\n משך הקורס:   {c.duration}' \
                         f'\n תיאור:   {c.description} ' \
                         f'\n קישור:   {c.link} ' \
                         f'\n ==================================\n '

                string = str(string) + str(course)
            send_message(chat_id, f'נמצאו {amount} קורסים בנושא זה.')
            send_message(chat_id, str(string))
            return Response('Ok', status=200)
        ##############################################################################################
        # >> Udemy Search.
        if input not in built_in and not hebrew:
            send_message(chat_id, f" מחפש קורסים עבור-{input}")
            courses = get_courses(input)
            amount = len(courses)
            if len(courses) == 0:
                send_message(chat_id, 'לא נמצאו קורסים בנושא זה כרגע.')
                return Response('Ok', status=200)
            else:
                for c in courses:
                    send_message(chat_id,
                                 f'שם הקורס:\n {c["name"]} \n מחיר הקורס:\n {c["price"]}\n תיאור הקורס: \n{c["headline"]} \n'
                                 f' קישור לקורס: \n {"https://www.udemy.com" + c["url"]}')
            send_message(chat_id, f'אלו הם 10 הקורסים החינמיים הנבחרים ביותר ב{input} באתר של Udemy.')
            return Response('Ok', status=200)

def main():
    pass


if __name__ == '__main__':
    main()
    app.run(debug=True)


