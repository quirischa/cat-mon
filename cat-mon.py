from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from config import BOT_TOKEN

# Определение состояний
ENTER_CAT_NAME = 1
CONFIRM_DELETE = 2

# Словарь для хранения имен котов
cat_names = {}
number_of_cats = len(cat_names)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Привет! Сейчас у вас {number_of_cats} cat. Максимум: 1 cat. Добавить кота - /add, список - /view")

def add_cat(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Введите имя кота")
    return ENTER_CAT_NAME

def save_cat_name(update, context):
    cat_name = update.message.text
    cat_names[update.message.chat_id] = cat_name
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Имя кота {cat_name} добавлено!")
    # Возвращаем в начальное состояние
    return ConversationHandler.END

def view_cat(update, context):
    # Проверяем, есть ли имя кота в словаре
    cat_name = cat_names.get(update.message.chat_id)
    if cat_name:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Имя кота: {cat_name}")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Кот не найден, добавьте кота командой /add")

def delete_cat(update, context):
    cat_name = cat_names.get(update.message.chat_id)
    if cat_name:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Вы уверены, что хотите удалить кота {cat_name}? (Да/Нет)")
        return CONFIRM_DELETE
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Кот не найден.")

def confirm_delete(update, context):
    confirmation = update.message.text.lower()
    if confirmation == 'да':
        del cat_names[update.message.chat_id]
        context.bot.send_message(chat_id=update.message.chat_id, text="Кот удален.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Отменено.")

    # Возвращаем в начальное состояние
    return ConversationHandler.END

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавляем ConversationHandler для управления состояниями
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('add', add_cat),
            CommandHandler('delete', delete_cat)
        ],
        states={
            ENTER_CAT_NAME: [MessageHandler(Filters.text, save_cat_name)],
            CONFIRM_DELETE: [MessageHandler(Filters.text, confirm_delete)],
        },
        fallbacks=[]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("view", view_cat))
    dp.add_handler(conv_handler)

#    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))  # Добавляем обработчик для обычных текстовых сообщений

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
