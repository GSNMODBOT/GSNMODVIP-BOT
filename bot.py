import telebot
from config import TOKEN, ADMIN_ID, CHANNEL, CHANNEL_LINK, CHANNEL_ID
import random
import time

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

# ========== دالة تحويل رابط المنشور إلى صورة ==========
def رابط_الصورة(رابط):
    return f"https://t.me/kenan_mod_2/{رابط.split('/')[-1]}?embed=1"

# ========== جميع نسخ ببجي لايت ==========
نسخ_ببجي = {
    "v1": {
        "اسم": "🔥 ببجي لايت نسخة 1 • استقرار تام",
        "حجم": "680 MB",
        "وصف": "• ✅ Anti-Ban 100%\n• ⚡ 60 FPS بدون تقطيع",
        "كود": "https://t.me/kenan_mod_2/37",
        "صورة": "https://t.me/kenan_mod_2/36"
    },
    "v2": {
        "اسم": "⚡ ببجي لايت نسخة 2 • سرعة الأساطير",
        "حجم": "690 MB",
        "وصف": "• 🚀 سرعة تصويب خارقة\n• 🎯 ريكويل 0%",
        "كود": "https://t.me/kenan_mod_2/44",
        "صورة": "https://t.me/kenan_mod_2/39"
    },
    "v3": {
        "اسم": "🎯 ببجي لايت نسخة 3 • للجوالات الضعيفة",
        "حجم": "675 MB",
        "وصف": "• 📱 تشغيل على 2 جيجا رام\n• 🔋 بطارية أقل استهلاك",
        "كود": "https://t.me/kenan_mod_2/47",
        "صورة": "https://t.me/kenan_mod_2/45"
    },
    "v4": {
        "اسم": "💀 ببجي لايت نسخة 4 • سكنات حصرية (قريبًا)",
        "حجم": "غير متاح",
        "وصف": "• 👑 سكنات نادرة\n• قيد الإعداد",
        "كود": "❌ لا يوجد كود بعد",
        "صورة": "https://t.me/kenan_mod_2/36"
    },
    "v5": {
        "اسم": "🕋 ببجي لايت نسخة عربية كاملة",
        "حجم": "غير متاح",
        "وصف": "• 🌍 واجهة عربية\n• قيد الإعداد",
        "كود": "❌ لا يوجد كود بعد",
        "صورة": "https://t.me/kenan_mod_2/36"
    }
}

