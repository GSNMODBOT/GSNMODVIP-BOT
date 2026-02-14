import telebot
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

print("🚀 البوت الخارق – نظام حل المشاكل مفعل ✅")

# ========== قاموس الأكواد ==========
اكواد_النسخ = {
    "v1": "🔥 ببجي لايت نسخة 1\nhttps://t.me/kenan_mod_2/37",
    "v2": "⚡ ببجي لايت نسخة 2\nhttps://t.me/kenan_mod_2/44",
    "v3": "🎯 ببجي لايت نسخة 3\nhttps://t.me/kenan_mod_2/47",
}

# ========== أمر start ==========
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = f"""
🌹 أهلاً {name} في بوت GSN MOD الذكي!

📌 الأوامر السريعة:
/help - المساعدة
/obb32 - OBB 32 بت
/obb64 - OBB 64 بت
/اكواد - جميع الأكواد

💬 أو اسألني عن أي مشكلة!
"""
    bot.reply_to(message, text)

# ========== أمر help ==========
@bot.message_handler(commands=['help'])
def help_command(message):
    text = """
📋 **الأوامر المتوفرة:**
/start - ترحيب
/help - المساعدة
/obb32 - OBB 32 بت
/obb64 - OBB 64 بت
/اكواد - عرض الأكواد
/jum3a - جمعة مباركة
/evening - مساء الخير

💬 أو اكتب "عندي مشكلة" للدعم الفني.
"""
    bot.reply_to(message, text, parse_mode="Markdown")

# ========== أوامر OBB ==========
@bot.message_handler(commands=['obb32'])
def obb32(message):
    bot.reply_to(message, "📦 OBB 32 بت:\nhttps://t.me/GSN_MOD_OBB/31")

@bot.message_handler(commands=['obb64'])
def obb64(message):
    bot.reply_to(message, "📦 OBB 64 بت:\nhttps://t.me/GSN_MOD_OBB/33")

# ========== أوامر المناسبات ==========
@bot.message_handler(commands=['jum3a', 'جمعة'])
def jum3a(message):
    bot.reply_to(message, "🌙 جمعة مباركة عليك وعلى أحبابك 🕊️❤️")

@bot.message_handler(commands=['evening', 'مساء'])
def evening(message):
    bot.reply_to(message, "🌆 مساء الخير والسرور، نورت البوت 🤍")

# ========== عرض كل الأكواد ==========
@bot.message_handler(commands=['اكواد', 'codes'])
def show_codes(message):
    if اكواد_النسخ:
        text = "🔖 **الأكواد المتوفرة:**\n\n"
        for name, code in اكواد_النسخ.items():
            text += f"• `{name}`: {code[:30]}...\n"
        text += "\n📝 أرسل /كود اسم_النسخة"
        bot.reply_to(message, text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "📭 لا توجد أكواد بعد")

# ========== البحث عن كود نسخة ==========
@bot.message_handler(commands=['كود'])
def get_code(message):
    try:
        name = message.text.split()[1].lower()
        if name in اكواد_النسخ:
            bot.reply_to(message, f"🔖 كود {name}:\n{اكواد_النسخ[name]}")
        else:
            bot.reply_to(message, f"❌ لا يوجد كود باسم '{name}'")
    except:
        bot.reply_to(message, "⚠️ استخدم: /كود اسم_النسخة")

