from nandhabot import bot
from pyrogram import filters
from pyrogram.types import *
from nandhabot import PM_START_TEXT, PM_START_IMG, UPDATES, SUPPORT, BOT_USERNAME


buttons = [[
            InlineKeyboardButton("ADD ME", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
            InlineKeyboardButton("HELP", callback_data="help_back"),
           ],[
            InlineKeyboardButton("SUPPORT", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("UPDATES", url=f"https://t.me/{UPDATES}")]]

@bot.on_message(filters.command("start"))
async def start(_, m):
        await m.reply_photo(photo=PM_START_IMG,caption=PM_START_TEXT,
             reply_markup=InlineKeyboardMarkup(buttons))
   
HELP_TEXT = """
anime themed **SFW**:

**image:**
`neko, waifu`

**animation:**
`cry, kill, smile, 
highfive, slap, kick, 
hug, pat, punch,
sleep, wink, think, 
feed, tickle, shoot, 
thumbsup, smug, laugh, 
bore, baka, dance,
blush, facepalm, stare, 
pout, handhold, wave, 
cuddle, poke, shrug`
"""

@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
           query = query.message
           await query.edit(HELP_TEXT)
