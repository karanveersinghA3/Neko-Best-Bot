from nandhabot import bot
from pyrogram import filters
from pyrogram.types import *
from nandhabot import PM_START_TEXT


buttons = [[
            InlineKeyboardButton("ADD ME", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
            InlineKeyboardButton("HELP", callback_data='help_back'),
           ],[
            InlineKeyboardButton("SUPPORT", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("UPDATES", url=f"https://t.me/{UPDATES}")]]

@bot.on_message(filters.command("start"))
async def (_, m):
        await m.reply_text(PM_START_TEXT,)
   
