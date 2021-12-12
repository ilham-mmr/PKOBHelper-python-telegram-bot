from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_KEYBOARD = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Get Victim Info", callback_data='victim'),

        ],
        [
            InlineKeyboardButton("website", callback_data='website'),
            InlineKeyboardButton("Help", callback_data='help'),
            InlineKeyboardButton("About", callback_data='about_general'),
        ]
    ])

ABOUT_KEYBOARD = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Developer Contact", callback_data='about_developer'),
            InlineKeyboardButton("What is this bot?", callback_data='about_bot'),
        ]
    ])