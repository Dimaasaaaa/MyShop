from aiogram import Router, F
from aiogram.types import Message, chat, ReplyKeyboardRemove

from database.utils import db_update_user
from keyboards.reply import get_main_menu

router = Router()

@router.message(F.contact)
async def update_contact(message: Message):
    """обновление данных пользователя, получение номера телефона"""
    chat_id = message.chat.id
    phone = message.contact.phone_number

    db_update_user(chat_id, phone)

    if db_create_user_cart(chat_id):
        await message.answer(text="Вы зарегистрированы")
    await show_main_menu(message)


async def show_main_menu(message: Message):
    """Демонстрация основного меню"""
    await message.answer("Сделайте выбор", reply_markup=get_main_menu())