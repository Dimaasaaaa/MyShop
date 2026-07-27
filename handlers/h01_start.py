from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

from database.utils import db_register_user
from keyboards.reply import start_keyboard

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """обработка старта"""

    photo = FSInputFile('media/hello.jpg')
    await message.answer_photo(
        photo=photo,
        caption=f'привет {message.from_user.full_name} для работы нажмите на кнопку',
        reply_markup=start_keyboard()
    )


@router.message(F.text=='начать 😀')
async def handle_start_button(message: Message):
    """обработка кнопки начать"""

    await handle_start(message)

async def handle_start(message: Message):
    await register_user(message)


async def register_user(message: Message):
    """регистрация пользователя и доступ к основному меню"""
    chat_id = message.chat.id
    full_name = message.from_user.full_name

    if db_register_user(full_name, chat_id):
        await message.answer(text='Добро пожаловать!')
        await show_main_menu(message)
    else:
        await message.answer(text='для работы нужен ваш номер телефона', reply_markup=phone_button())