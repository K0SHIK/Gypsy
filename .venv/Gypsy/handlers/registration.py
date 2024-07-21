from aiogram import F, Router
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message, TelegramObject
import logging

from keyboards.keyboards import fm_kb, menu_kb
from lexicon.lexicon_ru import LEXICON_RU
from databases.PSQL import check_user

logger = logging.getLogger(__name__)
rt = Router()

# Хэндлер на комманду /start
@rt.message(CommandStart())
async def start_command(msg: Message, config):
    await msg.answer(LEXICON_RU[msg.text])
    name = check_user(msg.from_user.id, config)
    if name:
        await menu_command(msg)
    else:
        logger.info('Новый пользователь с tg_id %s', msg.from_user.id)