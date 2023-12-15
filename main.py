import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "5104141375:AAEh67B2ZaUzoZgrCcmcPrIeg1bS4iLZXH8"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: types.Message, bot:Bot) -> None:
    # Вывод сообщения после /start
    await message.answer(f'''
{hbold(message.from_user.full_name)}, добро пожаловать в бот-партнерской программы AviaSales.
Данный бот предназначен для работы с владельцами рекламных площадок.
Здесь вы можете подать заявку на платное размещение наших рекламных постов в Вашем канале.

После принятия Вашей заявки, если Ваши условия и цены нам подходят - Вы сможете автоматически заказать полную предоплату за указанное количество постов, а так же начать работу по рекламной компании
''')
    

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Подтвердить аккаунт", web_app=WebAppInfo(url="https://google.com/")
    ))
    
    await message.answer(
        'Чтобы начать, авторизуйтесь',
        reply_markup=builder.as_markup(),
    )
    
    
    


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
