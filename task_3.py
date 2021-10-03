import requests

from datetime import datetime
import time

from pprint import pprint


page = 1
tag = 'python'
today_format = str(datetime.today())
today = int(time.mktime(datetime.strptime(today_format, '%Y-%m-%d %H:%M:%S.%f').timetuple()))
two_day_ago = today - 2*86400


def make_json():
    url = f'https://api.stackexchange.com//2.3/search?page={page}&pagesize=100&fromdate={two_day_ago}&todate={today}&order=desc&sort=activity&tagged={tag}&site=stackoverflow&filter=!nKzQUR693x'
    response = requests.get(url=url).json()
    return response


quantity_links = make_json()['total']
count = 0
while count != quantity_links:
    items = make_json()['items']
    for article in items:
        links = article['link']
        count += 1
        pprint(links)
        with open('task_3.txt', 'a') as file:
            file.write(f'{links}\n')
    page += 1
print(f'За 2 дня создано {count} вопросов с тегом {tag}')
