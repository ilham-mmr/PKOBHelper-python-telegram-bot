#!/usr/bin/env python3
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler, PicklePersistence
import re

import api
from keyboard import START_KEYBOARD, ABOUT_KEYBOARD
from strings import VICTIM_INFO_REGEX, START_MSG, VICTIM_INFO_MSG, START_ECHO_MSG, GET_VICTIM_MSG, GET_HELP_MSG, WEBISTE_MSG, ABOUT_DEVELOPER_MSG, ABOUT_BOT_MSG, ABOUT_GENERAL_MSG

from config import PORT,TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        START_MSG.format(update.effective_user.full_name),
        reply_markup=START_KEYBOARD
    )


def get_victim(update: Update, context: CallbackContext) -> int:
    info = re.match(VICTIM_INFO_REGEX, update.message.text)
    if info is None:
        update.message.reply_text(
            START_MSG.format(update.effective_user.full_name),
            reply_markup=START_KEYBOARD
        )

    arr = info.string.split('#')
    ic = arr[0]
    phone = arr[1]
    update.message.reply_text(
        f'getting victim\'s info...'
    )
    victim = api.get_victim_info(ic, phone)
    if(victim):
        update.message.reply_text(VICTIM_INFO_MSG.format(
            victim['ic'], victim['phone'], victim['name'], victim['age']), parse_mode=ParseMode.HTML, reply_markup=START_KEYBOARD)
    else:
        update.message.reply_text(
            f'the victim is not found, please register on https://pkob268954.herokuapp.com/', reply_markup=START_KEYBOARD)


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        START_ECHO_MSG.format(update.effective_user.full_name),
        reply_markup=START_KEYBOARD
    )


def victim_callback(update: Update, context: CallbackContext):
    update.callback_query.answer()
    update.callback_query.message.reply_text(GET_VICTIM_MSG.format(
        update.effective_user.full_name), parse_mode=ParseMode.HTML, reply_markup=START_KEYBOARD)


def website_callback(update: Update, context: CallbackContext):
    update.callback_query.answer()
    update.callback_query.message.reply_text(
        WEBISTE_MSG, reply_markup=START_KEYBOARD)


def help_callback(update: Update, context: CallbackContext):
    update.callback_query.answer()
    update.callback_query.message.reply_text(
        GET_HELP_MSG, reply_markup=START_KEYBOARD)


def about_callback(update: Update, context: CallbackContext):
    # Must call answer!
    update.callback_query.answer()
    query = update.callback_query
    data = query.data.split('_')[-1]
    if data == 'developer':
        update.callback_query.message.reply_text(
            ABOUT_DEVELOPER_MSG, reply_markup=ABOUT_KEYBOARD)
    elif data == 'bot':
        update.callback_query.message.reply_text(
            ABOUT_BOT_MSG, reply_markup=ABOUT_KEYBOARD)
    else:
        update.callback_query.message.reply_text(
            ABOUT_GENERAL_MSG.format(update.effective_user.first_name), reply_markup=ABOUT_KEYBOARD)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(
    CallbackQueryHandler(victim_callback, pattern=r"victim"))
updater.dispatcher.add_handler(
    CallbackQueryHandler(website_callback, pattern=r"website"))
updater.dispatcher.add_handler(
    CallbackQueryHandler(help_callback, pattern=r"help"))
updater.dispatcher.add_handler(
    CallbackQueryHandler(about_callback, pattern=r"about_"))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(VICTIM_INFO_REGEX), get_victim))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text & ~Filters.command, echo))


updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN, webhook_url="https://pkob268954bot.herokuapp.com/" + TOKEN)

updater.idle()

