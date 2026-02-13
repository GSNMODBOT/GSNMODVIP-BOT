import telebot
from config import TOKEN, ADMIN_ID, CHANNEL, CHANNEL_LINK, CHANNEL_ID
from datetime import datetime
import time

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

# ========== رابط صورة ==========
def رابط_الصورة(رابط):
    return f"https://t.me/kenan_mod_2/{رابط.split('/')[-1]}?embed=1"

# ========== نسخ ببجي ==========
النسخ = {
    "v1": {
        "اسم": "🔥 ببجي لايت نسخة 1 • استقرار تام",
        "رابط_تحميل": "https://t.me/kenan_mod_2/37",
        "صورة": "https://t.me/kenan_mod_2/36",
        "حجم": "680 MB",
        "وصف": "• ✅ Anti-Ban 100%\n• ⚡ 60 FPS بدون تقطيع\n• 🛡️ حماية من الحظر"
    },
    "v2": {
        "اسم": "⚡ ببجي لايت نسخة 2 • سرعة الأساطير",
        "رابط_تحميل": "https://t.me/kenan_mod_2/44",
        "صورة": "https://t.me/kenan_mod_2/39",
        "حجم": "690 MB",
        "وصف": "• 🚀 سرعة تصويب خارقة\n• 🎯 ريكويل 0%\n• 👑 سكنات حصرية"
    },
    "v3": {
        "اسم": "🎯 ببجي لايت نسخة 3 • للجوالات الضعيفة",
        "رابط_تحميل": "https://t.me/kenan_mod_2/47",
        "صورة": "https://t.me/kenan_mod_2/45",
        "حجم": "675 MB",
        "وصف": "• 📱 تشغيل على 2 جيجا رام\n• 🔋 بطارية أقل استهلاك\n• ✨ رسوم محسنة"
    }
}

# ========== تحقق ذكي ==========
def مشترك(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"خطأ تحقق: {e}")
        return False

# ========== Start ==========
@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    name = message.from_user.first_name

    if len(message.text.split()) > 1:
        كود = message.text.split()[1]
        if كود in النسخ:
            v = النسخ[كود]
            if مشترك(uid):
                bot.send_message(
                    uid,
                    f"""
{v['اسم']}
━━━━━━━━━━━━━━
📦 الحجم: {v['حجم']}
{v['وصف']}
━━━━━━━━━━━━━━
⬇️ رابط التحميل:
{v['رابط_تحميل']}
━━━━━━━━━━━━━━
📢 {CHANNEL}
""",
                    disable_web_page_preview=False
                )
            else:
                زر = telebot.types.InlineKeyboardMarkup()
                زر.add(
                    telebot.types.InlineKeyboardButton("📢 اشترك بالقناة", url=CHANNEL_LINK),
                    telebot.types.InlineKeyboardButton("🔄 تحقق بعد الاشتراك", callback_data=f"check_{كود}")
                )
                bot.send_photo(
                    uid,
                    photo=رابط_الصورة(v['صورة']),
                    caption=f"""
{v['اسم']}
━━━━━━━━━━━━━━
📦 الحجم: {v['حجم']}
{v['وصف']}
━━━━━━━━━━━━━━
⚠️ للتحميل اشترك بالقناة أولاً
""",
                    reply_markup=زر
                )
        else:
            bot.reply_to(message, "❌ رابط غير صحيح")
    else:
        if مشترك(uid):
            زر = telebot.types.InlineKeyboardMarkup(row_width=1)
            for k, v in النسخ.items():
                زر.add(telebot.types.InlineKeyboardButton(
                    f"{v['اسم']} • {v['حجم']}",
                    url=f"https://t.me/GSNMODBOT?start={k}"
                ))
            bot.reply_to(message, f"🌹 مرحبًا {name}\nاختر نسختك:", reply_markup=زر)
        else:
            زر = telebot.types.InlineKeyboardMarkup()
            زر.add(telebot.types.InlineKeyboardButton("📢 اشترك", url=CHANNEL_LINK))
            bot.send_photo(
                uid,
                photo=رابط_الصورة("https://t.me/kenan_mod_2/36"),
                caption=f"⚠️ اشترك أولاً يا {name} 😊",
                reply_markup=زر
            )

# ========== تحقق بعد الاشتراك ==========
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data.startswith("check_"):
        كود = call.data.split("_")[1]
        if مشترك(call.from_user.id):
            v = النسخ[كود]
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=f"""
✅ تم التحقق بنجاح!

{v['اسم']}
━━━━━━━━━━━━━━
⬇️ رابط التحميل:
{v['رابط_تحميل']}
"""
            )
            bot.answer_callback_query(call.id, "✅ اشتراكك مؤكد، تفضل الرابط")
        else:
            bot.answer_callback_query(call.id, "❌ لم يتم الاشتراك بعد، جرب مرة أخرى", show_alert=True)

# ========== تشغيل ==========
if __name__ == "__main__":
    print("🚀 البوت الذكي شغال")
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(3)
