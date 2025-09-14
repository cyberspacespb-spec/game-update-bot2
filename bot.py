import os
import telebot

# Получаем токен из переменных окружения (безопаснее)
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден. Укажи его в настройках Railway → Variables.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет 👋! Я бот и буду присылать обновления игр.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("✅ Бот запущен...")
bot.polling(none_stop=True)
