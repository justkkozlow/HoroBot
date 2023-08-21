from aiogram import F, Router, types
from aiogram.filters import Command

import kb
import utils
from text import SIGN_DICT, SING_DATE
from db import save_zodiac_sign
router = Router()

# subscribe = []


@router.message(Command('start'))
async def zodiac_sign_list(message: types.Message):
    await message.reply(utils.main_message(), reply_markup=kb.signs_btn)


@router.callback_query(lambda callback: callback.data in SIGN_DICT)
async def sign_content(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(utils.sign_message(callback), reply_markup=kb.date_btn)
    user_id = callback.from_user.id
    sign = callback.data
    save_zodiac_sign(user_id, sign)


@router.callback_query(lambda callback: callback.data in SING_DATE)
async def select_date(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text=f'{utils.on_date(callback)}',
                                     reply_markup=kb.date_btn)


@router.callback_query(F.data == "subscribe")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'Спасибо {callback.from_user.first_name} {callback.from_user.last_name} за подписку 😘'
    )
