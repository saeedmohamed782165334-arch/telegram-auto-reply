from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

client = TelegramClient("my_account", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if event.is_private:
        await event.reply("هلا حب ماعندي نت بسرق نت واجي😂😂")

client.start()
print("الرد التلقائي شغال!")
client.run_until_disconnected()
