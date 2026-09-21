from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from keyboards.inline import create_categories_menu, show_product_by_category
router = Router()


@router.callback_query(F.data.regexp(r"^category_(\d+)$"))
async def show_product(callback: CallbackQuery):
    """Показ всех продуктов из конкретной категории"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    category_id = int(callback.data.split("_")[-1])

    try:
        await callback.bot.edit_message_text(
            text="Выберите продукты:",
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=show_product_by_category(category_id))
    except TelegramBadRequest:
        await callback.answer("Категория не найдена")


@router.callback_query(F.data == "from_detail_to_category")
async def return_to_category(callback: CallbackQuery):
    """Возврат к списку категорий"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    await callback.bot.edit_message_text(
        text="Выберите категорию:",
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=create_categories_menu(chat_id)
    )
