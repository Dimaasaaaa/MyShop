from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, FSInputFile, InlineKeyboardMarkup


router = Router()

@router.callback_query(F.data.regexp(r"action [+-]"))
async def change_product_quantity(callback: CallbackQuery, bot:Bot):
    """Изменение кол-ва продуктов"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    action = callback.data.split()[-1]

    product_name = callback.data.split('\n')[0]
    product = db.get_product_by_name(product_name)