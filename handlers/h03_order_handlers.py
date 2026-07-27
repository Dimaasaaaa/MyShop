from aiogram import Router, F
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove

from keyboards.inline import create_categories_menu

router = Router()

@router.message(F.text == "Оформлить заказ")
async def make_order(message: Message, bot: Bot):
    """Оформление заказа, кнопка перехода в меню заказа"""
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Сделайте выбор товара:", reply_markup=back_to_main_menu())
    await message.answer(text="Выберете категорию", reply_markup=create_categories_menu())