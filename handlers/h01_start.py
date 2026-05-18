from aiogram import Router,F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from keyboard.reply import start_keyboard

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    """обработка старта"""

    photo = FSInputFile("media/welcome1.jpeg")
    await message.answer_photo(
           photo = photo,
        caption = f"Привет {message.from_user.full_name} для работы нажмите на кнопку",
        reply_markup = start_keyboard()
    )
