# Author - Slava Bugz
# Late date updated - 31/12/2019

import json
from parameters import *
from udemy_mod import *
import os
import c_e

from flask import Flask
from flask import request
from flask import Response

from flask_sslify import SSLify

bot_token = os.environ['BOT_TOKEN']
built_in = ['/start', '/heb', '/info', '/help','/copyright']

app = Flask(__name__)
sslify = SSLify(app)


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    print(r.url)
    return r


def delete_message(chat_id, message_id):
    url = f'https://api.telegram.org/bot{bot_token}/deleteMessage'
    payload = {'chat_id': chat_id, 'message_id': message_id}
    r = requests.delete(url, json=payload)
    print(r.url)
    return r


def parse_message(message):
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    msg_id = message['message']['message_id']
    name = message['message']['chat']['first_name']
    m = {
        'chat_id': chat_id,
        'message_id': msg_id,
        'text': text,
        'name': name

    }
    print(m)
    return m


def wtj(fileName, data):
    filePathNameWExt = fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        message = parse_message(message)
        input = message['text']
        chat_id = message['chat_id']
        message_id = message['message_id']
        delete_message(chat_id,message_id)
        if input == '/start':
            send_message(chat_id, """
            ברוכים הבאים לStudyBoi הבוט שיעזור לכם ללמוד מה שאתם רוצים, ובחינם.
            כדי למצוא קורס פשוט תקלידו את התחום שאותו אתם רוצים ללמוד.
            או תעזרו באחת האפשרויות המובנות.
            *כל הקורסים לגמריי בחינם*
            למידע - info/
            """)
            return Response('Ok', status=200)
        #Hebrew courses.
        if input == '/heb':
             send_message(chat_id, 'וואלה כמה שניות.....מחפש ב campus.gov.il')
             courses = c_e.fetch_course_list()
             count = 0
             string = ''
             for c in courses:
                count = count + 1
                if c.duration == '':
                    c.duration = "לא ידוע"
                if c.description == '':
                    c.description = "לא ידוע"
                if count <= 6:
                    course = f'שם הקורס:    {c.title}' \
                             f'\n משך הקורס:   {c.duration}' \
                             f'\n תיאור:   {c.description} ' \
                             f'\n קישור:   {c.link} ' \
                             f'\n ==================================\n '
                    print(course)
                    string = str(string) + str(course)
                    if count == 6:
                        send_message(chat_id,str(string))
                        string = ''
                        count = 0
             print(string)
             return Response('Ok', status=200)

        if input == '/info':
            send_message(chat_id, '''
            למה הבוט הזה קיים?
            כדי לספק לכם לימודים בחינם, בכל תחום שתרצו.
            /copyright - זכויות יוצרים.
            /heb - קורסים בעברית - מביא כ140 קורסים בעברית.
            חיפוש מתקדם - _adv/
            דוגמא לחיפוש מתקדם - adv_python/
            ''')
            return Response('Ok', status=200)
        if input == '/help':
            send_message(chat_id, '''
חיפוש רגיל - פשוט תכתבו את שם הנושא שאתם רוצים ללמוד, ותקבלו קורסים בשבילו.
            אפשרויות מובנות: 
כדי לקבל הקורסים הכי טובים, תכתבו "_adv/"  ולאחר מכן את שם הנושא.
דוגמא:
/adv_python
כדי לקבל קורסים בעברית, תכתבו "heb/".
    
            ''')
            return Response('Ok', status=200)
        if '/adv_' in input:
            input = input.replace('/adv_', '')
            print(input)
            courses = get_best_courses(input)
            for c in courses:
                send_message(chat_id,
                             f'שם הקורס:\n {c["name"]} \n מחיר הקורס:\n {c["price"]}\n תיאור הקורס: \n{c["headline"]} \n קישור לקורס: \n {"https://www.udemy.com" + c["url"]}')
            return Response('Ok', status=200)
        # >> Copyrights
        if '/copyright' in input:
            send_message(chat_id,'כל הזכויות שמורות ליוצרי הקורסים, אין לכותב הבוט שום קשר ליצירת הקורסים עצמם'
                                 'או ליצירת הפלטפורמוט, יוצר הבוט רק מפנה את המשתמש לקורסים שאותם הוא מבקש.'
                                 'יוצר הבוט לא מרוויח מבחינה כלכלית בשום צורה.')
        if input not in built_in:
            send_message(chat_id, f" מחפש קורסים עבור-{input}")
            courses = get_courses(input)
            if len(courses) == 0:
                send_message(chat_id, 'לא נמצאו קורסים בנושא זה כרגע.')
                return Response('Ok', status=200)
            else:
                for c in courses:
                    send_message(chat_id,
                                 f'שם הקורס:\n {c["name"]} \n מחיר הקורס:\n {c["price"]}\n תיאור הקורס: \n{c["headline"]} \n קישור לקורס: \n {"https://www.udemy.com" + c["url"]}')
            return Response('Ok', status=200)
        return Response('Ok', status=200)
    else:
        return Response('Ok', status=200)


def main():
    pass


if __name__ == '__main__':
    main()
    app.run(debug=True)


