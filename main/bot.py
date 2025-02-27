import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "7780202537:AAEhtNHJipLyfd-Kwtbrq3_yRhrUldF7kfc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# Клавиатура с кнопкой "Start"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("/start"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Соо про фам", reply_markup=keyboard)

@dp.message_handler(commands=['link'])
async def send_link(message: types.Message):
    await message.reply("https://discord.gg/S4yyv3Sw")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)