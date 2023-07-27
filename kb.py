from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
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

menu = InlineKeyboardMarkup(inline_keyboard=menu)
