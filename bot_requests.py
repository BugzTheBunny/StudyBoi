# Extractors
from extractors import udemy_mod
from extractors import campus_il_mod

# System
from system.description_strings import *
from telegram_handling.telegram_system import *
from facebook_handling.facebook_system import *
from langdetect import detect


# Telegram Campus searching
def telegram_campus_search(chat_id, input):
    """
    :param chat_id: - The chat id of the user - bot
    :param input: - the user input for searching
    """
    send_message(chat_id, f" מחפש קורסים עבור-{input}")
    courses = campus_il_mod.campus_get_courses_by_input(input)
    if len(courses) > 100:  # if there are more than 100 courses found, there are no courses found
        send_message(chat_id, 'לא נמצאו קורסים בנושא זה')
    else:
        send = ''
        for course in courses:
            new_course_name = f'💎 שם הקורס: {course.title}'
            new_course_duration = f'⏰ משך הקורס: {course.duration}'
            new_course_link = f'🌐 קישור לקורס: {course.link}'
            new_course_description = f'🧾 כמה מילים: {course.description}'
            send = send + '\n' + '🧙\u200d♂•••••••••••••••••••••••••••••••••••••••••••••🧙\u200d♂' \
                   + new_course_name + '\n\n' \
                   + new_course_description + '\n\n' \
                   + new_course_duration + '\n\n' \
                   + new_course_link + '\n\n'
        send = send + '🧙\u200d♂•••••••••••••••••••••••••••••••••••••••••••••🧙\u200d♂'
        send_message(chat_id, send)


# Facebook campus searching
def facebook_campus_search(chat_id, input):
    fb_send_message(chat_id, f" מחפש קורסים עבור - {input}")
    courses = campus_il_mod.campus_get_courses_by_input(input)
    if len(courses) > 100:  # if there are more than 100 courses found, there are no courses found
        fb_send_message(chat_id, "אין קורסים בנושא זה😥")
    else:
        send = ''
        count = 0
        for course in courses:
            count = count + 1
            new_course_name = f'💎 *שם הקורס:*\n {course.title}'
            new_course_duration = f'⏰ *משך הקורס:*\n{course.duration}'
            new_course_link = f'🌐 *קישור לקורס:* {course.link}'
            send = '\n' + '🧙\u200d♂••••••••••••••••••••🧙\u200d♂' \
                   + '' + new_course_name + '\n' \
                   + '' + new_course_duration + '\n' \
                   + '' + new_course_link + '\n'
            send = send + '🧙\u200d♂••••••••••••••••••••🧙\u200d♂'
            if count <= 5:
                fb_send_message(chat_id, send)


# Facebook Udemy Searching
def facebook_udemy_search(chat_id, input):
    fb_send_message(chat_id, f" מחפש קורסים עבור - {input}")
    courses = udemy_mod.udemy_get_courses_by_input(input)
    if len(courses) is 0:
        fb_send_message(chat_id, "אין קורסים בנושא זה😥")
    else:
        count = 0
        for course in courses:
            count = count + 1
            new_course_name = f'💎 *שם הקורס:* '
            new_course_link = f'🌐 *קישור לקורס:* '
            send = '\n' + '🧙\u200d♂••••••••••••••••••••🧙\u200d♂\n' \
                   + new_course_name + f'\n{course.title}\n' \
                   + new_course_link + f'\n www.udemy.com{course.link}\n' \
                   + '🧙\u200d♂••••••••••••••••••••🧙\u200d♂\n'
            if count <= 5:
                fb_send_message(chat_id, send)


# Telegram Udemy searching
def telegram_udemy_search(chat_id, input):
    send_message(chat_id, f" מחפש קורסים עבור-{input}")
    courses = udemy_mod.udemy_get_courses_by_input(input)
    if len(courses) == 0:  # if there are more than 100 courses found, there are no courses found
        send_message(chat_id, 'לא נמצאו קורסים בנושא זה')
    else:
        send = ''
        for course in courses:
            new_course_name = f'💎 שם הקורס: '
            new_course_price = f'⏰ מחיר הקורס: '
            new_course_link = f'🌐 קישור לקורס: '
            new_course_description = f'💡 כמה מילים: '
            send = send + '\n' + '🧙\u200d♂•••••••••••••••••••••••••••••••••••••••••••••🧙\u200d♂\n' \
                   + new_course_name + f'\n\n•{course.title}\n' \
                   + new_course_description + f'\n•{course.description}\n' \
                   + new_course_price + f'\n•{course.price}\n' \
                   + new_course_link + f'\n• www.udemy.com{course.link}\n'
        send = send + '🧙\u200d♂•••••••••••••••••••••••••••••••••••••••••••••🧙\u200d♂'
        send_message(chat_id, send)


