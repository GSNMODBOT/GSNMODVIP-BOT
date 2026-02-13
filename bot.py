import telebot
from config import TOKEN, ADMIN_ID, CHANNEL, CHANNEL_LINK, CHANNEL_ID
from datetime import datetime
import time
import os

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

# ========== دالة تحويل رابط المنشور إلى صورة ==========
def رابط_الصورة(رابط_المنشور):
    parts = رابط_المنشور.split('/')
    msg_id = parts[-1]
    return f"https://t.me/kenan_mod_2/{msg_id}?embed=1"

# ========== النسخ مع الصور ==========
النسخ = {
    "v1": {
        "اسم": "🔥 ببجي لايت نسخة 1",
        "رابط_تحميل": "https://t.me/kenan_mod_2/37",
        "صورة_النسخة": "https://t.me/kenan_mod_2/36",
        "حجم": "680 MB",
    },
    "v2": {
        "اسم": "⚡ ببجي لايت نسخة 2",
        "رابط_تحميل": "https://t.me/kenan_mod_2/44",
        "صورة_النسخة": "https://t.me/kenan_mod_2/39",
        "حجم": "690 MB",
    },
    "v3": {
        "اسم": "🎯 ببجي لايت نسخة 3",
        "رابط_تحميل": "https://t.me/kenan_mod_2/47",
        "صورة_النسخة": "https://t.me/kenan_mod_2/45",
        "حجم": "675 MB",
    }
}

# ========== التحقق من الاشتراك ==========
def مشترك(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# ========== أمر start ==========
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    
    if len(message.text.split()) > 1:
        الكود = message.text.split()[1]
        
        if الكود in النسخ:
            نسخة = النسخ[الكود]
            
            if مشترك(user_id):
                bot.send_message(
                    message.chat.id,
                    f"""
{نسخة['اسم']}
━━━━━━━━━━━━━━
📦 الحجم: {نسخة['حجم']}
⬇️ رابط التحميل:
{نسخة['رابط_تحميل']}
━━━━━━━━━━━━━━
📢 {CHANNEL}
""",
                    disable_web_page_preview=False
                )
            else:
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(
                    "📢 اشترك في القناة",
                    url=CHANNEL_LINK
                ))
                markup.add(telebot.types.InlineKeyboardButton(
                    "🔄 تحقق من الاشتراك",
                    callback_data=f"check_{الكود}"
                ))
                
                bot.send_photo(
                    message.chat.id,
                    photo=رابط_الصورة(نسخة['صورة_النسخة']),
                    caption=f"""
{نسخة['اسم']}
━━━━━━━━━━━━━━
📦 الحجم: {نسخة['حجم']}
━━━━━━━━━━━━━━

⚠️ للتحميل اشترك بالقناة أولاً
""",
                    reply_markup=markup
                )
        else:
            bot.reply_to(message, "❌ رابط غير صحيح")
    
    else:
        if مشترك(user_id):
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            for كود, نسخة in النسخ.items():
                markup.add(telebot.types.InlineKeyboardButton(
                    f"{نسخة['اسم']} - {نسخة['حجم']}",
                    url=f"https://t.me/GSNMODBOT?start={كود}"
                ))
            bot.reply_to(message, "👇 اختر النسخة:", reply_markup=markup)
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(
                "📢 اشترك في القناة",
                url=CHANNEL_LINK
            ))
            bot.send_photo(
                message.chat.id,
                photo=رابط_الصورة("https://t.me/kenan_mod_2/36"),
                caption=f"⚠️ اشترك في القناة أولاً",
                reply_markup=markup
            )

# ========== معالجة الأزرار ==========
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data.startswith("check_"):
        if مشترك(call.from_user.id):
            الكود = call.data.replace("check_", "")
            نسخة = النسخ[الكود]
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=f"✅ تم التحقق!\n\n{نسخة['رابط_تحميل']}"
            )
        else:
            bot.answer_callback_query(call.id, "❌ لم تشترك بعد!", show_alert=True)

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    print("🚀 البوت شغال!")
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(3)