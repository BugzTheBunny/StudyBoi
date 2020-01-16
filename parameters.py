#Headers
import os

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

#Real.discount search parameters

search_url = 'https://www.real.discount/search-page/?keyword='
pu1 = 'https://www.real.discount/search-page/page/'
pu2 = '/?keyword='

bot_token = os.environ['BOT_TOKEN']




