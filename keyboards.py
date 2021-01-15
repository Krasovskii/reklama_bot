from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# start buttons
zakrep_btn = InlineKeyboardButton(text='📌Закреп', callback_data='zakrep')
text_btn = InlineKeyboardButton(text='📝Текст', callback_data='textre')
bot_btn = InlineKeyboardButton(text='🤖Бот', callback_data='bot')
knopka_btn = InlineKeyboardButton(text='🕹Кнопка', callback_data='knopka')

# inside buttons
nazad_btn = InlineKeyboardButton(text='⏪Назад', callback_data='back')
zakaz_btn = InlineKeyboardButton(text='Заказать', url='https://t.me/mmmoneyadmin', callback_data='zakaz')

markup_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            zakrep_btn, text_btn
        ],
        [
            bot_btn, knopka_btn
        ]
    ]
)

markup_buy = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            nazad_btn, zakaz_btn
        ]
    ]
)

