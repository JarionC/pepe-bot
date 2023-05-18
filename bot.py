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
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hola, {user.first_name}! I'm your Peso-bot, here to assist with all things $PESO. Let's rock y roll!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="No problemo, amigo! Need some help? Just use these commands: /meme, /addresses, /website, /twitter, /telegram.")

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ready for a $PESO meme, amigo? Here you go: {random.choice(memes)}")

async def addresses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
    Owner Addr : 0xF097802Edd7926C78d4EfFa21fCd27D2146Bd229
    Liq. Airdrops : 0xC543B571FfA82C22F657C35424a208ceAdE43D84
    Comm. Airdrops : 0xcaf2608C3100b73133F86468248E
    CEX Reserve : 0x5815Dce1d0fdc4b9989c48DC69b1d0107cBFFDEf
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Looking for $PESO addresses, compadre? Here they are:\n{message}")

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Want to explore more about $PESO, amigo? Check our website: www.pepepeso.vip")

async def twitter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Follow the $PESO journey on Twitter, compadre! Here's our handle: https://twitter.com/Pepe_Peso")

async def telegram(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Join our $PESO community on Telegram, amigo! Here's the link: https://t.me/pepepeso")

def main() -> None:
    application = Application.builder().token("5704485196:AAFCQCxyqm85sI-In90d7FQcJ8qDqWELUSw").build()

    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("meme", meme))
    application.add_handler(CommandHandler("addresses", addresses))
    application.add_handler(CommandHandler("website", website))
    application.add_handler(CommandHandler("twitter", twitter))
    application.add_handler(CommandHandler("telegram", telegram))

    application.run_polling()

if __name__ == "__main__":
    main()
