import telebot
from config import TOKEN
import time

# تشغيل البوت
bot = telebot.TeleBot(TOKEN)

print("✅ البوت شغال...")

# أمر /start
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"🌹 أهلاً {name} في بوت GSN MOD!")

# أمر /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/start - ترحيب\n/help - المساعدة")

# الرد على أي رسالة
@bot.message_handler(func=lambda m: True)
def reply_all(message):
    bot.reply_to(message, "👍")

# تشغيل مستمر
while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(3)
