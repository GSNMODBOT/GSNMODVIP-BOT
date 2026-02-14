import telebot
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

print("🚀 البوت شغال...")

# ========== أمر start ==========
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = f"🌹 أهلاً {name} في بوت GSN MOD!\n\nأرسل /help لمشاهدة الأوامر."
    bot.reply_to(message, text)

# ========== أمر help ==========
@bot.message_handler(commands=['help'])
def help_command(message):
    text = """
📋 **الأوامر المتوفرة:**
/start - ترحيب
/help - المساعدة
/v1 - نسخة 1
/v2 - نسخة 2
/v3 - نسخة 3
/obb32 - ملف OBB 32 بت
/obb64 - ملف OBB 64 بت

💬 أو اسألني أي سؤال.
"""
    bot.reply_to(message, text, parse_mode="Markdown")

# ========== أوامر النسخ ==========
@bot.message_handler(commands=['v1'])
def v1(message):
    bot.reply_to(message, "🔥 نسخة 1:\nhttps://t.me/kenan_mod_2/37")

@bot.message_handler(commands=['v2'])
def v2(message):
    bot.reply_to(message, "⚡ نسخة 2:\nhttps://t.me/kenan_mod_2/44")

@bot.message_handler(commands=['v3'])
def v3(message):
    bot.reply_to(message, "🎯 نسخة 3:\nhttps://t.me/kenan_mod_2/47")

# ========== أوامر OBB ==========
@bot.message_handler(commands=['obb32'])
def obb32(message):
    bot.reply_to(message, "📦 رابط OBB 32 بت:\nhttps://t.me/GSN_MOD_OBB/31")

@bot.message_handler(commands=['obb64'])
def obb64(message):
    bot.reply_to(message, "📦 رابط OBB 64 بت:\nhttps://t.me/GSN_MOD_OBB/32")

# ========== الردود الذكية اليدوية ==========
@bot.message_handler(func=lambda m: True)
def smart_replies(message):
    text = message.text.strip()
    reply = None

    # ===== أسئلة شائعة =====
    if "من وين" in text or "بلدك" in text:
        reply = "🌍 أنا بوت، ساكن في السحابة ☁️، لكن مطوري يمني 🇾🇪"

    elif "مطورك" in text or "من صنعك" in text or "من مطورك" in text:
        reply = "👤 مطوري: @GSN_MOD_1 ❤️\nتحت أمرك دائمًا."

    elif "كيف حالك" in text or "كيفك" in text:
        reply = "الحمدلله تمام، انت كيفك؟ 🌹"

    elif "ملف اوبيبي" in text or "ملف obb" in text or "obb" in text:
        reply = "📦 أي نسخة تبغى؟\n/obb32 لنسخة 32 بت\n/obb64 لنسخة 64 بت"

    elif "32" in text and "obb" in text:
        reply = "📦 رابط OBB 32 بت:\nhttps://t.me/GSN_MOD_OBB/31"

    elif "64" in text and "obb" in text:
        reply = "📦 رابط OBB 64 بت:\nhttps://t.me/GSN_MOD_OBB/32"

    # ===== تحيات =====
    elif "السلام" in text or "سلام" in text:
        reply = "🌹 وعليكم السلام ورحمة الله وبركاته"

    elif "شكرا" in text or "شكرًا" in text:
        reply = "🤍 العفو، هذا واجبنا"

    # ===== رد افتراضي =====
    if reply:
        bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "👍 تم الاستلام")

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            time.sleep(3)