# Facebook info commands
def delegate_to_facebook_info_commands(chat_id, user_input):
    """
    This function should manage informative functions.
    :param chat_id:
    :param input:
    :return:
    """
    # Informative functions
    copyright = lambda user_input: fb_send_message(chat_id, fb_copyright_string) if 'copyright' in user_input else None
    contact = lambda user_input: fb_send_message(chat_id, fb_contact_string) if 'contact' in user_input else None
    help = lambda user_input: fb_send_message(chat_id, fb_help_string) if 'help' in user_input else None
    info = lambda user_input: fb_send_message(chat_id, fb_info_string) if 'info' in user_input else None
    try:
        # Will turn on the current function.
        copyright(user_input)
        contact(user_input)
        help(user_input)
        info(user_input)
    except:
        fb_send_message(chat_id, 'קרתה שגיאה לא ברורה, תנסו שוב :)')


# Telegram info commands
def delegate_to_telegram_info_commands(chat_id, user_input):
    """
    This function should manage informative functions.
    :param chat_id:
    :param user_input:
    :return:
    """
    # Informative functions
    copyright = lambda user_input: send_message(chat_id, copyright_string) if '/copyright' in user_input else None
    contact = lambda user_input: send_message(chat_id, contact_string) if '/contact' in user_input else None
    help = lambda user_input: send_message(chat_id, help_string) if '/help' in user_input else None
    info = lambda user_input: send_message(chat_id, info_string) if '/info' in user_input else None
    start = lambda user_input: send_message(chat_id, start_string) if '/start' in user_input else None

    try:
        # Will turn on the current function.
        copyright(user_input)
        contact(user_input)
        help(user_input)
        info(user_input)
        start(user_input)
    except:
        send_message(chat_id, 'קרתה שגיאה לא ברורה, תנסו שוב :)')


# Facebook input handling
def delegate_facebook_input(message):
    known_commands = [
        'copyrights',
        'contact',
        'help',
        'info',
        'start']

    input = message['text']
    chat_id = message['chat_id']

    """
    :param chat_id: - The chat id number (bot - user)
    :param input: - the users input
    :return:
    """
    input = input.lower()  # Lowering the input for easy use, and to save further errors..
    # Checking for hebrew content
    hebrew = False
    try:
        if type(input) is str and detect(input) == 'he':
            hebrew = True
    except:
        pass
    '''
    informative functions (They all should return strings.
    '''
    if input in known_commands:
        delegate_to_facebook_info_commands(chat_id, input)
    """
    Hebrew search, in campus.gov
    """
    if hebrew is True:
        try:
            facebook_campus_search(chat_id, input)
        except:
            pass
    elif not hebrew and input not in known_commands:
        try:
            facebook_udemy_search(chat_id, input)
        except:
            pass


# Telegram input handling
def delegate_telegram_input(message):
    known_commands = ['/copyrights', '/contact', '/help', '/info', '/start']
    user_input = message['text']
    chat_id = message['chat_id']
    message_id = message['message_id']

    """
    :param chat_id: - The chat id number (bot - user)
    :param input: - the users input
    :return:
    """
    user_input = user_input.lower()  # Lowering the input for easy use, and to save further errors..

    # Checking for hebrew content
    hebrew = False
    try:
        if type(user_input) is str and detect(user_input) == 'he':
            hebrew = True
    except:
        pass
    '''
    informative functions (They all should return strings.
    '''
    if user_input in known_commands:
        delegate_to_telegram_info_commands(chat_id, user_input)
    """
    Hebrew search, in campus.gov
    """
    if hebrew is True:
        try:
            telegram_campus_search(chat_id, user_input)
        except:
            pass
    elif not hebrew and user_input not in known_commands:
        try:
            telegram_udemy_search(chat_id, user_input)
        except:
            pass
