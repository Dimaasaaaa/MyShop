from aiogram import Router, F, Bot
from aiogram.types.message import Message
from aiogram.exceptions import TelegramBadRequest
from handlers.h03_order_handler import make_order

router = Router()

@router.message(F.text=='Назад⏪')
async def return_to_category_menu(message: Message, bot: Bot):
    """Возврат пользователя к категориям с удалением предыдущего сообщения"""
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    except TelegramBadRequest:
        pass
    await make_order(message, bot)