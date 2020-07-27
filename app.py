from bot_requests import delegate_telegram_input
from telegram_handling.telegram_system import parse_telegram_message

# Flask
from flask import Flask
from flask import request
from flask import Response
from flask_sslify import SSLify

# System

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    handling a request from telegram (the user input)
    :return:
    """
    if request.method == 'POST':
        try:
            hebrew = False
            try:
                message = format_message(request.get_json())
            except:
                pass
            return Response('Ok', status=200)
        except Exception as e:
            print(f'Unknown error\n {e}')
            Response('Ok', status=200)
        return Response('Ok', status=200)


def format_message(request_message):
    """
    Formating the message - delegating from which platform the message was send, and handling it.
    :param request_message:
    :return:
    """
    # print(request_message)
    message_first_keys = request_message.keys()
    # -----------# Handling telegram call----------------------------------------
    if 'update_id' in message_first_keys:
        message = parse_telegram_message(request_message)
        message_type = 'telegram'
        delegate_telegram_input(message)
        return Response('Ok', status=200)


def main():
    pass


if __name__ == '__main__':
    main()
    app.run(debug=False)
