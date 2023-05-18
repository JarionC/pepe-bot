import random
import asyncio
from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext

bot = Bot(token="5704485196:AAFCQCxyqm85sI-In90d7FQcJ8qDqWELUSw")
update_queue = asyncio.Queue()
updater = Updater(bot=bot, update_queue=update_queue)

# List of memes (these can be links to images, or text memes)
memes = ["Meme 1", "Meme 2", "Meme 3", "...", "Meme n"]

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola {}! Soy Peso-bot, aquí para ayudarte con $PESO!".format(user.first_name))

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ayuda para ti!")

def meme(update: Update, context: CallbackContext) -> None:
    """Send a meme when the command /meme is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(memes))

def addresses(update: Update, context: CallbackContext) -> None:
    """Send the contract addresses."""
    message = """
    Owner Addr : 0xF097802Edd7926C78d4EfFa21fCd27D2146Bd229
    Liq. Airdrops : 0xC543B571FfA82C22F657C35424a208ceAdE43D84
    Comm. Airdrops : 0xcaf2608C3100b73133F86468248E
    CEX Reserve : 0x5815Dce1d0fdc4b9989c48DC69b1d0107cBFFDEf
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def website(update: Update, context: CallbackContext) -> None:
    """Send the website link."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Website: www.pepepeso.vip")

def twitter(update: Update, context: CallbackContext) -> None:
    """Send the Twitter link."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Twitter: https://twitter.com/Pepe_Peso")

def telegram(update: Update, context: CallbackContext) -> None:
    """Send the Telegram link."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Telegram: https://t.me/pepepeso")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('meme', meme))
updater.dispatcher.add_handler(CommandHandler('addresses', addresses))
updater.dispatcher.add_handler(CommandHandler('website', website))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram))

async def main():
    await updater.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
