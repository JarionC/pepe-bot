import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# List of memes (these can be links to images, or text memes)
memes = ["Meme 1", "Meme 2", "Meme 3", "...", "Meme n"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola {}! Soy Peso-bot, aquí para ayudarte con $PESO!".format(user.first_name))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ayuda para ti!")

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a meme when the command /meme is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(memes))

async def addresses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the contract addresses."""
    message = """
    Owner Addr : 0xF097802Edd7926C78d4EfFa21fCd27D2146Bd229
    Liq. Airdrops : 0xC543B571FfA82C22F657C35424a208ceAdE43D84
    Comm. Airdrops : 0xcaf2608C3100b73133F86468248E
    CEX Reserve : 0x5815Dce1d0fdc4b9989c48DC69b1d0107cBFFDEf
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the website link."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Website: www.pepepeso.vip")

async def twitter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the Twitter link."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Twitter: https://twitter.com/Pepe_Peso")

async def telegram(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the Telegram link."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Telegram: https://t.me/pepepeso")

def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5704485196:AAFCQCxyqm85sI-In90d7FQcJ8qDqWELUSw").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("meme", meme))
    application.add_handler(CommandHandler("addresses", addresses))
    application.add_handler(CommandHandler("website", website))
    application.add_handler(CommandHandler("twitter", twitter))
    application.add_handler(CommandHandler("telegram", telegram))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
