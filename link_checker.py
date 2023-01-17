from aiogram import types, Dispatcher
import re

async def catch_message(message:types.Message):
    await check_url_in_message('https://sdfdf.com')

async def check_url_in_message(message):
    result = re.search(r'(https?://[\S]+)',message,flags=0)
    print(result)
    return result

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(catch_message)
