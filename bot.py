import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json

# Файл для хранения суммы
SUM_FILE = 'donation_sum.json'

def load_sum():
    if os.path.exists(SUM_FILE):
        with open(SUM_FILE, 'r') as f:
            return json.load(f)
    return {"current_sum": 0, "target_sum": 5000000}

def save_sum(data):
    with open(SUM_FILE, 'w') as f:
        json.dump(data, f)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я бот для управления пожертвованиями.\n\n"
        "Доступные команды:\n"
        "/show - Показать текущую сумму\n"
        "/add [сумма] - Добавить пожертвование\n"
        "/set [сумма] - Установить точную сумму\n"
        "/target [сумма] - Изменить целевую сумму"
    )

def show_sum(update: Update, context: CallbackContext):
    data = load_sum()
    update.message.reply_text(
        f"Текущая сумма: {data['current_sum']:,} ₸\n"
        f"Целевая сумма: {data['target_sum']:,} ₸\n"
        f"Прогресс: {data['current_sum'] / data['target_sum'] * 100:.1f}%"
    )

def add_sum(update: Update, context: CallbackContext):
    try:
        amount = int(context.args[0])
        data = load_sum()
        data['current_sum'] += amount
        save_sum(data)
        update.message.reply_text(f"Добавлено {amount:,} ₸\nНовая сумма: {data['current_sum']:,} ₸")
    except (IndexError, ValueError):
        update.message.reply_text("Пожалуйста, укажите корректную сумму. Например: /add 1000")

def set_sum(update: Update, context: CallbackContext):
    try:
        amount = int(context.args[0])
        data = load_sum()
        data['current_sum'] = amount
        save_sum(data)
        update.message.reply_text(f"Сумма установлена: {amount:,} ₸")
    except (IndexError, ValueError):
        update.message.reply_text("Пожалуйста, укажите корректную сумму. Например: /set 1000")

def set_target(update: Update, context: CallbackContext):
    try:
        amount = int(context.args[0])
        data = load_sum()
        data['target_sum'] = amount
        save_sum(data)
        update.message.reply_text(f"Целевая сумма установлена: {amount:,} ₸")
    except (IndexError, ValueError):
        update.message.reply_text("Пожалуйста, укажите корректную сумму. Например: /target 5000000")

def main():
    updater = Updater('7856309359:AAG2qcgB9fJ9AqV2birmBBWFLz72YjZf-oQ')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("show", show_sum))
    dp.add_handler(CommandHandler("add", add_sum))
    dp.add_handler(CommandHandler("set", set_sum))
    dp.add_handler(CommandHandler("target", set_target))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 