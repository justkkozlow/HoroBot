import logging

from aiogram import Bot, Dispatcher, executor, types

import kb
from utils import main_message, sign_message, SIGN_LIST
from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def zodiac_sign_list(message: types.Message):
    await message.reply(main_message(), reply_markup=kb.menu)


@dp.callback_query_handler()
async def sign_content(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    if callback.data in SIGN_LIST:
        await bot.send_message(callback.from_user.id, sign_message(callback))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
