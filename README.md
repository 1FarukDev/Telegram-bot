# FarukDev Telegram ChatGPT Bot

A Telegram bot built with **Python**, **aiogram v3**, and **OpenAI API** that responds to user messages using ChatGPT. The bot supports commands like `/start`, `/help`, `/clear`, and maintains a conversation memory for better context.

---

## Features

- `/start` – Welcomes the user.
- `/help` – Shows a help menu with available commands.
- `/clear` – Clears the conversation memory.
- All other messages are sent to **ChatGPT** and replies are returned.
- Supports **OpenAI GPT-3.5-turbo** model.
- Uses **aiogram v3** for async Telegram bot handling.
- Simple in-memory conversation memory (can be upgraded per user).

---

## Requirements

- Python 3.9+
- [aiogram](https://docs.aiogram.dev/en/latest/)
- [OpenAI Python SDK >=1.0.0](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/1FarukDev/Telegram-bot.git
cd telegram-chatgpt-bot
````

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```env
TELEGRAM_BOT_API=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```


## Usage

Run the bot:

```bash
python main.py
```

Once running, interact with your bot on Telegram:

* `/start` – Start conversation.
* `/help` – Show help commands.
* `/clear` – Clear past conversation.
* Any other text – ChatGPT will respond.

---

## Notes

* The current memory implementation is **global**, meaning all users share the same conversation context. For multi-user support, per-user memory should be implemented.
* Make sure your **OpenAI API key** has access to GPT-3.5-turbo.
* Compatible with **OpenAI Python SDK >=1.0.0** (uses the new `openai.chat.completions.create()` interface).

---

## License

MIT License © 2025 Faruk Ajibade
=
