import logging
from aiogram import Bot, Dispatcher, executor, types

import kb
from bot import main_message
from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def zodiacks_list(message: types.Message):
    await message.reply(main_message(), reply_markup=kb.menu)


@dp.callback_query_handler()
async def sign_content(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, sign_list(callback.data))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
