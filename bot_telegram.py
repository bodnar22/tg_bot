from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)                      # простое ехо
    await message.reply(message.text)                         # упоминает автора сообщения при ответе
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)

# virtual enviroment


