from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import random

# Bot's token
updater = Updater("5704485196:AAFCQCxyqm85sI-In90d7FQcJ8qDqWELUSw")

# List of meme URLs
memes = [
    "https://yourserver.com/meme1.jpg",
    "https://yourserver.com/meme2.jpg",
    "https://yourserver.com/meme3.jpg",
    # Add as many memes as you want...
]

# A function to show greetings
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hola, amigo! I am Peso-bot, your friendly guide to the world of Pepe Peso ($PESO). How can I help you today? Para continuar, escribe /help.')

# Bot's help prompt
#'/meme - Get a random meme\n'
def help(update: Update, context: CallbackContext):
    update.message.reply_text('Here are commands you can use:\n'
                              '/tokenomics - Learn about Pepe Peso\'s tokenomics\n'
                              '/addresses - Get information about associated addresses\n'
                              '/links - Get links to our website and social media')

# A function to show the tokenomics
def tokenomics(update: Update, context: CallbackContext):
    update.message.reply_text("Here's how our $PESO tokenomics work, mi amigo:\n"
                              "Total Supply: 430,000,000,000,000\n"
                              "NO TAXES - In honor of the great Mexican Dream.\n"
                              "80% of our $PESO is in PancakeSwap, stuffed like a well-filled piñata!\n"
                              "10% is for our hardworking Liquidity Providers. Muchas gracias for your support!\n"
                              "3% is dedicated to airdrops for community engagement.\n"
                              "The remaining 7% is for expanding our fiesta to other exchanges, building bridges, and spreading the word about Pepe Peso!\n"
                              "Initial LP tokens will be burned, like the heat of a habanero.")

# A function to show associated addresses
def addresses(update: Update, context: CallbackContext):
    update.message.reply_text("These are our important addresses, compadre:\n"
                              "Owner Addr: 0xF097802Edd7926C78d4EfFa21fCd27D2146Bd229\n"
                              "Liq. Airdrops: 0xC543B571FfA82C22F657C35424a208ceAdE43D84\n"
                              "Comm. Airdrops: 0xcaf2608C3100E234059D0330b73133F86468248E\n"
                              "CEX Reserve: 0x5815Dce1d0fdc4b9989c48DC69b1d0107cBFFDEf")

# A function to send a random meme
def meme(update: Update, context: CallbackContext):
    meme_url = random.choice(memes)  # Select a random meme
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=meme_url)

# A function to show links
def links(update: Update, context: CallbackContext):
    update.message.reply_text("Check us out, compadre!\n"
                              "Website: www.pepepeso.vip\n"
                              "Twitter: https://twitter.com/Pepe_Peso\n"
                              "Telegram: https://t.me/pepepeso")

# Handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('tokenomics', tokenomics))
updater.dispatcher.add_handler(CommandHandler('addresses', addresses))
updater.dispatcher.add_handler(CommandHandler('meme', meme))
updater.dispatcher.add_handler(CommandHandler('links', links))

# Run the bot
updater.start_polling()
updater.idle()
