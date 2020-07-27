import requests
from parameters import bot_token


def send_message(chat_id, text):
    """
    This is handling the message sending.
    :param chat_id: -> the Chat id.
    :param text: -> The text you want to send to the user.
    :return:
    """
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r


def parse_telegram_message(message):
    """
    This function takes the important things from the message, and returns a proper message.
    :param message:
    :return:
    """
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    msg_id = message['message']['message_id']
    name = message['message']['chat']['first_name']
    delete_message(chat_id, msg_id)
    m = {
        'chat_id': chat_id,
        'message_id': msg_id,
        'text': text,
        'name': name
    }
    return m


def delete_message(chat_id, msg_id):
    """
    Deletes the message
    :param chat_id: - The id of the user chat
    :param msg_id: - the message id
    :return:
    """
    try:
        url = f'https://api.telegram.org/bot{bot_token}/deleteMessage'
        payload = {'chat_id': chat_id, 'message_id': msg_id}
        r = requests.delete(url, json=payload)
    except:
        pass