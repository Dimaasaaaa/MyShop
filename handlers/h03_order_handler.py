from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from keyboards.reply import back_to_main_menu
from keyboards.inline import create_categories_menu
from database.utils import db_get_last_orders
from handlers.h02_get_contact import show_main_menu

router = Router()

@router.message(F.text == "Сделать заказ 🛎")
async def make_order(message: Message, bot: Bot):
    """Оформление заказа, кнопка перехода в меню заказа"""
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Формируем заказ:", reply_markup=back_to_main_menu())
    await message.answer(text="Выберете категорию", reply_markup=create_categories_menu(chat_id))


@router.message(F.text == "История 📚")
async def make_history(message: Message):
    """Обработка истории заказа"""
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)

    if not orders:
        await message.answer(text="У вас нет истории заказов ＞﹏＜")
        return
    text = "Ваша история: \n\n"
    for order in orders:
        text += f"{order.product_name} - {order.final_price} руб. - {order.quantity}шт.\n"
    await message.answer(text=text)


@router.message(F.text == "Главное меню 🔙")
async def handle_main_menu(message: Message, bot: Bot):
    """Возврат в главное меню и удаление прошлого сообщения"""
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id -1)
    except  TelegramBadRequest:
        pass

    await show_main_menu(message)