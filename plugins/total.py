from pyrogram import Client, filters
from config import ADMINS
from .database import collection

@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total_message(c,m):
    txt= await m.reply('Processing...')
    total = collection.find().count()
    await txt.edit(f"{str(total)} Files Total")