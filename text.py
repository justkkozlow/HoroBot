from datetime import datetime

SIGN_DICT = {
    'aries': 'Овен',
    'taurus': 'Телец',
    'gemini': 'Близнецы',
    'cancer': 'Рак',
    'leo': 'Лев',
    'virgo': 'Дева',
    'libra': 'Весы',
    'scorpio': 'Скорпион',
    'sagittarius': 'Стрелец',
    'capricorn': 'Козерог',
    'aquarius': 'Водолей',
    'pisces': 'Рыбы'
}

date_now = datetime.now().strftime("%d.%m.%Y")

today = f'Гороскоп для всех знаков на 🗓 {date_now}'
choose_sign = 'Хотите посмотреть гороскоп для конкретного знака зодиака❓'

sign = f'Гороскоп на {date_now}: '
