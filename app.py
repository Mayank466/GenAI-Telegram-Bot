import os
import re
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "") or ""
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "TelegramJokeBot")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

def setup_llm_chain():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a comedy writer for an Indian Telegram group chat. Generate genuinely funny, clever, and unpredictable jokes in natural Hinglish. Keep it short, conversational, and original. Use sharp sarcasm, absurd logic, relatable desi situations, dark-ish humor, and unexpected punchlines. Roast ideas and situations more than people. Never explain a joke. Give a single statement joke in Hinglish, no more than 2-3 lines. Do not use hashtags or emojis. Avoid cliches, generic motivational jokes, basic Q&A jokes, cringe shayari, and predictable punchlines."
        ),
        ("user", "Generate a joke on the topic: {topic}")
    ])

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model="qwen/qwen3.8-27b"
    )

    return prompt | llm | StrOutputParser()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your Joke Bot. Send me a topic, and I'll generate a Hinglish joke for you! For example: '@CtrlAltLaughBot Python'")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Mention a topic, for example: '@CtrlAltLaughBot Python'")


async def generate_joke(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str):
    await update.message.reply_text(f"Generating a joke on the topic: {topic}...")
    joke = setup_llm_chain().invoke({"topic": topic}).strip()
    if not joke:
        joke = f"{topic} aur zindagi ka rishta bilkul wahi hai: sabko lagta hai main samajh raha hoon, par asli sach yeh hai ki main sirf apni confusion ko hashtag bana raha hoon."
    await update.message.reply_text(joke)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or not update.message.text:
        return

    msg = update.message.text.strip()
    bot_username = (context.bot.username or "").strip()
    if not bot_username or not msg:
        return

    mention_pattern = rf"@{re.escape(bot_username)}\s*(.+)"
    match = re.search(mention_pattern, msg)
    if not match:
        return

    topic = match.group(1).strip()
    if not topic:
        await update.message.reply_text("Please provide a topic after mentioning me. For example, '@CtrlAltLaughBot Python'")
        return

    await generate_joke(update, context, topic)


def main():
    token = os.getenv("TELEGRAM_API_KEY")
    if not token:
        raise RuntimeError("TELEGRAM_API_KEY is missing. Add it to your .env file.")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()