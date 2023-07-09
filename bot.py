import requests
from bs4 import BeautifulSoup as Bs

from text import *


def main_message():
    r = requests.get('https://horo.mail.ru/')
    soup = Bs(r.text, 'lxml')
    links = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for item in links:
        return f'{today}\n\n{item.text}\n{choose_sign}'


# def sign_list(callback):

    # sign = callback
    # url = 'https://horo.mail.ru/' + 'prediction/' + sign
    # r = requests.get('https://horo.mail.ru/')
    # soup = Bs(r.text, 'lxml')
    # links = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    # for item in links:
    #     callback = item.text

    #     urls_list = f'{r}{i["href"]}'
    #     clear_link = urls_list.replace('today/', '')
    #     # signs_urls.append(clear_link)

    # print(links)
    # return callback

# def content(callback):
#     """
#     Функция принимает выбранный знак зодиака,
#     находит, по ключу, ссылку на его страницу и возвращает текст
#
#     :param callback: полученное значение знака зодиака из функции sign_content
#     :return: Обработанный текст
#     """
#     sign_content = requests.get(sign_list(URL).setdefault(callback.data))
#     soup = Bs(sign_content.text, 'html.parser')
#     selected_sign = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
#     return ' '.join([s.text for s in selected_sign])
