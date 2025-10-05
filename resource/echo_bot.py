import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_API', '').strip()
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_API token found in environment variables")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()  # no bot passed here


@dp.message()
async def command_start_handler(message: types.Message):
    if message.text in ['/start', '/help']:
        await message.answer("Hi,\nI am FarukDev bot")


async def main():
    logging.info("Bot is starting...")
    await dp.start_polling(bot)  # bot is passed here
    logging.info("Bot stopped")


if __name__ == '__main__':
    import sys
    asyncio.run(main())
