import telebot
from config import TOKEN, ADMIN_ID, CHANNEL, CHANNEL_LINK
import time

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

print("🚀 البوت بدأ التشغيل...")
print(f"🤖 اسم البوت: @{bot.get_me().username}")
print("✅ الردود اليدوية مفعلة")

# ========== قاموس النسخ (زيادة باللي عندك) ==========
النسخ = {
    "v1": {
        "اسم": "🔥 ببجي لايت نسخة 1",
        "رابط": "https://t.me/kenan_mod_2/37",
        "حجم": "680 MB"
    },
    "v2": {
        "اسم": "⚡ ببجي لايت نسخة 2",
        "رابط": "https://t.me/kenan_mod_2/44",
        "حجم": "690 MB"
    },
    "v3": {
        "اسم": "🎯 ببجي لايت نسخة 3",
        "رابط": "https://t.me/kenan_mod_2/47",
        "حجم": "675 MB"
    }
}

# ========== أمر start ==========
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = f"""
🌹 أهلاً {name} في بوت GSN MOD!

📌 الأوامر المتوفرة:
/versions - عرض كل النسخ
/v1 - نسخة 1
/v2 - نسخة 2
/v3 - نسخة 3
/help - المساعدة

📢 القناة: {CHANNEL}
"""
    bot.reply_to(message, text)

# ========== أمر المساعدة ==========
@bot.message_handler(commands=['help', 'مساعدة'])
def help_command(message):
    text = """
🆘 **المساعدة**:
- إذا واجهت مشكلة في التثبيت، أرسل "مشكلة تثبيت"
- إذا تبغى نسخة معينة، استخدم /v1, /v2, /v3
- لأي استفسار آخر، اكتبه وأنا أرد عليك

📢 {CHANNEL}
"""
    bot.reply_to(message, text)

# ========== عرض كل النسخ ==========
@bot.message_handler(commands=['versions', 'نسخ'])
def versions(message):
    text = "📦 **النسخ المتوفرة:**\n\n"
    for key, val in النسخ.items():
        text += f"🔹 {val['اسم']}\n📦 {val['حجم']}\n⬇️ /{key}\n\n"
    bot.reply_to(message, text, parse_mode="Markdown")

# ========== أوامر النسخ ==========
@bot.message_handler(commands=['v1', 'v2', 'v3'])
def send_version(message):
    key = message.text[1:]  # v1, v2, v3
    if key in النسخ:
        v = النسخ[key]
        bot.reply_to(message, f"{v['اسم']}\n📦 {v['حجم']}\n⬇️ {v['رابط']}")
    else:
        bot.reply_to(message, "❌ هذه النسخة غير موجودة")

# ========== الردود التلقائية اليدوية ==========
@bot.message_handler(func=lambda m: True)
def manual_replies(message):
    text = message.text.strip()
    reply = None

    # ===== تحيات =====
    if "السلام" in text or "سلام" in text:
        reply = "🌹 وعليكم السلام ورحمة الله وبركاته"
    elif "شكرا" in text or "شكرًا" in text:
        reply = "🤍 العفو، هذا واجبنا"
    elif "كيفك" in text or "كيف حالك" in text:
        reply = "الحمدلله تمام، انت كيفك؟"
    elif "من وين" in text:
        reply = "أنا بوت، ساكن في السحابة ☁️"

    # ===== مشاكل تقنية =====
    elif "بيوقف" in text or "توقف" in text or "بطء" in text:
        reply = "⚠️ جرب تحذف اللعبة وتثبتها مرة ثانية، وإذا استمرت المشكلة أخبرني"
    elif "تثبيت" in text or "تنصيب" in text:
        reply = "📲 طريقة التثبيت:\n1. حمل الملف\n2. افتحه واضغط تثبيت\n3. إذا طلب صلاحيات، وافق\n4. استمتع باللعبة ✅"
    elif "ايمبوت" in text or "aimbot" in text:
        reply = "🔫 الإيمبوت موجود في نسخة v2:\nhttps://t.me/kenan_mod_2/44"
    elif "سكنات" in text or "اسكنات" in text:
        reply = "🎭 قريبًا في نسخة v4 سكنات حصرية، تابع القناة"
    elif "حجم" in text:
        reply = "📦 v1: 680 MB\n📦 v2: 690 MB\n📦 v3: 675 MB"

    # ===== قناة وتواصل =====
    elif "القناة" in text or "قناتك" in text:
        reply = f"📢 قناتنا: {CHANNEL_LINK}"
    elif "مطور" in text or "مين صنعك" in text:
        reply = "👤 مطوري: @GSN_MOD_1 ❤️"

    # ===== رد افتراضي لو ما لقى =====
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
