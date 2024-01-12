from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from config import BOT_TOKEN

# Обработка команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я твой бот.")

# Обработка обычных сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет")

def main():
    # Получите токен бота от BotFather и вставьте его здесь
    token = "BOT_TOKEN"

    # Создайте объект Updater и передайте ему токен бота
    updater = Updater(token, use_context=True)

    # Получите объект Dispatcher для регистрации обработчиков
    dp = updater.dispatcher

    # Добавьте обработчики команды /start и обычных сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запустите бота
    updater.start_polling()

    # Дайте боту время работать
    updater.idle()

if __name__ == '__main__':
    main()
