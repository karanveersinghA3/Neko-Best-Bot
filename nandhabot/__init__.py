import os
from pyrogram import Client 

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SUPPORT = os.environ.get("SUPPORT", None)
UPDATES = os.environ.get("UPDATES", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) 
PM_START_IMG = os.environ.get("PM_START_IMG" , "https://telegra.ph/file/895f87f9f8028ecc4b632.jpg")

bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))


PM_START_TEXT = "hello! {}\nI'm anime themed nekos bot below click the help button know my commandslist!"
