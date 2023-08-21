from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

signs_btn = [
    [InlineKeyboardButton(text='♈ Овен', callback_data='aries'),
     InlineKeyboardButton(text='♉ Телец', callback_data='taurus'),
     InlineKeyboardButton(text='♊ Близнецы', callback_data='gemini')],
    [InlineKeyboardButton(text='♋ Рак', callback_data='cancer'),
     InlineKeyboardButton(text='♌ Лев', callback_data='leo'),
     InlineKeyboardButton(text='♍ Дева', callback_data='virgo')],
    [InlineKeyboardButton(text='♎ Весы', callback_data='libra'),
     InlineKeyboardButton(text='♏ Скорпион', callback_data='scorpio'),
     InlineKeyboardButton(text='♐ Стрелец', callback_data='sagittarius')],
    [InlineKeyboardButton(text='♑ Козерог', callback_data='capricorn'),
     InlineKeyboardButton(text='♒ Водолей', callback_data='aquarius'),
     InlineKeyboardButton(text='♓ Рыбы', callback_data='pisces')]
]

signs_btn = InlineKeyboardMarkup(inline_keyboard=signs_btn)

date_btn = [
    [InlineKeyboardButton(text='Вчера', callback_data='yesterday'),
     InlineKeyboardButton(text='Сегодня', callback_data='today')],
    [InlineKeyboardButton(text='Завтра', callback_data='tomorrow'),
     InlineKeyboardButton(text='Неделя', callback_data='week')],
    [InlineKeyboardButton(text='Месяц', callback_data='month'),
     InlineKeyboardButton(text='Год', callback_data='year')],

    [InlineKeyboardButton(text='Подписаться', callback_data='subscribe')]
]

date_btn = InlineKeyboardMarkup(inline_keyboard=date_btn)
