from nandhabot import bot
import logging 
from nandhabot import SUPPORT

# enable logging
FORMAT = "[NekosBestBot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)


if __name__ == "__main__":
   bot.run()
   with bot:
        bot.send_message(f"@{SUPPORT}", "Hello there I'm Now online")
