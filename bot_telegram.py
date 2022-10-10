from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Максим' :

        await message.answer("ЛЮБИТ ЮЛЮ!!!!!")

    if message.text == 'Юля для него кто?':
        await message.answer("НЕВЕРОЯТНАЯ КРАСОТКА И ПРОСТО БОГИНЯ")

    if message.text == 'Кто тут у нас самый невероятный человечек?':
        await message.reply("Мы все знаем о ком речь))")


executor.start_polling(dp, skip_updates=True)
