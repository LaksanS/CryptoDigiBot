from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_API_TOKEN' with your bot's API token
API_TOKEN = '7394480636:AAFwZ9k-mL3mYDB3_L0-sR-lki6OyS4ESYo'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your CryptoDigiBot.')

def main():
    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
