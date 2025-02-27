from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

# Вставьте сюда ваш токен
TOKEN = "7780202537:AAEhtNHJipLyfd-Kwtbrq3_yRhrUldF7kfc"

# Текст приветствия
welcome_text = "Привет! Я бот семьи Synthetic."

# ✅ Исправленный путь к изображению
image_path = r"C:\Users\Dear\Desktop\synthetic\images\logo.jpg"

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(welcome_text)

    # Проверяем, существует ли файл
    try:
        with open(image_path, "rb") as photo:
            await update.message.reply_photo(photo=photo)
    except FileNotFoundError:
        await update.message.reply_text("Ошибка: изображение не найдено.")

def main():
    app = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))

    # Запуск бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