# ========== نظام المشاكل الذكي (بالأزرار) ==========
@bot.message_handler(func=lambda m: "مشكله" in m.text or "مشكلة" in m.text)
def show_problems(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("❌ التطبيق ليس متوافق", callback_data="problem_incompatible"),
        telebot.types.InlineKeyboardButton("⚠️ لم يتم تثبيت التطبيق", callback_data="problem_install"),
        telebot.types.InlineKeyboardButton("📲 كيف أثبت النسخة؟", callback_data="problem_install_method"),
        telebot.types.InlineKeyboardButton("📁 كيف أرَكب ملف OBB؟", callback_data="problem_obb"),
        telebot.types.InlineKeyboardButton("🗂️ كيف أرَكب ملف data؟", callback_data="problem_data")
    )
    bot.reply_to(message, "🔍 اختر مشكلتك من القائمة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_problems(call):
    if call.data == "problem_incompatible":
        bot.send_message(call.message.chat.id, """
❌ **مشكلة: التطبيق غير متوافق**

✅ **الحل:**
1. تأكد من إصدار جهازك (Android 8+)
2. إذا كان جهازك 64 بت، جرب نسخة 64 بت
3. حمل النسخة المناسبة لجهازك:
   /obb32 للـ 32 بت
   /obb64 للـ 64 بت
4. جرب نسخة v3 (للجوالات الضعيفة)
""")
    elif call.data == "problem_install":
        bot.send_message(call.message.chat.id, """
⚠️ **مشكلة: لم يتم تثبيت التطبيق**

✅ **الحل:**
1. امسح أي نسخة قديمة من اللعبة
2. فعّل "مصادر غير معروفة" من إعدادات الأمان
3. تأكد أن مساحة التخزين كافية (2 جيجا على الأقل)
4. أعد تشغيل الجهاز
5. حمّل النسخة مرة ثانية
""")
    elif call.data == "problem_install_method":
        bot.send_message(call.message.chat.id, """
📲 **طريقة تثبيت النسخة:**

1. حمّل ملف APK من الرابط
2. افتح الملف
3. اضغط "تثبيت"
4. إذا ظهر تحذير، وافق على "مصادر غير معروفة"
5. بعد التثبيت، افتح اللعبة
6. إذا طلب ملف OBB، اتبع خطوات تركيب OBB
""")
    elif call.data == "problem_obb":
        bot.send_message(call.message.chat.id, """
📁 **كيفية تركيب ملف OBB:**

1. حمّل ملف OBB المناسب لجهازك:
   /obb32 للـ 32 بت
   /obb64 للـ 64 بت
2. استخدم برنامج ZArchiver
3. انسخ المجلد إلى:
   Internal Storage/Android/obb/
4. تأكد من اسم المجلد يكون بالظبط:
   com.tencent.ig
5. أعد تشغيل اللعبة
""")
    elif call.data == "problem_data":
        bot.send_message(call.message.chat.id, """
🗂️ **كيفية تركيب ملف data:**

1. حمل ملف data من الرابط (قريباً)
2. استخدم برنامج ZArchiver
3. انسخ المجلد إلى:
   Internal Storage/Android/data/
4. تأكد من اسم المجلد يكون بالظبط:
   com.tencent.ig
5. أعد تشغيل اللعبة
""")
    bot.answer_callback_query(call.id)

# ========== الردود الذكية الشاملة ==========
@bot.message_handler(func=lambda m: True)
def smart_replies(message):
    text = message.text.strip().lower()
    reply = None

    # ===== الكلمات المتوقعة + ردودها =====
    كلمات_متوقعة = {
        "طريقة التثبيت": "📲 طريقة تثبيت النسخ: حمّل الملف، افتحه، اضغط تثبيت، وافق على الصلاحيات.",
        "النسخة الأصلية": "🎯 كل نسخنا معدلة وآمنة 100%، جرب v2 أو v3.",
        "فيرجن": "🔥 الفيرجن (الدمار) موجود في v2، جربها.",
        "ايمبوت": "🔫 الإيمبوت مفعل تلقائياً في v2.",
        "بان": "🛡️ نسخنا مضادة للبان 100%، جرب v1.",
        "باسورد": "🔐 معظم النسخ بدون باسورد، لو فيه بنكتبه في المنشور.",
        "آخر تحديث": "🆕 آخر تحديث كان قبل 3 أيام، v3.",
        "وين السكنات": "🎭 سكنات حصرية قريباً في v4.",
        "الشحن": "💎 الشحن والشدات متاحة في v4 (قيد الإعداد).",
        "الدعم الفني": "🛠️ للدعم الفني، تواصل مع @GSN_MOD_1."
    }

    for كلمة, رد_مخصص in كلمات_متوقعة.items():
        if كلمة in text:
            reply = رد_مخصص
            break

    # ===== تحيات ومناسبات =====
    if not reply:
        if "السلام" in text or "سلام" in text:
            reply = "🌹 وعليكم السلام ورحمة الله وبركاته"
        elif "صباح" in text:
            reply = "🌅 صباح النور والسرور"
        elif "مساء" in text:
            reply = "🌆 مساء الخير والهنا"
        elif "جمعة" in text:
            reply = "🌙 جمعة مباركة، تقبل الله طاعاتكم"
        elif "شكرا" in text:
            reply = "🤍 العفو، هذا واجبنا"

    # ===== معلومات شخصية =====
    elif "من وين" in text:
        reply = "🌍 أنا بوت، ساكن في السحابة ☁️، مطوري يمني 🇾🇪"
    elif "مطورك" in text:
        reply = "👤 مطوري: @GSN_MOD_1 ❤️"
    elif "كيفك" in text:
        reply = "الحمدلله تمام، انت كيفك؟ 🌹"

    # ===== ملفات OBB =====
    elif "obb" in text or "اوبيبي" in text:
        if "32" in text:
            reply = "📦 OBB 32 بت:\nhttps://t.me/GSN_MOD_OBB/31"
        elif "64" in text:
            reply = "📦 OBB 64 بت:\nhttps://t.me/GSN_MOD_OBB/33"
        else:
            reply = "📦 أي إصدار تبغى؟ 32 أو 64؟"

    # ===== روابط سريعة =====
    elif "القناة" in text:
        reply = "📢 قناتنا: @kenan_mod_2"
    elif "obb32" in text:
        reply = "📦 https://t.me/GSN_MOD_OBB/31"
    elif "obb64" in text:
        reply = "📦 https://t.me/GSN_MOD_OBB/33"

    # ===== رد افتراضي =====
    if reply:
        bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "👍 تم الاستلام، شكراً لتواصلك")

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            time.sleep(3)
