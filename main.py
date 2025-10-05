import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_API', '').strip()
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_API token found in environment variables")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OPENAI_API_KEY found in environment variables")

openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

# Memory for last assistant response (global)
class Reference:
    def __init__(self) -> None:
        self.answer = ""  # store last assistant response

reference = Reference()
model = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Function to clear conversation memory
def clear_past():
    reference.answer = ''

# Command handlers
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hi,\nI am bot created by FarukDev")

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    help_command = """
Hi there, I am bot created by FarukDev, Please follow these commands:
- /start - to start a new conversation
- /clear - to clear the past conversation and context
- /help - to get this help menu
I hope this helps :)
"""
    await message.answer(help_command)

@dp.message(Command("clear"))
async def clear_handler(message: types.Message):
    clear_past()
    await message.answer("I have cleared all past conversation")

# ChatGPT handler for all other text messages
@dp.message(F.text & ~F.text.startswith("/"))
async def chatgpt_handler(message: types.Message):
    print(f">>> USER: {message.text}")

    # Use new v1 API
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "assistant", "content": reference.answer},
            {"role": "user", "content": message.text},
        ],
    )

    reference.answer = response.choices[0].message.content
    print(f">>> ChatGPT: {reference.answer}")

    await message.answer(reference.answer)


# Main async function to start polling
async def main():
    logging.info("Bot is starting...")
    await dp.start_polling(bot)
    logging.info("Bot stopped")

# Entry point
if __name__ == '__main__':
    import sys
    asyncio.run(main())
