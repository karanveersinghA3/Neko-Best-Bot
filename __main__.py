import logging, os, random
from pyrogram import filters, Client 
from pyrogram.types import Message 
import requests 

# enable logging
FORMAT = "[NekosBestBot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SUPPORT = os.environ.get("SUPPORT", None)
UPDATES = os.environ.get("UPDATES", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) 
PM_START_IMG = os.environ.get("PM_START_IMG" , None)
PM_START_TEXT = os.environ.get("PM_START_TEXT", None) 

bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


PM_START_TEXT = "hello! {}\nI'm anime themed nekos bot below click the help button know my commandslist!"


buttons = [[
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_back"),
           ],[
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES}")]]

@bot.on_message(filters.command("start"))
async def start(_, m):
        await m.reply_photo(photo=PM_START_IMG,caption=PM_START_TEXT.format(m.from_user.mention),
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
           await query.edit_caption(HELP_TEXT,
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT}")]]))

@bot.on_message(filters.command("cuddle"))
def cuddle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("shrug"))
def shrug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

      
@bot.on_message(filters.command("poke"))
def poke(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("facepalm"))
def facepalm(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("stare"))
def stare(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
      
@bot.on_message(filters.command("pout"))
def pout(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("handhold"))
def handhold(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wave"))
def wave(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("blush"))
def blush(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("neko"))
def neko(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          reply.reply_photo(url)
      else:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          m.reply_photo(url)

@bot.on_message(filters.command("dance"))
def dance(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("baka"))
def baka(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("bore"))
def bore(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("laugh"))
def laugh(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("smug"))
def smug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("thumbsup"))
def thumbsup(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("shoot"))
def shoot(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("tickle"))
def tickle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("feed"))
def feed(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("think"))
def think(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wink"))
def wink(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("sleep"))
def sleep(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("punch"))
def punch(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
 


@bot.on_message(filters.command("cry"))
def cry(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/cry").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
   
@bot.on_message(filters.command("kill"))
def kill(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kill").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kill").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
      
@bot.on_message(filters.command("smile"))
def smile(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/smile").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("highfive"))
def highfive(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/highfive").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/highfive").json()
          url = api["url"]      
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("slap"))
def slap(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           m.reply_animation(url)      
         
    
@bot.on_message(filters.command("kick"))
def kick(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kick").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kick").json()
          url = api["url"]     
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("hug"))
def hug(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/hug").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/hug").json()
          url = api["url"]  
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("pat"))
def pat(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/pat").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/pat").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("waifu"))
def waifu(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/waifu").json()
           url = api["url"]
           reply.reply_photo(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/waifu").json()
          url = api["url"]       
          m.reply_photo(photo=url)
    
bot.run()
   with bot:
        bot.send_message(f"@{SUPPORT_CHAT}", "Hello there I'm Now online")
