from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

rt = Router()

# Хэндлер для отлова сообщениий
@rt.message()
async def send_answer(msg: Message):
    await msg.answer(text=LEXICON_RU['other'])
