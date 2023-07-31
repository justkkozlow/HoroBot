import requests
from bs4 import BeautifulSoup as Bs

import text


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
        return self.get_horoscope()


def main_message():
    parser = HoroscopeParser()
    horoscope_links = parser.get_horoscope()
    return '\n\n'.join([f'{text.today}\n\n{item.text}\n{text.choose_sign}' for item in horoscope_links])


def sign_message(callback):
    parser = HoroscopeParser()
    horoscope_links = parser.get_horoscope_with_url(additional_url=f'{callback.data}')
    sign_value = text.SIGN_DICT.get(callback.data)
    return '\n\n'.join([f'{text.sign}{sign_value}\n\n{item.text}\n' for item in horoscope_links])
