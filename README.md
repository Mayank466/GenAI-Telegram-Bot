# Telegram Joke Bot

A Telegram bot that generates short, conversational Hinglish jokes about a topic you provide. It uses the Groq API through LangChain and responds when mentioned in a chat.

## Try the bot

Experience it on Telegram: [@CtrlAltLaughBot](https://t.me/CtrlAltLaughBot). Send `/start`, then send a topic to get a Hinglish joke.

## Features

- Generates short, original Hinglish jokes
- Responds to bot mentions in Telegram chats
- Uses Groq's `qwen/qwen3.8-27b` model

## Requirements

- Python 3.10 or newer
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A Groq API key from [Groq Console](https://console.groq.com/keys)

## Setup

1. Clone this repository and open its directory:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your credentials:

   ```env
   TELEGRAM_API_KEY=your_telegram_bot_token
   GROQ_API_KEY=your_groq_api_key
   ```

   Do not commit `.env` or share its contents. The `.gitignore` file excludes it from Git.

## Run

Start the bot from the project directory:

```bash
python app.py
```

Open your bot in Telegram and send `/start`. In a group, mention the bot followed by a topic:

```text
@YourBotUsername Python
```

You can also send `/help` to see usage instructions.

## Project files

- `app.py` — Telegram bot and joke-generation logic
- `requirements.txt` — Python dependencies
- `testing.ipynb` — Notebook for manually testing Groq joke generation

## Security

Keep API keys private. If a key is exposed, revoke it with its provider and replace it in your local `.env` file. Never paste credentials into issues, screenshots, or commits.
"# GenAI-Telegram-Bot" 
