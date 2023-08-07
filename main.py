import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import kb
import utils
from text import SIGN_DICT, SING_DATE

logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def zodiac_sign_list(message: types.Message):
    await message.reply(utils.main_message(), reply_markup=kb.signs_btn)


@dp.callback_query_handler(lambda callback: callback.data in SIGN_DICT)
async def sign_content(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, utils.sign_message(callback), reply_markup=kb.date_btn)


@dp.callback_query_handler(lambda callback: callback.data in SING_DATE)
async def select_date(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=f'{utils.on_date(callback)}',
                                reply_markup=kb.date_btn)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
