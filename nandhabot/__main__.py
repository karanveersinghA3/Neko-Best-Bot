import os
import logging
import pyrogram

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="nandhabot/plugins")
    bot = pyrogram.Client(
        "nandhabot",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    bot.run()