# ========== التحقق من الاشتراك ==========
def مشترك(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# ========== ردود تلقائية عامة ==========
@bot.message_handler(func=lambda message: True)
def ردود_تلقائية(message):
    if message.text is None:
        return
    text = message.text.strip()
    reply = None

    if text in ["السلام", "السلام عليكم", "سلام"]:
        reply = "🌹 وعليكم السلام ورحمة الله وبركاته"
    elif text in ["شكرا", "شكرًا"]:
        reply = "🤍 العفو، هذا واجبنا"
    elif text in ["هلا", "هلا والله"]:
        reply = "🌹 هلا فيك نورت"
    elif text in ["كيفك", "كيف حالك"]:
        reply = "الحمدلله، انت كيفك؟"
    elif text in ["ايش اسمك", "اسمك ايه"]:
        reply = "أنا بوت غسان مود 🤖"
    elif text in ["من مطورك", "مين مطورك"]:
        reply = "مطوري: @GSN_MOD_1 ❤️"
    elif text in ["وين التحميل", "كيف احمل", "رابط التحميل"]:
        reply = "⬇️ حمل من هنا:\nhttps://t.me/kenan_mod_2"
    elif text in ["كيف اثبت", "طريقة التثبيت"]:
        reply = "📲 **طريقة التثبيت:**\n1. حمل الملف\n2. افتحه واضغط تثبيت\n3. إذا طلب صلاحيات، وافق\n4. استمتع باللعبة ✅"

    if reply:
        bot.reply_to(message, reply)

# ========== أمر start الرئيسي ==========
@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    name = message.from_user.first_name

    if len(message.text.split()) > 1:
        كود = message.text.split()[1]
        if كود in نسخ_ببجي:
            v = نسخ_ببجي[كود]
            if مشترك(uid):
                if v['كود'] == "❌ لا يوجد كود بعد":
                    bot.reply_to(message, f"⏳ {v['اسم']}\n📦 {v['حجم']}\n{v['وصف']}\n⚠️ لا يوجد كود بعد، جرب لاحقًا")
                else:
                    bot.send_message(uid, f"{v['اسم']}\n━━━━━━━━━━━━━━\n📦 {v['حجم']}\n{v['وصف']}\n━━━━━━━━━━━━━━\n⬇️ {v['كود']}", disable_web_page_preview=False)
            else:
                زر = telebot.types.InlineKeyboardMarkup()
                زر.add(telebot.types.InlineKeyboardButton("📢 اشترك", url=CHANNEL_LINK))
                bot.send_photo(uid, photo=رابط_الصورة(v['صورة']), caption=f"{v['اسم']}\n━━━━━━━━━━━━━━\n📦 {v['حجم']}\n{v['وصف']}\n━━━━━━━━━━━━━━\n⚠️ اشترك أولاً", reply_markup=زر)
    else:
        if مشترك(uid):
            زر = telebot.types.InlineKeyboardMarkup(row_width=1)
            for k, v in نسخ_ببجي.items():
                زر.add(telebot.types.InlineKeyboardButton(f"{v['اسم']}", url=f"https://t.me/GSNMODBOT?start={k}"))
            bot.reply_to(message, f"🌹 مرحبًا {name}\nاختر نسختك:", reply_markup=زر)
        else:
            زر = telebot.types.InlineKeyboardMarkup()
            زر.add(telebot.types.InlineKeyboardButton("📢 اشترك", url=CHANNEL_LINK))
            bot.send_photo(uid, photo=رابط_الصورة("https://t.me/kenan_mod_2/36"), caption=f"⚠️ اشترك أولًا يا {name}", reply_markup=زر)

# ========== أمر عرض جميع النسخ ==========
@bot.message_handler(commands=['نسخ', 'versions'])
def عرض_النسخ(message):
    text = "📋 **جميع النسخ المتوفرة:**\n\n"
    for key, val in نسخ_ببجي.items():
        if val['كود'] != "❌ لا يوجد كود بعد":
            text += f"✅ {val['اسم']} – {val['حجم']}\n{val['وصف']}\n📎 {val['كود']}\n\n"
        else:
            text += f"⏳ {val['اسم']} – {val['حجم']}\n{val['وصف']}\n⚠️ {val['كود']}\n\n"
    bot.reply_to(message, text, parse_mode="Markdown")

# ========== أوامر حجم النسخة الفردية ==========
@bot.message_handler(commands=['v1', 'v2', 'v3', 'v4', 'v5'])
def حجم_نسخة(message):
    cmd = message.text[1:]
    if cmd in نسخ_ببجي:
        v = نسخ_ببجي[cmd]
        if v['كود'] == "❌ لا يوجد كود بعد":
            bot.reply_to(message, f"⏳ {v['اسم']}\n📦 {v['حجم']}\n{v['وصف']}\n⚠️ لا يوجد كود بعد")
        else:
            bot.reply_to(message, f"{v['اسم']}\n📦 {v['حجم']}\n{v['وصف']}\n📎 {v['كود']}")
    else:
        bot.reply_to(message, "❌ هذه النسخة غير موجودة")

# ========== أمر نسخة عشوائية ==========
@bot.message_handler(commands=['random'])
def نسخة_عشوائية(message):
    المتاحة = [v for v in نسخ_ببجي.values() if v['كود'] != "❌ لا يوجد كود بعد"]
    if المتاحة:
        v = random.choice(المتاحة)
        bot.reply_to(message, f"🎲 اخترت لك:\n{v['اسم']}\n📎 {v['كود']}")
    else:
        bot.reply_to(message, "⏳ لا توجد نسخ متاحة حاليًا")

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    print("🚀 البوت شغال مع جميع الإضافات الذكية ✅")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(3)
