from telegram.ext import *
import constants as keys
import responses as R

print("Bot has started...")

def start_command(update, context):
    update.message.reply_text('Can\'t decide where to eat? Sit back and just let me do all the work for you!')

def help_command(update, context):
    update.message.reply_text('You can narrow down your choices by picking a specific cuisine or food item, filtering by budget or go completely crazy and let me pick a random place ;)\
        \n\nJust click on one of the commands to get started!')

def custom_command(update, context):
    update.message.reply_text('this is a custom command!')


def handle_message(update, context):
    text = str(update.message.text).lower() # receives text from user
    response = R.handle_responses(text)      # processes the text

    update.message.reply_text(response)     # returns back to user

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("custom", custom_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling() # in seconds
    updater.idle()          # stay active

main()