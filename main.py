import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

GIF_URL = "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام\nلعنت به این زندگی")
    await update.message.reply_animation(GIF_URL)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
