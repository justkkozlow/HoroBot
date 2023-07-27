import requests
from bs4 import BeautifulSoup as Bs

from text import *

SIGN_LIST = ['aurus', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn',
        'aquarius', 'pisces']


class HoroscopeParser:
    def __init__(self):
        self.url = 'https://horo.mail.ru/prediction/'

    def get_horoscope(self):
        r = requests.get(self.url)
        soup = Bs(r.text, 'lxml')
        links = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
        return links

    def get_horoscope_with_url(self, additional_url):
        self.url += additional_url
        horoscope_links = self.get_horoscope()
        return horoscope_links


def main_message():
    parser = HoroscopeParser()
    horoscope_links = parser.get_horoscope()
    for item in horoscope_links:
        return f'{today}\n\n{item.text}\n{choose_sign}'


def sign_message(callback):
    parser = HoroscopeParser()
    horoscope_links = parser.get_horoscope_with_url(additional_url=f'{callback.data}')
    for item in horoscope_links:
        return f'{sign}{callback.data}\n\n{item.text}\n'
