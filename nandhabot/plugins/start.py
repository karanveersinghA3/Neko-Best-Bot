from nandhabot import bot
from pyrogram import filters
from pyrogram.types import *
from nandhabot import PM_START_TEXT

@bot.on_message(filters.command("start"))
async def (_, m):
        await m.reply_text(PM_START_TEXT)
   
