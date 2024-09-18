from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)


main1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='получить telegram premium', request_contact=True)],
    ],
resize_keyboard=True

)

#main = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [InlineKeyboardButton(text='ПОЛУЧИТЬ PREMIUM', url='https://sudoteach.com/content/2/30')]
#    ],
#resize_keyboard=True)
