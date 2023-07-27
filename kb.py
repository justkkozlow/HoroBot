from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

signs_btn = [
    [InlineKeyboardButton('♈ Овен', callback_data='aries'),
     InlineKeyboardButton('♉ Телец', callback_data='taurus'),
     InlineKeyboardButton('♊ Близнецы', callback_data='gemini')],
    [InlineKeyboardButton('♋ Рак', callback_data='cancer'),
     InlineKeyboardButton('♌ Лев', callback_data='leo'),
     InlineKeyboardButton('♍ Дева', callback_data='virgo')],
    [InlineKeyboardButton('♎ Весы', callback_data='libra'),
     InlineKeyboardButton('♏ Скорпион', callback_data='scorpio'),
     InlineKeyboardButton('♐ Стрелец', callback_data='sagittarius')],
    [InlineKeyboardButton('♑ Козерог', callback_data='capricorn'),
     InlineKeyboardButton('♒ Водолей', callback_data='aquarius'),
     InlineKeyboardButton('♓ Рыбы', callback_data='pisces')]
]

signs_btn = InlineKeyboardMarkup(inline_keyboard=signs_btn)

date_btn = [
    [InlineKeyboardButton('Вчера', callback_data='yesterday'),
     InlineKeyboardButton('Завтра', callback_data='tomorrow')],
    [InlineKeyboardButton('Неделя', callback_data='week'),
     InlineKeyboardButton('Месяц', callback_data='month')],
    [InlineKeyboardButton('Год', callback_data='year')]
]

date_btn = InlineKeyboardMarkup(inline_keyboard=date_btn)