from telethon import TelegramClient, events
from telethon.tl.custom import Button
import asyncio
import datetime
from config import api_id, api_hash

client = TelegramClient('user_session', api_id, api_hash)

async def main():
    await client.start()
    me = await client.get_me()
    print(f"✅ يوزر بوت {me.first_name} شغال وجاهز!")

    # ===== رد على كلمة "ملف obb" =====
    @client.on(events.NewMessage(pattern=r'(?i)(ملف obb|اوبيبي|obb|اوبي)'))
    async def obb_menu(event):
        buttons = [
            [Button.inline("📦 32 بت", b"obb_32")],
            [Button.inline("📦 64 بت", b"obb_64")]
        ]
        await event.reply("📁 **اختر نوع ملف OBB:**", buttons=buttons)

    # ===== رد على كلمة "مشكلة" =====
    @client.on(events.NewMessage(pattern=r'(?i)(مشكله|مشكلة|عندي مشكله|مشكلتي)'))
    async def problem_menu(event):
        buttons = [
            [Button.inline("❌ التطبيق غير متوافق", b"prob_incompatible")],
            [Button.inline("⚠️ خطأ في ZArchiver", b"prob_zarchiver")],
            [Button.inline("📲 طريقة التثبيت", b"prob_install")],
            [Button.inline("📁 تركيب OBB", b"prob_obb")],
            [Button.inline("🔑 كود النسخة", b"prob_code")],
            [Button.inline("⚡ تقطيع (اسبيد)", b"prob_speed")],
            [Button.inline("📞 التواصل مع المطورين", b"prob_contact")]
        ]
        await event.reply("🔍 **اختر مشكلتك:**", buttons=buttons)

    # ===== معالج الأزرار =====
    @client.on(events.CallbackQuery)
    async def callback(event):
        data = event.data.decode()
        
        if data == "obb_32":
            await event.edit("📦 **OBB 32 بت:**\nhttps://t.me/GSN_MOD_OBB/31")
        elif data == "obb_64":
            await event.edit("📦 **OBB 64 بت:**\nhttps://t.me/GSN_MOD_OBB/33")
        elif data == "prob_incompatible":
            await event.edit("❌ **مشكلة: التطبيق غير متوافق**\n✅ **الحل:**\n1. جرب v3 (للجوالات الضعيفة)\n2. تأكد من إصدار أندرويد 8+")
        elif data == "prob_zarchiver":
            await event.edit("⚠️ **مشكلة: خطأ في ZArchiver**\n✅ **الحل:**\n1. أعد تشغيل الجوال\n2. تأكد من المساحة\n3. أعد تثبيت ZArchiver")
        elif data == "prob_install":
            await event.edit("📲 **طريقة التثبيت:**\n1. حمّل ملف APK\n2. افتحه\n3. اضغط 'تثبيت'\n4. وافق على الصلاحيات")
        elif data == "prob_obb":
            await event.edit("📁 **طريقة تركيب OBB:**\nhttps://t.me/GSN_MOD_FILE/26")
        elif data == "prob_code":
            await event.edit("🔑 **للحصول على كود النسخة:**\nأرسل رقم النسخة (مثال: كود 1)")
        elif data == "prob_speed":
            await event.edit("⚡ **حل مشكلة التقطيع (الاسبيد):**\nhttps://t.me/GSN_MOD_FILE/24")
        elif data == "prob_contact":
            await event.edit("📞 **للتواصل مع المطورين:**\n@GSN_MOD_1")
        
        await event.answer()

    # ===== ردود سريعة =====
    @client.on(events.NewMessage)
    async def default(event):
        text = event.message.text.lower()
        
        if "السلام" in text:
            await event.reply("🌹 وعليكم السلام")
        elif "شكرا" in text:
            await event.reply("🤍 العفو")
        elif "كود v1" in text:
            await event.reply("🔥 https://t.me/kenan_mod_2/37")
        elif "كود v2" in text:
            await event.reply("⚡ https://t.me/kenan_mod_2/44")
        elif "كود v3" in text:
            await event.reply("🎯 https://t.me/kenan_mod_2/47")
        elif "سكنات" in text:
            await event.reply("🎭 قريبًا في v4")
        elif "v4" in text:
            await event.reply("⏳ قيد الإعداد")
        elif "ما يشتغل" in text:
            await event.reply("🔧 تأكد من OBB والمساحة")
        elif "نكتة" in text:
            await event.reply("😂 مرة واحد بوت...")
        elif "مطور" in text:
            await event.reply("👨‍💻 @GSN_MOD_1")
        elif "القناة" in text:
            await event.reply("📢 @kenan_mod_2")

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
