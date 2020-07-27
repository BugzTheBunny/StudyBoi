import os

# Headers
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
    'dnt': '1',
    'referer': 'https',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
}

auth_token = os.environ['AUTH_TOKEN']

udemy_headers = {
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

# Real.discount search parameters

search_url = 'https://www.real.discount/search-page/?keyword='
pu1 = 'https://www.real.discount/search-page/page/'
pu2 = '/?keyword='

bot_token = os.environ['BOT_TOKEN']

info_string = 'קוראים לי StudyBoi, ואני מספק לכם קורסים בחינם\n' \
              'הקורסים לקוחים מUdemy ואתר קמפוס.\n' \
              'הקורסים חינם לגמריי, כל הנדרש זה להרשם באתרים האלו ולהנות!\n' \
              'ליצירת קשר - https://www.facebook.com/SlavaBugzBunny'

fb_info_string = 'קוראים לי StudyBoi,\n ואני מספק לכם קורסים בחינם\n' \
                 'הקורסים לקוחים מUdemy ואתר קמפוס.\n' \
                 'הקורסים חינם לגמריי, כל הנדרש זה להרשם באתרים האלו ולהנות!\n' \
                 'ליצירת קשר - https://www.facebook.com/SlavaBugzBunny'

start_string = """
            ברוכים הבאים לStudyBoi הבוט שיעזור לכם ללמוד מה שאתם רוצים, ובחינם.
            כדי למצוא קורס פשוט תקלידו את התחום שאותו אתם רוצים ללמוד.
            או תעזרו באחת האפשרויות המובנות.
            *כל הקורסים לגמריי בחינם*
            למידע - info/
            """

fb_help_string = '''
*חיפוש*\n פשוט תכתבו את שם הנושא שאתם רוצים.             
            '''

help_string = '''
חיפוש רגיל - פשוט תכתבו את שם הנושא שאתם רוצים ללמוד, ותקבלו קורסים בשבילו.             
            אפשרויות מובנות: 
כדי לקבל הקורסים הכי טובים, תכתבו "_adv/"  ולאחר מכן את שם הנושא.             
דוגמא:             
             /adv_python
כדי לקבל קורסים בעברית, תכתבו "heb/".             

                בשביל חיפוש חופשי אין צורך להשתמש ב"/"
            '''

fb_copyright_string = 'כל הזכויות שמורות ליוצרי הקורסים, אין לכותב הבוט שום קשר ליצירת הקורסים עצמם' \
                      'או ליצירת הפלטפורמוט, יוצר הבוט רק מפנה את המשתמש לקורסים שאותם הוא מבקש.' \
                      '\n' \
                      '======================' \
                      '\n' \
                      'כל הקורסים שאפשר לקבל מהבוט שייכים ב100% לUdemy או לcampus.gov.il' \
                      '\n' \
                      '======================' \
                      '\n' \
                      'יוצר הבוט לא מרוויח מבחינה כלכלית בשום צורה.'

copyright_string = 'כל הזכויות שמורות ליוצרי הקורסים, אין לכותב הבוט שום קשר ליצירת הקורסים עצמם' \
                   'או ליצירת הפלטפורמוט, יוצר הבוט רק מפנה את המשתמש לקורסים שאותם הוא מבקש.' \
                   '\n' \
                   '======================' \
                   '\n' \
                   'כל הקורסים שאפשר לקבל מהבוט שייכים ב100% לUdemy או לcampus.gov.il' \
                   '\n' \
                   '======================' \
                   '\n' \
                   'יוצר הבוט לא מרוויח מבחינה כלכלית בשום צורה.'

fb_contact_string = 'מוזמנים ליצור קשר איתו: https://www.facebook.com/SlavaBugzBunny'

contact_string = 'מוזמנים ליצור קשר ב - https://www.facebook.com/SlavaBugzBunny'
