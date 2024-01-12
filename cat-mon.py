from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN  # Убедитесь, что путь к файлу правильный

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я твой бот.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
