from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


aurus = InlineKeyboardButton('Овен', callback_data='aurus')
taurus = InlineKeyboardButton('Телец', callback_data='taurus')
gemini = InlineKeyboardButton('Близнецы', callback_data='gemini')
cancer = InlineKeyboardButton('Рак', callback_data='cancer')
leo = InlineKeyboardButton('Лев', callback_data='leo')
virgo = InlineKeyboardButton('Дева', callback_data='virgo')
libra = InlineKeyboardButton('Весы', callback_data='libra')
scorpio = InlineKeyboardButton('Скорпион', callback_data='scorpio')
sagittarius = InlineKeyboardButton('Стрелец', callback_data='sagittarius')
capricorn = InlineKeyboardButton('Козерог', callback_data='capricorn')
aquarius = InlineKeyboardButton('Водолей', callback_data='aquarius')
pisces = InlineKeyboardButton('Рыбы', callback_data='pisces')


signs = InlineKeyboardMarkup().add(
    aurus,
    taurus,
    gemini,
    cancer,
    leo,
    virgo,
    libra,
    scorpio,
    sagittarius,
    capricorn,
    aquarius,
    pisces,
)
