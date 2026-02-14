import telebot
from config import TOKEN, GEMINI_KEY
import google.generativeai as genai
import time

# ========== تشغيل Gemini ==========
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

# ========== البوت ==========
bot = telebot.TeleBot(TOKEN)
bot.skip_pending = True

print("🚀 البوت مع Gemini بدأ التشغيل...")
print(f"🤖 اسم البوت: @{bot.get_me().username}")

# ========== أمر start ==========
@bot.message_handler(commands=['start'])
def start(message):
    welcome = f"""
🌹 أهلاً {message.from_user.first_name} في بوت GSN MOD الذكي!

✨ أنا بستعدك في أي حاجة:
• اسألني أي سؤال
• استفسر عن ببجي لايت
• أطلب مساعدة

📝 جرب تكتب حاجة دلوقتي!
"""
    bot.reply_to(message, welcome)

# ========== أمر المساعدة ==========
@bot.message_handler(commands=['help', 'مساعدة'])
def help_command(message):
    help_text = """
📋 الأوامر المتوفرة:
/start - ترحيب
/help - المساعدة
/versions - عرض النسخ
/v1 - نسخة 1
/v2 - نسخة 2
/v3 - نسخة 3

💬 أو اسألني أي سؤال بالعربي
"""
    bot.reply_to(message, help_text)

# ========== أمر عرض النسخ ==========
@bot.message_handler(commands=['versions', 'نسخ'])
def show_versions(message):
    versions = """
📦 **النسخ المتوفرة:**
/v1 - نسخة 1 (680 MB)
/v2 - نسخة 2 (690 MB)
/v3 - نسخة 3 (675 MB)
"""
    bot.reply_to(message, versions, parse_mode="Markdown")

# ========== أوامر النسخ ==========
@bot.message_handler(commands=['v1', 'v2', 'v3'])
def version_command(message):
    if message.text == '/v1':
        bot.reply_to(message, "🔥 نسخة 1:\nhttps://t.me/kenan_mod_2/37")
    elif message.text == '/v2':
        bot.reply_to(message, "⚡ نسخة 2:\nhttps://t.me/kenan_mod_2/44")
    elif message.text == '/v3':
        bot.reply_to(message, "🎯 نسخة 3:\nhttps://t.me/kenan_mod_2/47")

# ========== الذكاء الاصطناعي مع Gemini ==========
@bot.message_handler(func=lambda m: True)
def ai_response(message):
    try:
        user_input = message.text
        user_name = message.from_user.first_name
        
        # إظهار أن البوت بيكتب
        bot.send_chat_action(message.chat.id, 'typing')
        
        # ردود سريعة مبرمجة
        if "السلام" in user_input:
            bot.reply_to(message, "🌹 وعليكم السلام")
            return
        elif "شكرا" in user_input:
            bot.reply_to(message, "🤍 العفو، تحت أمرك")
            return
        elif "كيفك" in user_input:
            bot.reply_to(message, "الحمدلله، أنا تمام! انت كيفك؟")
            return
        
        # استخدام Gemini
        response = model.generate_content(
            f"المستخدم اسمه {user_name}. سؤاله: {user_input}\nرد عليه بلغة عربية فصيحه وبشكل مفيد."
        )
        
        bot.reply_to(message, response.text[:4000])
        
    except Exception as e:
        print(f"خطأ: {e}")
        bot.reply_to(message, "⚠️ حصل خطأ تقني، جرب تسأل بطريقة تانية")

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"⚠️ خطأ في الاتصال: {e}")
            time.sleep(3)
