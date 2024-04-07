import asyncio

from aiogram import Bot, Dispatcher, F
import logging
from aiogram.dispatcher.filters import Command, ContentTypesFilter
from aiogram.types import ContentType
from dotenv import load_dotenv
from core.filters.iscintact import IsTrueContact
from core.handlers.callback import select_object
from core.handlers.basic import get_start, get_sticker, reset, sp_object
from core.handlers.contact import get_true_contact, get_fake_contact
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import news, about, idk, all_objects
from core.handlers.pay import order, pre_checkout_query, successful_payment


dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, F"Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, F"Бот остановлен")


async def start():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(token=settings.bots.bot_token)

    dp.startup.register(start_bot)
    dp.message.register(order, text="Благотварительость 💸")
    dp.callback_query.register(select_object)
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]))
    dp.message.register(news, text=sp_object)
    dp.message.register(reset, commands="reset")
    dp.message.register(about, text="О нас ❕")
    dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]), IsTrueContact())
    dp.message.register(get_fake_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    dp.message.register(all_objects, text="Список предметов:")
    dp.shutdown.register(stop_bot)
    dp.message.register(get_sticker, F.content_type == ContentType.STICKER)
    dp.message.register(get_start, Command(commands=["start", "run", "старт"]))
    dp.message.register(idk)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
