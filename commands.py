import requests
from parameters import *


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
