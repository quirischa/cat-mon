from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN

# Словарь для хранения имен котов
cat_names = {}

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Добавить кота - /add, список котов - /view")

def add_cat(update, context):
    # Запрашиваем у пользователя ввод имени кота
    context.bot.send_message(chat_id=update.message.chat_id, text="Введите имя кота")
    # Устанавливаем обработчик сообщений для получения имени кота
    context.bot.register_next_step_handler(update.message, save_cat_name)

def save_cat_name(update, context):
    cat_name = update.message.text
    # Добавляем имя кота в словарь
    cat_names[update.message.chat_id] = cat_name
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Имя кота {cat_name} добавлено!")

def view_cat(update, context):
    # Проверяем, есть ли имя кота в словаре
    cat_name = cat_names.get(update.message.chat_id)
    if cat_name:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Имя кота: {cat_name}")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Кот не найден, добавьте кота командой /add")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", add_cat))
    dp.add_handler(CommandHandler("view", view_cat))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))  # Добавляем обработчик для обычных текстовых сообщений

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
