from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

# Словарь для хранения имен котов
cat_names = {}

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Добавить кота - /add Cat, список котов - /view")

def add_cat(update, context):
    # Разбираем команду /add
    command_parts = context.args
    if not command_parts:
        context.bot.send_message(chat_id=update.message.chat_id, text="Укажите имя кота после команды /add")
        return

    cat_name = ' '.join(command_parts)
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
    dp.add_handler(CommandHandler("add", add_cat, pass_args=True))  # Используем pass_args для передачи аргументов
    dp.add_handler(CommandHandler("view", view_cat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
