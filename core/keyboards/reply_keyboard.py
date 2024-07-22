from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="SEND MESSAGE"
            )
        ],
        [
            KeyboardButton(
                text="USERS"
            )
        ]
    ],
    resize_keyboard=True
)