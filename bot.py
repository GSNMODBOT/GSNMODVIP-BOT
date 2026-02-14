import telebot
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"🌹 أهلاً {message.from_user.first_name}")

@bot.message_handler(func=lambda m: True)
def ردود(message):
    if "السلام" in message.text:
        bot.reply_to(message, "🌹 وعليكم السلام")
    elif "مشكلة" in message.text or "بيوقف" in message.text:
        bot.reply_to(message, "⚠️ جرب تحذف اللعبة وتثبتها مرة ثانية، وإذا استمرت المشكلة أخبرني")
    else:
        bot.reply_to(message, "👍 تم الاستلام")

print("✅ البوت شغال")
bot.polling(none_stop=True)
