
from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# Кнопки основного меню
btn_cartomancy = InlineKeyboardButton(text=LEXICON_RU['cartomancy'])
btn_lk = InlineKeyboardButton(text=LEXICON_RU['lk'])
btn_pay = InlineKeyboardButton(text=LEXICON_RU['pay'])
btn_feedback = InlineKeyboardButton(text=LEXICON_RU['feedback'])

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[[btn_cartomancy],
                     [btn_lk],
                     [btn_pay],
                     [btn_feedback]],
)

# Кнопки выбора пола
btn_male = KeyboardButton(text=LEXICON_RU['male'])
btn_female = KeyboardButton(text=LEXICON_RU['female'])
fm_builder = ReplyKeyboardBuilder()
fm_builder.row(btn_female, btn_male, width=2)

fm_kb: ReplyKeyboardMarkup = fm_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)
