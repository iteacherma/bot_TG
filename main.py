import os

from aiogram import Bot, Dispatcher, executor, types # аиограм ассихронная библиотека
from dotenv import load_dotenv
load_dotenv()
APITOKEN = os.getenv('token')

bot = Bot(APITOKEN)
dp = Dispatcher(bot) #процесс входящих обновлений. все события обрабатываются через него

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.reply('привет')


if __name__ == '__main__':
    import link_checker  # так как затрагиваем только регистрацию
    link_checker.register_handlers(dp)
    executor.start_polling(dp,skip_updates=True) # запускаем отлавливать события с пропуском обновлений
