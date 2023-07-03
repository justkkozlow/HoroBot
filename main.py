import logging
from aiogram import Bot, Dispatcher, executor, types

import kb
from text import *
from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def zodiacks_list(message: types.Message):
    await message.reply(choose_sign, reply_markup=kb.signs)


@dp.callback_query_handler(lambda callback: zodiacks_list(callback))
async def sign_content(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Hmmmm')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
