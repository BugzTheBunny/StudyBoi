from pymessenger.bot import Bot
import parameters
from flask import request

bot = Bot(parameters.fb_access_token)


def fb_send_message(chat_id, response):
    """
    Sending the response to the user.
    :param recipient_id: - The sender id.
    :param response: - The thing that will be sent to the user.
    :return:
    """
    bot.send_text_message(chat_id, response)
    return "success"


def verify_fb_token(token_sent):
    """
    facebook token verification, the token is set in facebook itself.
    :param token_sent: -> Should be sent by itself, will be verified
    :return:
    """
    if token_sent == parameters.fb_vefiry_token:
        print(f'Token = {token_sent} Correct token')
        return request.args.get("hub.challenge")
    else:
        print(f'Token = {token_sent} - Wrong Token')
        return 'Invalid verification token'


def parse_facebook_message(message):
    """
    This function takes the important things from the message, and returns a proper message.
    :param message:
    :return:
    """
    msg = message['entry']
    for a in msg:
        messaging = a['messaging']
        for message in messaging:
            if message.get('message'):
                chat_id = message['sender']['id']
                if message['message'].get('text'):
                    text = message['message'].get('text')
                    obj = {
                        'chat_id' : chat_id,
                        'text' : text
                    }
                    return obj
                elif message['message'].get('attachments'):
                    fb_send_message(chat_id, 'מה זה הניסיון הזה לעבוד עליי? אני צריך מילה!')
    return '200'
