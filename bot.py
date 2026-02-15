from telethon import TelegramClient

api_id = 39458857
api_hash = '3b62c284e0f6b6b0b16ba6d7b46a4a6f'

client = TelegramClient('GSNMOD', api_id, api_hash)

async def main():
    await client.send_message('me', '✅ يوزر بوت شغال باسم GSNMOD!')

with client:
    client.loop.run_until_complete(main())
