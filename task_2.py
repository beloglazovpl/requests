import requests

from test import YandexDisk

from pprint import pprint

TOKEN = ''


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk('text.txt', 'text.txt')
