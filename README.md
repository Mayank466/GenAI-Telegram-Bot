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

4. Copy `.env.example` to `.env` in the project root and replace the placeholder values with your credentials:

   ```env
   TELEGRAM_API_KEY=your_telegram_bot_token
   GROQ_API_KEY=your_groq_api_key
   TELEGRAM_WEBHOOK_SECRET=your_random_webhook_secret
   ```

   `TELEGRAM_WEBHOOK_SECRET` is only needed when deploying to Render. Do not commit `.env` or share its contents. The `.gitignore` file excludes it from Git.

To run the optional testing notebook, install its additional development dependency with `pip install -r requirements-dev.txt`.

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

## Deploy to Render

The included Render Blueprint deploys the bot as a **Free Web Service** using Telegram webhooks. When run locally without `RENDER_EXTERNAL_URL`, the bot continues to use long polling.

1. Push this repository to GitHub.
2. In the [Render Dashboard](https://dashboard.render.com/), select **New** > **Blueprint** and connect the repository. Render will read the included `render.yaml`.
3. Enter the `TELEGRAM_API_KEY` and `GROQ_API_KEY` values when prompted. Set `TELEGRAM_WEBHOOK_SECRET` to a random value containing only letters, numbers, underscores, or hyphens (for example, generate one with `python -c "import secrets; print(secrets.token_urlsafe(32))"`). Do not add quotes around the values.
4. Deploy the Blueprint. Check the service's logs in Render to confirm it starts successfully.

Free Web Services can spin down after a period without incoming requests, which may delay the first response while the service starts again. If you need to add or replace a key later, open the service's **Environment** settings, update the value, and redeploy. Do not commit credentials to `render.yaml` or the repository.

## Project files

- `app.py` — Telegram bot and joke-generation logic
- `requirements.txt` — Python dependencies
- `testing.ipynb` — Notebook for manually testing Groq joke generation
- `render.yaml` — Render Free Web Service configuration

## Security

Keep API keys and the webhook secret private. If a key is exposed, revoke it with its provider and replace it in your local `.env` file or Render environment settings. Never paste credentials into issues, screenshots, or commits.
"# GenAI-Telegram-Bot" 
